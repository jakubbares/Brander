import { type NextPage } from "next";
import Head from "next/head";
import Link from "next/link";
import BaseQuestion from "~/components/questions/BaseQuestion";
import TextQuestion from "~/components/questions/TextQuestion";
import CheckboxListItem from "~/components/form/CheckboxListItem";
import ExtendedCheckboxListItem from "~/components/form/ExtendedCheckboxListItem";
import { useState } from "react";

import axios from "axios";
import FormLayout from "~/components/layout/FormLayout";
// import type FormData from "~/types/form-data";
import CheckboxColumn from "~/components/form/layout/CheckboxColumn";


const Step2: NextPage = () => {

  const checkboxColumns = {
    'gender': [
      'Men',
      'Woman',
      'Non-binary'
    ],
    'age': [
      '< 20',
      '20 - 30',
      '30 - 40',
      '40 - 50',
      '50+'
    ],
    'salary': [
      '< 500 $',
      '500 - 1000 $',
      '1000 - 1500 $',
      '1500 - 2500 $',
      '2500 - 5000 $',
      '5000+ $',
    ],
    'need': [
      'Status',
      'Price:Quality',
      'Lifestyle',
    ],
    'motivation': [
      'Functional',
      'Emotional',
      'Social',
      'Personal',
      'Financial',
    ]
  }

  type FormData = {
    age: string[];
    gender: string[];
    salary: string[];
    need: string[];
    motivation: string[];
  }


  const [formData, setFormData] = useState<FormData>({
    age: [],
    gender: [],
    salary: [],
    need: [],
    motivation: [],
  });

  const handleCheckboxItemChecked = (name: string, isChecked: boolean, value: string) => {
    const updatedFormData: FormData = formData;

    if (isChecked) {

      // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-call
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
    <>
      <Head>
        <title>Brander</title>
      </Head>
      <FormLayout currentPage={2} sectionTitle="Target audience" title="Who is your primary customer?" subtitle="">

        <BaseQuestion>
          <div className="flex flex-row w-full">
              <CheckboxColumn title="Gender">
                {checkboxColumns.gender.map((item, index) => {
                  return <CheckboxListItem key={index} name="s2_gender" label={item} id={`gender-${index}`} isChecked={false} onItemChecked={handleCheckboxItemChecked} />
                })}
              </CheckboxColumn>
              <CheckboxColumn title="Age">
                {checkboxColumns.age.map((item, index) => {
                  return <CheckboxListItem key={index} name="s2_age" label={item} id={`age-${index}`} isChecked={false} onItemChecked={handleCheckboxItemChecked} />
                })}
              </CheckboxColumn>
              <CheckboxColumn title="Salary">
                {checkboxColumns.salary.map((item, index) => {
                  return <CheckboxListItem key={index} name="s2_salary" label={item} id={`salary-${index}`} isChecked={false} onItemChecked={handleCheckboxItemChecked} />
                })}
              </CheckboxColumn>
              <CheckboxColumn title="Need">
                {checkboxColumns.need.map((item, index) => {
                  return <CheckboxListItem key={index} name="s2_need" label={item} id={`need-${index}`} isChecked={false} onItemChecked={handleCheckboxItemChecked} />
                })}
              </CheckboxColumn>
              <CheckboxColumn title="Motivation">
                {checkboxColumns.salary.map((item, index) => {
                  return <CheckboxListItem key={index} name="s2_motivation" label={item} id={`motivation-${index}`} isChecked={false} onItemChecked={handleCheckboxItemChecked} />
                })}
              </CheckboxColumn>
          </div>

        </BaseQuestion>
        
      </FormLayout>
    </>
  );
};

export default Step2;




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