'use client'

import clsx from 'clsx'
import { AnimatePresence, motion, useIsPresent } from 'framer-motion'
import Link from 'next/link'
import { usePathname } from 'next/navigation'
import { useRef } from 'react'

import { useIsInsideMobileNavigation } from '@/components/MobileNavigation'
import { useSectionStore } from '@/components/SectionProvider'
import { Tag } from '@/components/Tag'
import { remToPx } from '@/lib/remToPx'
import { CloseButton } from '@headlessui/react'

interface NavGroup {
  title: string
  links: Array<{
    title: string
    href: string
  }>
}

function useInitialValue<T>(value: T, condition = true) {
  let initialValue = useRef(value).current
  return condition ? initialValue : value
}

function NavLink({
  href,
  children,
  tag,
  active = false,
  isAnchorLink = false,
}: {
  href: string
  children: React.ReactNode
  tag?: string
  active?: boolean
  isAnchorLink?: boolean
}) {
  return (
    <CloseButton
      as={Link}
      href={href}
      aria-current={active ? 'page' : undefined}
      className={clsx(
        'flex justify-between gap-2 py-1 pr-3 text-sm transition',
        isAnchorLink ? 'pl-7' : 'pl-4',
        active
          ? 'text-zinc-900 dark:text-white'
          : 'text-zinc-600 hover:text-zinc-900 dark:text-zinc-400 dark:hover:text-white',
      )}
    >
      <span className="truncate">{children}</span>
      {tag && (
        <Tag variant="small" color="zinc">
          {tag}
        </Tag>
      )}
    </CloseButton>
  )
}

function VisibleSectionHighlight({
  group,
  pathname,
}: {
  group: NavGroup
  pathname: string
}) {
  let [sections, visibleSections] = useInitialValue(
    [
      useSectionStore((s) => s.sections),
      useSectionStore((s) => s.visibleSections),
    ],
    useIsInsideMobileNavigation(),
  )

  let isPresent = useIsPresent()
  let firstVisibleSectionIndex = Math.max(
    0,
    [{ id: '_top' }, ...sections].findIndex(
      (section) => section.id === visibleSections[0],
    ),
  )
  let itemHeight = remToPx(2)
  let height = isPresent
    ? Math.max(1, visibleSections.length) * itemHeight
    : itemHeight
  let top =
    group.links.findIndex((link) => link.href === pathname) * itemHeight +
    firstVisibleSectionIndex * itemHeight

  return (
    <motion.div
      layout
      initial={{ opacity: 0 }}
      animate={{ opacity: 1, transition: { delay: 0.2 } }}
      exit={{ opacity: 0 }}
      className="absolute inset-x-0 top-0 bg-zinc-800/10 will-change-transform dark:bg-white/10"
      style={{ borderRadius: 8, height, top }}
    />
  )
}

function ActivePageMarker({
  group,
  pathname,
}: {
  group: NavGroup
  pathname: string
}) {
  let itemHeight = remToPx(2)
  let offset = remToPx(0.25)
  let activePageIndex = group.links.findIndex((link) => link.href === pathname)
  let top = offset + activePageIndex * itemHeight

  return (
    <motion.div
      layout
      className="absolute left-2 h-6 w-px bg-emerald-500"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1, transition: { delay: 0.2 } }}
      exit={{ opacity: 0 }}
      style={{ top }}
    />
  )
}

function NavigationGroup({
  group,
  className,
}: {
  group: NavGroup
  className?: string
}) {
  // If this is the mobile navigation then we always render the initial
  // state, so that the state does not change during the close animation.
  // The state will still update when we re-open (re-render) the navigation.
  let isInsideMobileNavigation = useIsInsideMobileNavigation()
  let [pathname, sections] = useInitialValue(
    [usePathname(), useSectionStore((s) => s.sections)],
    isInsideMobileNavigation,
  )

  let isActiveGroup =
    group.links.findIndex((link) => link.href === pathname) !== -1

  return (
    <li className={clsx('relative mt-6', className)}>
      <motion.h2
        layout="position"
        className="text-xs font-semibold text-zinc-900 dark:text-white"
      >
        {group.title}
      </motion.h2>
      <div className="relative mt-3 pl-2">
        <AnimatePresence initial={!isInsideMobileNavigation}>
          {isActiveGroup && (
            <VisibleSectionHighlight group={group} pathname={pathname} />
          )}
        </AnimatePresence>
        <motion.div
          layout
          className="absolute inset-y-0 left-2 w-px bg-zinc-900/10 dark:bg-white/5"
        />
        <AnimatePresence initial={false}>
          {isActiveGroup && (
            <ActivePageMarker group={group} pathname={pathname} />
          )}
        </AnimatePresence>
        <ul role="list" className="border-l border-transparent">
          {group.links.map((link) => (
            <motion.li key={link.href} layout="position" className="relative">
              <NavLink href={link.href} active={link.href === pathname}>
                {link.title}
              </NavLink>
              <AnimatePresence mode="popLayout" initial={false}>
                {link.href === pathname && sections.length > 0 && (
                  <motion.ul
                    role="list"
                    initial={{ opacity: 0 }}
                    animate={{
                      opacity: 1,
                      transition: { delay: 0.1 },
                    }}
                    exit={{
                      opacity: 0,
                      transition: { duration: 0.15 },
                    }}
                  >
                    {sections.map((section) => (
                      <li key={section.id}>
                        <NavLink
                          href={`${link.href}#${section.id}`}
                          tag={section.tag}
                          isAnchorLink
                        >
                          {section.title}
                        </NavLink>
                      </li>
                    ))}
                  </motion.ul>
                )}
              </AnimatePresence>
            </motion.li>
          ))}
        </ul>
      </div>
    </li>
  )
}

export const navigation: Array<NavGroup> = [
  {
    title: 'Biological Foundations',
    links: [
      {
        title: 'Cells, Chromosomes, and Genomes',
        href: '/biological-foundations/cells-genomes-dna-chromosomes',
      },
      {
        title: 'The Central Dogma',
        href: '/biological-foundations/the-central-dogma',
      },
      { title: 'Transcription', href: '/biological-foundations/transcription' },
      { title: 'Translation', href: '/biological-foundations/translation' },
      {
        title: 'Genotype, Phenotype and Haplotype',
        href: '/biological-foundations/genotype-phenotype-haplotype',
      },
    ],
  },
  {
    title: 'Genomic Variation',
    links: [
      { title: 'Introduction', href: '/genomic-variation/index' },
      {
        title: 'Baselines for Variation',
        href: '/genomic-variation/baselines-for-variation',
      },
      {
        title: 'Single Nucleotide Variation',
        href: '/genomic-variation/single-nucleotide-variation',
      },
      {
        title: 'Insertions and Deletions',
        href: '/genomic-variation/insertions-and-deletions',
      },
      {
        title: 'Structural Variation',
        href: '/genomic-variation/structural-variation',
      },
      {
        title: 'Copy Number Variation',
        href: '/genomic-variation/copy-number-variation',
      },
      {
        title: 'Variant Equivalence',
        href: '/genomic-variation/variant-equivalence',
      },
      { title: 'Summary', href: '/genomic-variation/summary' },
    ],
  },
  {
    title: 'Next-Generation Sequencing',
    links: [
      { title: 'Introduction', href: '/next-generation-sequencing/index' },
      {
        title: 'Sample Collection',
        href: '/next-generation-sequencing/sample-collection',
      },
      {
        title: 'Next-Generation Sequencing',
        href: '/next-generation-sequencing/next-generation-sequencing',
      },
      {
        title: 'Types of Sequencing',
        href: '/next-generation-sequencing/types-of-sequencing',
      },
      {
        title: 'Read Mapping',
        href: '/next-generation-sequencing/read-mapping',
      },
    ],
  },
  {
    title: 'Genomic File Formats',
    links: [
      { title: 'Introduction', href: '/genomic-file-formats/index' },
      {
        title: 'Compression and BGZF',
        href: '/genomic-file-formats/compression-and-bgzf',
      },
      { title: 'FASTQ Files', href: '/genomic-file-formats/fastq-files' },
      { title: 'BAM Files', href: '/genomic-file-formats/bam-files' },
      { title: 'VCF Files', href: '/genomic-file-formats/vcf-files' },
    ],
  },
  {
    title: 'Engineering Ecosystem',
    links: [
      { title: 'Engineering Ecosystem', href: '/engineering-ecosystem/index' },
      { title: 'Data Sources', href: '/engineering-ecosystem/data-sources' },
      {
        title: 'Common Genomics Tools',
        href: '/engineering-ecosystem/common-genomics-tools',
      },
      {
        title: 'Worked Example',
        href: '/engineering-ecosystem/worked-example',
      },
    ],
  },
  {
    title: 'Advanced Topics',
    links: [
      { title: 'Introduction', href: '/advanced-topics/index' },
      {
        title: 'Alternative Splicing',
        href: '/advanced-topics/alternative-splicing',
      },
      {
        title: 'Cancer Development and Control',
        href: '/advanced-topics/cancer-primer',
      },
    ],
  },
]

export function Navigation(props: React.ComponentPropsWithoutRef<'nav'>) {
  return (
    <nav {...props}>
      <ul role="list">
        {navigation.map((group, groupIndex) => (
          <NavigationGroup
            key={group.title}
            group={group}
            className={groupIndex === 0 ? 'md:mt-0' : ''}
          />
        ))}
      </ul>
    </nav>
  )
}
