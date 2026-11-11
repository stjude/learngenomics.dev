const BACKBONE = new Set(["N", "CA", "C", "O"]);

/**
 * Trims a PDB file to one chain's backbone atoms, plus every atom of the
 * residues in `keepResidues`, and moves the coordinates by `rotation` (a 3x3
 * matrix) and `translation`. Keeps that chain's HELIX and SHEET records so the
 * cartoon is drawn the same way.
 */
export default function prepareStructure(
  pdb,
  { chain, keepResidues = [], rotation, translation = [0, 0, 0] },
) {
  const keep = new Set(keepResidues);
  const lines = [];
  for (const line of pdb.split("\n")) {
    const record = line.slice(0, 6).trim();
    if (record === "HELIX") {
      if (line[19] === chain) lines.push(line);
    } else if (record === "SHEET") {
      if (line[21] === chain) lines.push(line);
    } else if (record === "ATOM" && line[21] === chain) {
      const name = line.slice(12, 16).trim();
      const residue = Number(line.slice(22, 26));
      if (!BACKBONE.has(name) && !keep.has(residue)) continue;
      const p = [30, 38, 46].map((at) => Number(line.slice(at, at + 8)));
      const moved = rotation.map(
        (row, i) =>
          row[0] * p[0] + row[1] * p[1] + row[2] * p[2] + translation[i],
      );
      lines.push(
        line.slice(0, 30) +
          moved.map((value) => value.toFixed(3).padStart(8)).join("") +
          line.slice(54),
      );
    }
  }
  lines.push("END");
  return lines.join("\n");
}
