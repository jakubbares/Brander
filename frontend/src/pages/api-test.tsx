import { type NextPage } from "next";
import Head from "next/head";

import axios from "axios";
import FormLayout from "~/components/layout/FormLayout";


const ApiTest: NextPage = () => {

  const testAPI = async () => {

    const res = await axios({
      method: 'POST',
      url: 'http://localhost:5000/brander/content_strategyzzzzzz',
      data: {
        human_template: 'John Doe',
      }
    });

    console.log(res, 'res');

  }

  const handleOnClick = () => {
    testAPI().then((res) => { console.log(res) }).catch((err) => { console.error(err) });
  }

  return (
    <>
      <Head>
        <title>Brander - API test</title>
      </Head>
      <FormLayout>
        <button className="btn btn-primary" onClick={handleOnClick}>Test API</button>
      </FormLayout>
    </>
  );
};

export default ApiTest;
