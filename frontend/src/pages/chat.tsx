import { type NextPage } from "next";
import Head from "next/head";

const Home: NextPage = () => {

  return (
    <>
      <Head>
        <title>Brander</title>
        <meta name="description" content="Brander app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      

      <div className="min-h-screen mx-auto px-2 pt-2 bg-gradient bg-cover flex flex-col">
        <div className="text-center basis-1/4 h-auto py-5">
          <h1 className="text-6xl font-bold mb-2">Brander</h1>
          <p className="text-light">Ver 1.0</p>
        </div>
        {/* <Toaster position="bottom-center" reverseOrder={false} /> */}
        <main className="grow flex flex-col justify-end items-center">
          <div className="w-full max-w-4xl m-3">

            <ChatMessage author={ChatMessageAuthor.System}>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quod.
            </ChatMessage>

            <ChatMessage author={ChatMessageAuthor.User}>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam, quod.
            </ChatMessage>

            <ChatInput />

          </div>
        </main>
      </div>
    </>
  );
};

export default Home;

const ChatInput: React.FC = () => {

  return (
    <div className="flex flex-row items-center justify-center gap-4 border-2 border-light rounded-lg w-full bg-base-100">

      <div className="grow">
        <textarea className="textarea w-full text-lg py-3 h-14" placeholder="Type your message here"></textarea>
      </div>
      <div>
        <button className="btn btn-ghost mr-3">Send</button>
      </div>
    </div>
  )

}

enum ChatMessageAuthor {
  System,
  User
}

type ChatMessageProps = {
  children: React.ReactNode;
  author: ChatMessageAuthor
}

const ChatMessage: React.FC<ChatMessageProps> = (props: ChatMessageProps) => {

  const wrapperClass = props.author === ChatMessageAuthor.System ? " justify-self-start float-left" : " justify-self-end float-right";

  return (
    <>
      <div className={"text-lg rounded-lg w-10/12 bg-neutral-content my-3 p-3 shadow" + wrapperClass}>
        <p>
          {props.children}
        </p>
      </div> 
    </>
  )

}