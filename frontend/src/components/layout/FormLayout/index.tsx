// import { signIn, signOut, useSession } from "next-auth/react";
// import Link from "next/link";

import Link from "next/link";
import PageHeader from "../PageHeader";

type FormLayoutProps = {
  children: React.ReactNode;
  numberOfPages?: number;
  currentPage: number;
  sectionTitle?: string;
  title?: string;
  subtitle?: string;
};

export default function FormLayout({ children, numberOfPages = 12, currentPage, sectionTitle, title, subtitle }: FormLayoutProps) {
  // const { data: sessionData } = useSession();

  return (
    <>
      <PageHeader />
      <div className="min-h-screen mx-auto px-2 pt-2 bg-gradient bg-cover flex flex-col">
        {sectionTitle && (
          <small className="text-center text-xl font-medium uppercase tracking-wider mt-16">
            {sectionTitle}
          </small>
        )}

        <div className="mx-auto text-center max-w-3xl min-h-[265px] flex flex-col justify-center">
          {title && (
            <h2 className="text-4xl font-semibold mb-3 whitespace-pre-line">
              {title}
            </h2>
          )}

          {subtitle && (
            <div className="font-medium whitespace-pre-line">{subtitle}</div>
          )}
        </div>

        {/* <Toaster position="bottom-center" reverseOrder={false} /> */}
        {/* <main className="grow flex flex-col items-center justify-center">{children}</main> */}
        <main className="grow flex flex-col items-center">{children}</main>

        <div className="flex justify-center gap-4 my-5">
          {Array.from(Array(numberOfPages).keys()).map((page) => {
            return <PaginationButton key={`pagination-btn-${page}`} page={page + 1} isActive={(page + 1) === currentPage} />
          })}
        </div>

      </div>
    </>
  );
}


type PaginationButtonProps = {
  page: number;
  onClick?: () => void;
  isActive: boolean;
}

const PaginationButton = (props: PaginationButtonProps) => {

  const activeClass = props.isActive ? " border-base-content" : " border-lighter text-lighter hover:border-base-content";

  return (
    <Link href={"/brand-strategy/" + props.page.toString()} onClick={props.onClick} className={"inline-flex text-center justify-center items-center bg-transparent font-medium border rounded-full text-base w-10 h-10 hover:text-neutral-content hover:bg-base-content transition duration-150 ease-out hover:ease-in" + activeClass}>
      {props.page}
    </Link>
  )
}