import { type NextPage } from "next";
import Head from "next/head";
import { useState } from "react";
import Textarea from "~/components/form/Textarea";
import FormLayout from "~/components/layout/FormLayout";
import PageHeader from "~/components/layout/PageHeader";

import { api } from "~/utils/api";

const Home: NextPage = () => {

  const { data: generatedPostContent, isLoading: ticketTypesLoading } = api.example.hello.useQuery({
    text: "Prompt should be here"
  });

  const [text, setText] = useState<string>('');
  const [isGenerating, setIsGenerating] = useState<boolean>(false);

  const handleGenerationRequest = (prompt: string) => {
    setText(prompt);
    setIsGenerating(true);
  };

  return (
    <>
      <Head>
        <title>Brander</title>
        <meta name="description" content="Brander app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <PageHeader />
      
      <div className="min-h-screen mx-auto px-2 pt-2 bg-gradient bg-cover flex flex-col">
        <main className="grow flex flex-col justify-center items-center">
          {!isGenerating && (
            <PostGenRequest onPostGen={handleGenerationRequest} />
          )}

          {generatedPostContent && (<div>{generatedPostContent.greeting}</div>)}
          {isGenerating && ( 
            <PostGenResult />
          )}
        </main>
      </div>
    </>
  );
};

export default Home;

type PostGenRequestParams = {
  onPostGen: (post: string) => void;
}

const PostGenRequest = (params: PostGenRequestParams) => {

  const handleOnClick = () => {
    console.log("clicked");
    params.onPostGen("post");
  };
  
  return (
    <div className="w-full max-w-4xl min-h-[60vh] m-3 text-center flex flex-col justify-between items-center">
      <h1 className="text-7xl font-bold">What kind of post would you like to generate?</h1>

      <Textarea placeholder="Example: Please, generate me a viral Facebook post that will increase interest in my page by people from Brno." name="input" onChange={(val) => {console.log(val)}} />

      <button className="btn bg-black rounded-full text-4xl h-auto p-3 bg-black max-w-2xl w-full" onClick={handleOnClick}>🚀</button>
    </div>
  )
}


const PostGenResult = () => {
  return (
    <div className="w-full max-w-4xl min-h-[60vh] m-3 text-center flex flex-col justify-between items-center">
      <div>
        <h1 className="text-7xl font-bold mb-5">Here you go, Petr! 😎</h1>
        <p className="text-4xl font-medium">Some AI joke on the post</p>
      </div>


      <div className="card w-full bg-base-100 shadow-md rounded-md">
        <div className="card-body text-[1.25rem] font-bold">
          <p>No offence, Prague guys and girls, but Brno is just... special 😜 Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet  Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet Lorem ipsum dolor sit amet </p>
        </div>
      </div>

      <button className="btn bg-black rounded-full text-4xl h-auto p-3 bg-black max-w-2xl w-full capitalize bg-[#000]"><span className="text-2xl inline-block pr-3">Regenerate</span> 🚀</button>
    </div>
  )
}