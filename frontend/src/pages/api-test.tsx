import { type NextPage } from "next";
import Head from "next/head";

import axios from "axios";
import MainLayout from "~/components/layout/MainLayout";


const ApiTest: NextPage = () => {

  const testAPI = async () => {

    const res = await axios({
      method: 'POST',
      url: 'http://localhost:5000/brander/content_strategy',
      // params: {
      //   input_parameters_json: "{}",
      //   human_template: 'John Doe',
      // }
      data: {
        input_parameters_json: "{}",
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
      <MainLayout>
        <button className="btn btn-primary" onClick={handleOnClick}>Test API</button>
      </MainLayout>
    </>
  );
};

export default ApiTest;
