'use client'

import Link from 'next/link'
import { usePathname } from 'next/navigation'

function PencilIcon(props: React.ComponentPropsWithoutRef<'svg'>) {
  return (
    <svg viewBox="0 0 20 20" aria-hidden="true" {...props}>
      <path d="M2.695 14.763l-1.262 3.154a.5.5 0 00.632.633l3.154-1.262a1 1 0 00.421-.345l8.652-13.633a.5.5 0 00-.167-.686l-2.83-1.794a.5.5 0 00-.686.167L1.957 14.63a1 1 0 00-.262.133z" />
      <path d="M12.296 2.754l2.667 1.69 1.04-1.64-2.666-1.69-1.04 1.64z" />
    </svg>
  )
}

export function EditThisPage() {
  let pathname = usePathname()

  // Don't show edit link on homepage
  if (pathname === '/') {
    return null
  }

  // Convert pathname to GitHub file path
  const filePath = `redesign/src/app${pathname}/page.mdx`
  const githubUrl = `https://github.com/learngenomics/learngenomics.dev/edit/main/${filePath}`

  return (
    <Link
      href={githubUrl}
      target="_blank"
      rel="noopener noreferrer"
      className="group flex items-center gap-2 text-sm text-zinc-600 transition hover:text-zinc-900 dark:text-zinc-400 dark:hover:text-white"
    >
      <PencilIcon className="h-4 w-4 flex-none fill-zinc-600 transition group-hover:fill-zinc-900 dark:fill-zinc-400 dark:group-hover:fill-white" />
      <span>Edit this page</span>
    </Link>
  )
}
