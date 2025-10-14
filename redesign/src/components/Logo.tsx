export function Logo(props: React.ComponentPropsWithoutRef<'p'>) {
  return (
    <p {...props} className={`${props.className} text-xl font-extrabold`} aria-hidden="true">learngenomics.dev</p>
  )
}
