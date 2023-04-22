import { type NextPage } from "next";
import Head from "next/head";
import Link from "next/link";
import BaseQuestion from "~/components/questions/BaseQuestion";
import TextQuestion from "~/components/questions/TextQuestion";
import CheckboxListItem from "~/components/form/CheckboxListItem";
import ExtendedCheckboxListItem from "~/components/form/ExtendedCheckboxListItem";
import { useState } from "react";

interface FormData {
  [age: string]: string[];
}

const Home: NextPage = () => {

  return (
    <>
      <Head>
        <title>Brander</title>
        <meta name="description" content="Brander app" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      {/* <CheckboxColsPageContent /> */}
      <TextPageContent />
      {/* <ExtendedCheckboxesPageContent /> */}

      {/* <main className="flex min-h-screen flex-col items-center justify-center">
        <div className="container flex flex-col items-center justify-center gap-12 px-4 py-16 ">
            <TextQuestion />
        </div>
      </main> */}
    </>
  );
};

export default Home;


type CheckboxColumnProps = {
  children: React.ReactNode;
  title: string;
}

const CheckboxColumn: React.FC<CheckboxColumnProps> = (props) => {
  return (
    <>
      <div className="grow">
        <div className="text-2xl font-semibold">
          {props.title}
        </div>
        <div>
          {props.children}
        </div>
      </div>
    </>
  )
}

const TextPageContent: React.FC = () => {

  return (
    <>
      <TextQuestion questionNumber={1} label="Can you please describe the primary problem or challenge your customers are currently facing?" footnote="Max. 100 words">.</TextQuestion>
    </>
  );

}

const CheckboxColsPageContent: React.FC = () => {

  const [formData, setFormData] = useState<FormData>({
    age: []
  });

  const handleCheckboxItemChecked = (name: string, isChecked: boolean, value: string) => {
    const updatedFormData: FormData = formData;

    if (isChecked) {

      updatedFormData[name]?.push(value);
      setFormData(updatedFormData);

    } else {

      const updatedCheckboxList = updatedFormData[name]?.filter((item: string) => item !== value);

      if (updatedCheckboxList) {
        updatedFormData[name] = updatedCheckboxList;
      }

      setFormData(updatedFormData);
    }
  }


  return (

      <BaseQuestion questionNumber={2} label="Can you please describe the primary problem or challenge your customers are currently facing?">
        <div className="flex flex-row w-full">
            <CheckboxColumn title="Age">
              <CheckboxListItem name="age" label="18-24" id="age-1" isChecked={false} onItemChecked={handleCheckboxItemChecked} />
              <CheckboxListItem name="age" label="25-30" id="age-2" isChecked={false} onItemChecked={handleCheckboxItemChecked} />
              <CheckboxListItem name="age" label="31-35" id="age-3" isChecked={false} onItemChecked={handleCheckboxItemChecked} />
            </CheckboxColumn>
            <CheckboxColumn title="Age">
              <CheckboxListItem name="age2" label="18-24" id="age2-1" isChecked={false} onItemChecked={handleCheckboxItemChecked} />
            </CheckboxColumn>
            <CheckboxColumn title="Location">
              <input type="checkbox" className="checkbox" />
            </CheckboxColumn>
            <CheckboxColumn title="Need">
              <input type="checkbox" className="checkbox" />
            </CheckboxColumn>
            <CheckboxColumn title="Motivation">
              <input type="checkbox" className="checkbox" />
            </CheckboxColumn>
        </div>
      </BaseQuestion>
  )
}

const ExtendedCheckboxesPageContent: React.FC = () => {

  return (
    <BaseQuestion questionNumber={3} label="Can you please describe the primary problem or challenge your customers are currently facing?">

      <div className="flex">

        <div className="flex-grow">
          <ExtendedCheckboxListItem name="age" label="18-24" id="age-1" isChecked={false} onItemChecked={() => {}}>
            Brands that are reliable, efficient, and effective. They are often associated with qualities such as intelligence, professionalism, and expertise.
          </ExtendedCheckboxListItem>
          <ExtendedCheckboxListItem name="age" label="18-24" id="age-1" isChecked={false} onItemChecked={() => {}}>
            Brands that are reliable, efficient, and effective. They are often associated with qualities such as intelligence, professionalism, and expertise.
          </ExtendedCheckboxListItem>
          <ExtendedCheckboxListItem name="age" label="18-24" id="age-1" isChecked={false} onItemChecked={() => {}}>
            Brands that are reliable, efficient, and effective. They are often associated with qualities such as intelligence, professionalism, and expertise.
          </ExtendedCheckboxListItem>
        </div>

        <div className="flex-grow">
          <ExtendedCheckboxListItem name="age" label="25-30" id="age-2" isChecked={false} onItemChecked={() => {}}>
            Brands that are reliable, efficient, and effective. They are often associated with qualities such as intelligence, professionalism, and expertise.
          </ExtendedCheckboxListItem>
          <ExtendedCheckboxListItem name="age" label="25-30" id="age-2" isChecked={false} onItemChecked={() => {}}>
            Brands that are reliable, efficient, and effective. They are often associated with qualities such as intelligence, professionalism, and expertise.
          </ExtendedCheckboxListItem>
          <ExtendedCheckboxListItem name="age" label="25-30" id="age-2" isChecked={false} onItemChecked={() => {}}>
            Brands that are reliable, efficient, and effective. They are often associated with qualities such as intelligence, professionalism, and expertise.
          </ExtendedCheckboxListItem>
        </div>
      </div>

    </BaseQuestion>
  )
}