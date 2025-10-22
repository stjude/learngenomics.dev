import { Button } from '@/components/Button'
import { Heading } from '@/components/Heading'

const learningPaths = [
  {
    href: '/biological-foundations/cells-genomes-dna-chromosomes',
    name: 'Biological Foundations',
    description: 'Learn about cells, DNA, chromosomes, and the central dogma of molecular biology.',
  },
  {
    href: '/genomic-variation/index',
    name: 'Genomic Variation',
    description: 'Understand single nucleotide variants, indels, structural variations, and copy number changes.',
  },
  {
    href: '/next-generation-sequencing/index',
    name: 'Next-Generation Sequencing',
    description: 'Explore sequencing technologies, sample collection, read mapping, and types of sequencing.',
  },
  {
    href: '/genomic-file-formats/index',
    name: 'Genomic File Formats',
    description: 'Master essential file formats including FASTQ, BAM, VCF, and compression techniques.',
  },
  {
    href: '/engineering-ecosystem/index',
    name: 'Engineering Ecosystem',
    description: 'Discover data sources, common genomics tools, and end-to-end workflow examples.',
  },
  {
    href: '/advanced-topics/index',
    name: 'Advanced Topics',
    description: 'Deep dive into alternative splicing, cancer genomics, and complex biological phenomena.',
  },
]

export function LearningPaths() {
  return (
    <div className="my-16 xl:max-w-none">
      <Heading level={2} id="learning-paths">
        Learning Paths
      </Heading>
      <div className="not-prose mt-4 grid grid-cols-1 gap-8 border-t border-zinc-900/5 pt-10 sm:grid-cols-2 xl:grid-cols-3 dark:border-white/5">
        {learningPaths.map((path) => (
          <div key={path.href}>
            <h3 className="text-sm font-semibold text-zinc-900 dark:text-white">
              {path.name}
            </h3>
            <p className="mt-1 text-sm text-zinc-600 dark:text-zinc-400">
              {path.description}
            </p>
            <p className="mt-4">
              <Button href={path.href} variant="text" arrow="right">
                Read more
              </Button>
            </p>
          </div>
        ))}
      </div>
    </div>
  )
}
