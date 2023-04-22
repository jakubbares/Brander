import { signIn, signOut, useSession } from "next-auth/react";
import Link from "next/link";

type MainLayoutProps = {
  children: React.ReactNode;
};

export default function MainLayout({ children }: MainLayoutProps) {
  const { data: sessionData } = useSession();

  return (
    <>
      <div className="min-h-screen mx-auto px-2 pt-2 bg-gradient bg-cover flex flex-col">
        <div className="text-center basis-1/4 h-auto py-5">
          <h1 className="text-6xl font-bold mb-2">Brander</h1>
          <p className="text-light">Ver 1.0</p>
        </div>
        {/* <Toaster position="bottom-center" reverseOrder={false} /> */}
        <main className="grow flex flex-col items-center justify-center">{children}</main>
      </div>
    </>
  );
}
