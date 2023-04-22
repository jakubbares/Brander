import { type AppType } from "next/app";
import { type Session } from "next-auth";
import { SessionProvider } from "next-auth/react";

import { api } from "~/utils/api";

import "~/styles/globals.css";
import MainLayout from "~/components/layout/MainLayout";

import type { ReactElement, ReactNode } from 'react'
import type { NextPage } from 'next'
import type { AppProps } from 'next/app'

export type NextPageWithLayout<P = {}, IP = P> = NextPage<P, IP> & {
  getLayout?: (page: ReactElement) => ReactNode
}

type AppPropsWithLayout = AppProps & {
  Component: NextPageWithLayout
}

// const MyApp: AppType<{ session: Session | null }> = ({ Component, pageProps: { session, ...pageProps }, }: AppPropsWithLayout) => {
const MyApp: AppType = ({ Component, pageProps, }: AppPropsWithLayout) => {
  // Use the layout defined at the page level, if available
  const getLayout = Component.getLayout ?? ((page) => page)

  return getLayout(<Component {...pageProps} />)
}
// const MyApp: AppType<{ session: Session | null }> = ({
//   Component,
//   pageProps: { session, ...pageProps },
// }) => {

//   // Use the layout defined at the page level, if available
//   // eslint-disable-next-line @typescript-eslint/no-unsafe-assignment
//   const getLayout = Component.getLayout || ((page: any) => page);

//   return getLayout(<Component {...pageProps} />)
//   return (
//     <SessionProvider session={session}>
//       <MainLayout>
//         <Component {...pageProps} />
//       </MainLayout>
//     </SessionProvider>
//   );
// };

export default api.withTRPC(MyApp);
