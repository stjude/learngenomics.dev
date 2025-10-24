import clsx from 'clsx'

const variantStyles = {
  small: '',
  medium: 'rounded-lg px-1.5 ring-1 ring-inset',
}

const colorStyles = {
  emerald: {
    small: 'text-brand-success-500 dark:text-brand-success-400',
    medium:
      'ring-brand-success-300 dark:ring-brand-success-400/30 bg-brand-success-400/10 text-brand-success-500 dark:text-brand-success-400',
  },
  sky: {
    small: 'text-brand-info-500',
    medium:
      'ring-brand-info-300 bg-brand-info-400/10 text-brand-info-500 dark:ring-brand-info-400/30 dark:bg-brand-info-400/10 dark:text-brand-info-400',
  },
  amber: {
    small: 'text-brand-warning-500',
    medium:
      'ring-brand-warning-300 bg-brand-warning-400/10 text-brand-warning-500 dark:ring-brand-warning-400/30 dark:bg-brand-warning-400/10 dark:text-brand-warning-400',
  },
  rose: {
    small: 'text-brand-error-500 dark:text-brand-error-500',
    medium:
      'ring-brand-error-200 bg-brand-error-50 text-brand-error-500 dark:ring-brand-error-500/20 dark:bg-brand-error-400/10 dark:text-brand-error-400',
  },
  zinc: {
    small: 'text-zinc-400 dark:text-zinc-500',
    medium:
      'ring-zinc-200 bg-zinc-50 text-zinc-500 dark:ring-zinc-500/20 dark:bg-zinc-400/10 dark:text-zinc-400',
  },
}

const valueColorMap = {
  GET: 'emerald',
  POST: 'sky',
  PUT: 'amber',
  DELETE: 'rose',
} as Record<string, keyof typeof colorStyles>

export function Tag({
  children,
  variant = 'medium',
  color = valueColorMap[children] ?? 'emerald',
}: {
  children: keyof typeof valueColorMap & (string | {})
  variant?: keyof typeof variantStyles
  color?: keyof typeof colorStyles
}) {
  return (
    <span
      className={clsx(
        'font-mono text-[0.625rem]/6 font-semibold',
        variantStyles[variant],
        colorStyles[color][variant],
      )}
    >
      {children}
    </span>
  )
}
