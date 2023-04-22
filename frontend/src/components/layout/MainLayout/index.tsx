// import { signIn, signOut, useSession } from "next-auth/react";
// import Link from "next/link";

type MainLayoutProps = {
  children: React.ReactNode;
};

export default function MainLayout({ children }: MainLayoutProps) {
  // const { data: sessionData } = useSession();

  return (
    <>
      <div className="fixed w-full top-0 left-0">
        <div className="flex flex-row justify-between container mx-auto py-5 px-2">
          <div>
            <div className="text-4xl font-bold mb-2">Brander</div>
          </div>
          <div className="flex items-center gap-5">
            <h1 className="text-4xl font-bold mb-2">Petr Pavel</h1>
            {/* <Image src="/img/profile_img.png" alt="Profile image" width={40} height={40} /> */}
            <img src="/img/profile_img.png" alt="Profile image" className="rounded-full h-16 w-16 mt-[-5px]" />
          </div>
        </div>
      </div>
      <div className="min-h-screen mx-auto px-2 pt-2 bg-gradient bg-cover flex flex-col">
        
        {/* <Toaster position="bottom-center" reverseOrder={false} /> */}
        <main className="grow flex flex-col items-center justify-center">{children}</main>
      </div>
    </>
  );
}
