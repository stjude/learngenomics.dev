"""Check that the atom-level drawings in figures 7.3, 7.8, 7.10 and 7.11 are chemically correct.

Each figure's molecule graph is converted to an RDKit molecule and compared with the
PubChem structure of the matching nucleotide; the hydrogen-bonding atoms in figures 7.3
and 7.10 are confirmed with SMARTS patterns. Needs RDKit (pip install -r requirements-checks.txt).
Exits with status 1 if any check fails.
"""

import sys

from rdkit import Chem

from figures import rna_atoms
from figures.dna_atoms import build_bases, build_pairs
from figures.molecules import G

# PubChem isomeric SMILES of the 5'-monophosphates.
DNA_REF = {"A": ("dAMP, CID 12599", "C1[C@@H]([C@H](O[C@H]1N2C=NC3=C(N=CN=C32)N)COP(=O)(O)O)O"),
           "G": ("dGMP, CID 135398597", "C1[C@@H]([C@H](O[C@H]1N2C=NC3=C2N=C(NC3=O)N)COP(=O)(O)O)O"),
           "T": ("dTMP, CID 9700", "CC1=CN(C(=O)NC1=O)[C@H]2C[C@@H]([C@H](O2)COP(=O)(O)O)O"),
           "C": ("dCMP, CID 13945", "C1[C@@H]([C@H](O[C@H]1N2C=CC(=NC2=O)N)COP(=O)(O)O)O"),
           "5mC": ("5-Methyl dCMP, CID 102276", "CC1=CN(C(=O)N=C1N)[C@H]2C[C@@H]([C@H](O2)COP(=O)(O)O)O")}
RNA_REF = {"A": ("AMP, CID 6083", "C1=NC(=C2C(=N1)N(C=N2)[C@H]3[C@@H]([C@@H]([C@H](O3)COP(=O)(O)O)O)O)N"),
           "U": ("UMP, CID 6030", "C1=CN(C(=O)NC1=O)[C@H]2[C@@H]([C@@H]([C@H](O2)COP(=O)(O)O)O)O")}

# Watson-Crick donor and acceptor atoms, described by their chemical environment.
HBOND_ATOMS = {"A.N1": "[#7;R;X2]~[#6;R](-[#7;!R;H2])",
               "A.N6": "[#7;!R;H2]-[#6;R]",
               "T.O4": "[#8;X1]~[#6;R]~[#6;R]-[#6;!R]",
               "T.N3": "[#7;R;H1](~[#6]~[#8;X1])~[#6]~[#8;X1]",
               "G.O6": "[#8;X1]~[#6;R]~[#6;R2]",
               "G.N1": "[#7;R;H1](~[#6]~[#8;X1])~[#6]-[#7;!R]",
               "G.N2": "[#7;!R;H2]-[#6;R]~[#7;R;H1]",
               "C.N4": "[#7;!R;H2]-[#6;R]",
               "C.N3": "[#7;R;X2](~[#6]-[#7;!R;H2])~[#6]~[#8;X1]",
               "C.O2": "[#8;X1]~[#6;R]~[#7;R;X2]"}
# figure: (pairs for build_pairs, methylated prefixes, base drawn at each prefix, negative control)
# The control compares the first drawn nucleotide with a reference it must not match.
PAIR_FIGURES = {"7.10": ((("A", "T"), ("G", "C")), (), {"L0": "A", "R0": "T", "L1": "G", "R1": "C"}, "G"),
                "7.3": ((("C", "G"), ("G", "C")), ("L0", "R1"), {"L0": "5mC", "R0": "G", "L1": "G", "R1": "5mC"}, "C")}


def to_mol(g):
    """RDKit molecule from a molecule graph; atoms keep their graph names as the 'name' prop."""
    rw = Chem.RWMol(); idx = {}
    for n, at in g["atoms"].items():
        a = Chem.Atom(at["el"]); a.SetFormalCharge(at["charge"]); a.SetNoImplicit(at["el"] in "NO")
        a.SetProp("name", n); idx[n] = rw.AddAtom(a)
    for x, y, o, _ in g["bonds"]:
        rw.AddBond(idx[x], idx[y], Chem.BondType.DOUBLE if o == 2 else Chem.BondType.SINGLE)
    for n, at in g["atoms"].items():
        if at["label"] == "OH":
            rw.GetAtomWithIdx(idx[n]).SetNumExplicitHs(1)
        if at["label"] == "CH3":
            rw.GetAtomWithIdx(idx[n]).SetNoImplicit(False)
    m = rw.GetMol()
    Chem.SanitizeMol(m)
    return m, idx


def canon(m):
    m = Chem.RemoveHs(Chem.Mol(m), sanitize=True); Chem.RemoveStereochemistry(m)
    return Chem.MolToSmiles(m)


def neutral(m):
    rw = Chem.RWMol(m)
    for a in rw.GetAtoms():
        if a.GetFormalCharge() == -1:
            a.SetFormalCharge(0); a.SetNoImplicit(False)
    out = rw.GetMol(); Chem.SanitizeMol(out); return out


def hidden_h(m):
    """Nitrogens and oxygens carrying hydrogens that the drawing does not show."""
    return [a.GetProp("name") for a in m.GetAtoms() if a.GetSymbol() in "NO" and a.GetNumImplicitHs()]


def split_nucleotides(m, idx, links):
    """Cut each O3'-P link, cap the phosphate with OH, and return the nucleotide fragments."""
    cut = [m.GetBondBetweenAtoms(idx[f"{u}.O3'"], idx[f"{d}p.P"]).GetIdx() for u, d in links]
    rw = Chem.RWMol(Chem.FragmentOnBonds(m, cut, addDummies=True))
    for a in rw.GetAtoms():
        if a.GetAtomicNum() == 0:
            a.SetAtomicNum(8 if a.GetNeighbors()[0].GetSymbol() == "P" else 1); a.SetIsotope(0); a.SetNoImplicit(False)
    return Chem.GetMolFrags(rw.GetMol(), asMols=True, sanitizeFrags=True)


def check_pairs(fig):
    """Figures 7.3 and 7.10: four nucleotides and the hydrogen bonds between them."""
    ok = True
    pairs, methyl, bases, control_ref = PAIR_FIGURES[fig]
    build_pairs(pairs, methyl)
    m, idx = to_mol(G)
    print(f"figure {fig}: {m.GetNumAtoms()} atoms incl. drawn H, sanitized (valences OK)")
    for n in hidden_h(m):
        print("  hidden H on", n); ok = False
    frags = split_nucleotides(m, idx, (("L0s", "L1s"), ("R1s", "R0s")))
    assert len(frags) == 4, len(frags)
    first = None
    for fr in frags:
        names = {a.GetProp("name").split(".")[0] for a in fr.GetAtoms() if a.HasProp("name")}
        pre = [n for n in names if len(n) == 2][0]
        base = bases[pre]
        lab, smi = DNA_REF[base]
        mine, ref = canon(neutral(fr)), canon(Chem.MolFromSmiles(smi))
        good = mine == ref
        ok &= good
        if pre == "L0":
            first = mine
        print(f"  {pre} {base}: {'MATCH' if good else 'MISMATCH'} vs {lab}" + ("" if good else f"\n    fig {mine}\n    ref {ref}"))
    for h, acc in G["hbonds"]:
        don = [y if x == h else x for x, y, *_ in G["bonds"] if h in (x, y)][0]
        for nm in (don, acc):
            pre, at = nm.split(".")
            key = f"{bases[pre][-1]}.{at}"
            good = key in HBOND_ATOMS and idx[nm] in {
                mt[0] for mt in m.GetSubstructMatches(Chem.MolFromSmarts(HBOND_ATOMS[key]))}
            ok &= good
            print(f"  H-bond atom {pre} {key}: {'confirmed' if good else 'NOT CONFIRMED'}")
    for i in range(len(pairs)):
        print(f"  pair {i} ({bases[f'L{i}']}-{bases[f'R{i}']}) hydrogen bonds:",
              sum(1 for h, _ in G["hbonds"] if h.startswith((f"L{i}", f"R{i}"))))
    control = first == canon(Chem.MolFromSmiles(DNA_REF[control_ref][1]))
    print(f"  negative control ({bases['L0']} drawn vs {DNA_REF[control_ref][0]}) matches:", control)
    return ok and not control


def check_bases():
    """Figure 7.8: cap each sugar stub with H and compare with the base cut from its dNMP."""
    ok = True
    stubs = build_bases()
    m, idx = to_mol(G)
    rw = Chem.RWMol(m)
    for n, _ in stubs.values():
        h = rw.AddAtom(Chem.Atom(1)); rw.AddBond(idx[n], h, Chem.BondType.SINGLE)
    m = rw.GetMol(); Chem.SanitizeMol(m)
    for fr in Chem.GetMolFrags(m, asMols=True):
        k = fr.GetAtomWithIdx(0).GetProp("name").split(".")[0]
        ref = Chem.MolFromSmiles(DNA_REF[k][1])
        # the glycosidic bond: ring N (degree 3) to the sugar carbon next to the ring O
        gly = [b.GetIdx() for b in ref.GetBonds()
               if {b.GetBeginAtom().GetSymbol(), b.GetEndAtom().GetSymbol()} == {"C", "N"}
               and any(a.GetSymbol() == "N" and a.IsInRing() and a.GetDegree() == 3 and
                       any(x.GetSymbol() == "C" and x.IsInRingSize(5) and any(y.GetSymbol() == "O" and y.IsInRingSize(5) for y in x.GetNeighbors()) for x in a.GetNeighbors())
                       for a in (b.GetBeginAtom(), b.GetEndAtom()))
               and any(a.GetSymbol() == "C" and any(y.GetSymbol() == "O" and y.IsInRingSize(5) for y in a.GetNeighbors()) for a in (b.GetBeginAtom(), b.GetEndAtom()))]
        rwr = Chem.RWMol(Chem.FragmentOnBonds(ref, gly[:1], addDummies=True))
        for a in rwr.GetAtoms():
            if a.GetAtomicNum() == 0:
                a.SetAtomicNum(1); a.SetIsotope(0)
        parts = Chem.GetMolFrags(rwr.GetMol(), asMols=True, sanitizeFrags=True)
        basefrag = [p for p in parts if not any(a.GetSymbol() == "P" for a in p.GetAtoms())][0]
        good = canon(fr) == canon(basefrag)
        ok &= good
        print(f"figure 7.8 {k}: {'MATCH' if good else 'MISMATCH'} vs base of {DNA_REF[k][0]} ({canon(fr)})")
    return ok


def check_rna():
    """Figure 7.11: the two linked ribonucleotides."""
    ok = True
    rna_atoms.build()
    m, idx = to_mol(G)
    for fr in split_nucleotides(m, idx, (("L0s", "L1s"),)):
        b = "A" if any(a.HasProp("name") and a.GetProp("name").startswith("L0.") for a in fr.GetAtoms()) else "U"
        lab, smi = RNA_REF[b]
        mine, want = canon(neutral(fr)), canon(Chem.MolFromSmiles(smi))
        ok &= mine == want
        print(f"figure 7.11 {b}: {'MATCH' if mine == want else 'MISMATCH'} vs {lab}")
    for n in hidden_h(m):
        print("  hidden H on", n); ok = False
    return ok


if __name__ == "__main__":
    results = [check_pairs("7.10"), check_pairs("7.3"), check_bases(), check_rna()]
    print("ALL OK" if all(results) else "*** PROBLEMS ***")
    sys.exit(0 if all(results) else 1)
