import { type NextPage } from "next";
import Head from "next/head";
import BaseQuestion from "~/components/questions/BaseQuestion";


import FormLayout from "~/components/layout/FormLayout";

import Textarea from "~/components/form/Textarea";


const Step3: NextPage = () => {


  return (
    <>
      <Head>
        <title>Brander</title>
      </Head>
      <FormLayout currentPage={3} sectionTitle="Vision" title={"What is the purpose of the company?\nWhy do you exist?"} subtitle="">

        <BaseQuestion>
            <Textarea name="s3-company-purpose" onChange={(e) => {console.log(e)}} maxWordsCount={100} placeholder="Example: Ryanair exists to offer low fares that generate increased passenger traffic while maintaining a continuous focus on cost containment and efficiency." />
        </BaseQuestion>
        
      </FormLayout>
    </>
  );
};

export default Step3;
