import clsx from 'clsx'
import Link from 'next/link'

import { EditThisPage } from '@/components/EditThisPage'
import { Feedback } from '@/components/Feedback'
import { Heading } from '@/components/Heading'
import { Prose } from '@/components/Prose'

export const a = Link
export { Button } from '@/components/Button'
export { Code as code, CodeGroup, Pre as pre } from '@/components/Code'

export function wrapper({ children }: { children: React.ReactNode }) {
  return (
    <article className="flex h-full flex-col pt-16 pb-10">
      <Prose className="flex-auto">{children}</Prose>
      <footer className="mx-auto mt-16 w-full max-w-2xl lg:max-w-5xl">
        <div className="space-y-4">
          <EditThisPage />
          <Feedback />
        </div>
      </footer>
    </article>
  )
}

export const h2 = function H2(
  props: Omit<React.ComponentPropsWithoutRef<typeof Heading>, 'level'>,
) {
  return <Heading level={2} {...props} />
}

function InfoIcon(props: React.ComponentPropsWithoutRef<'svg'>) {
  return (
    <svg viewBox="0 0 16 16" aria-hidden="true" {...props}>
      <circle cx="8" cy="8" r="8" strokeWidth="0" />
      <path
        fill="none"
        strokeLinecap="round"
        strokeLinejoin="round"
        strokeWidth="1.5"
        d="M6.75 7.75h1.5v3.5"
      />
      <circle cx="8" cy="4" r=".5" fill="none" />
    </svg>
  )
}

const noteStyles = {
  info: {
    container:
      'border-brand-info-500/20 bg-brand-info-50/50 text-brand-info-900 dark:border-brand-info-500/30 dark:bg-brand-info-500/5 dark:text-brand-info-200 dark:[--tw-prose-links-hover:var(--color-brand-info-300)] dark:[--tw-prose-links:var(--color-white)]',
    icon: 'fill-brand-info-500 stroke-white dark:fill-brand-info-200/20 dark:stroke-brand-info-200',
  },
  tip: {
    container:
      'border-brand-success-500/20 bg-brand-success-50/50 text-brand-success-900 dark:border-brand-success-500/30 dark:bg-brand-success-500/5 dark:text-brand-success-200 dark:[--tw-prose-links-hover:var(--color-brand-success-300)] dark:[--tw-prose-links:var(--color-white)]',
    icon: 'fill-brand-success-500 stroke-white dark:fill-brand-success-200/20 dark:stroke-brand-success-200',
  },
  caution: {
    container:
      'border-brand-warning-500/20 bg-brand-warning-50/50 text-brand-warning-900 dark:border-brand-warning-500/30 dark:bg-brand-warning-500/5 dark:text-brand-warning-200 dark:[--tw-prose-links-hover:var(--color-brand-warning-300)] dark:[--tw-prose-links:var(--color-white)]',
    icon: 'fill-brand-warning-500 stroke-white dark:fill-brand-warning-200/20 dark:stroke-brand-warning-200',
  },
}

export function Note({
  children,
  type = 'info',
  header,
}: {
  children: React.ReactNode
  type?: 'info' | 'tip' | 'caution'
  header?: string
}) {
  return (
    <div
      className={clsx(
        'my-6 flex gap-2.5 rounded-2xl border p-4 text-sm/6',
        noteStyles[type].container,
      )}
    >
      <InfoIcon
        className={clsx('mt-1 h-4 w-4 flex-none', noteStyles[type].icon)}
      />
      <div>
        <b className="font-semibold">
          {header || type.charAt(0).toUpperCase() + type.slice(1)}
        </b>
        <div className="[&>:first-child]:mt-0 [&>:last-child]:mb-0">
          {children}
        </div>
      </div>
    </div>
  )
}

export function Row({ children }: { children: React.ReactNode }) {
  return (
    <div className="grid grid-cols-1 items-start gap-x-16 gap-y-10 xl:max-w-none xl:grid-cols-2">
      {children}
    </div>
  )
}

export function Col({
  children,
  sticky = false,
}: {
  children: React.ReactNode
  sticky?: boolean
}) {
  return (
    <div
      className={clsx(
        '[&>:first-child]:mt-0 [&>:last-child]:mb-0',
        sticky && 'xl:sticky xl:top-24',
      )}
    >
      {children}
    </div>
  )
}

export function Properties({ children }: { children: React.ReactNode }) {
  return (
    <div className="my-6">
      <ul
        role="list"
        className="m-0 max-w-[calc(var(--container-lg)-(--spacing(8)))] list-none divide-y divide-zinc-900/5 p-0 dark:divide-white/5"
      >
        {children}
      </ul>
    </div>
  )
}

export function Property({
  name,
  children,
  type,
}: {
  name: string
  children: React.ReactNode
  type?: string
}) {
  return (
    <li className="m-0 px-0 py-4 first:pt-0 last:pb-0">
      <dl className="m-0 flex flex-wrap items-center gap-x-3 gap-y-2">
        <dt className="sr-only">Name</dt>
        <dd>
          <code>{name}</code>
        </dd>
        {type && (
          <>
            <dt className="sr-only">Type</dt>
            <dd className="font-mono text-xs text-zinc-400 dark:text-zinc-500">
              {type}
            </dd>
          </>
        )}
        <dt className="sr-only">Description</dt>
        <dd className="w-full flex-none [&>:first-child]:mt-0 [&>:last-child]:mb-0">
          {children}
        </dd>
      </dl>
    </li>
  )
}
