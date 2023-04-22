import { type NextPage } from "next";
import Head from "next/head";
import BaseQuestion from "~/components/questions/BaseQuestion";
import FormLayout from "~/components/layout/FormLayout";
import Textarea from "~/components/form/Textarea";
import { useState } from "react";
import { saveToStorage, getFromStorage } from "~/utils/localstorage";

type FormData = {
  clientProblem: string;
}

const Step1: NextPage = () => {

  console.log(getFromStorage('s1'));
  // console.log( (JSON.parse(getFromStorage('s1') || "no local storage")) );

  // eslint-disable-next-line @typescript-eslint/no-unsafe-argument
  const [formData, setFormData] = useState<FormData>( JSON.parse('{}') );

  const handleOnChange = (value: string) => {
    // update value in formData
    const updatedFormData: FormData = formData;
    updatedFormData.clientProblem = value;
    
    // save formData to localStorage
    saveToStorage('s1', JSON.stringify(updatedFormData));

    // update formData state
    setFormData(updatedFormData);
  }


  return (
    <>
      <Head>
        <title>Brander</title>
      </Head>
      <FormLayout currentPage={1} sectionTitle="Insight" title="Can you please describe the primary problem or challenge your customers are&nbsp;currently facing?" subtitle="">

        <BaseQuestion>
            <Textarea name="s1-client-problem" onChange={handleOnChange} />
        </BaseQuestion>
        
      </FormLayout>
    </>
  );
};

export default Step1;


// const CheckboxColsPageContent: React.FC = () => {

//   const [formData, setFormData] = useState<FormData>({
//     age: []
//   });

//   const handleCheckboxItemChecked = (name: string, isChecked: boolean, value: string) => {
//     const updatedFormData: FormData = formData;

//     if (isChecked) {

//       updatedFormData[name]?.push(value);
//       setFormData(updatedFormData);

//     } else {

//       const updatedCheckboxList = updatedFormData[name]?.filter((item: string) => item !== value);

//       if (updatedCheckboxList) {
//         updatedFormData[name] = updatedCheckboxList;
//       }

//       setFormData(updatedFormData);
//     }
//   }


//   return (

//       <BaseQuestion>
//         <div className="flex flex-row w-full">
//             <CheckboxColumn title="Age">
//               <CheckboxListItem name="age" label="18-24" id="age-1" isChecked={false} onItemChecked={handleCheckboxItemChecked} />
//               <CheckboxListItem name="age" label="25-30" id="age-2" isChecked={false} onItemChecked={handleCheckboxItemChecked} />
//               <CheckboxListItem name="age" label="31-35" id="age-3" isChecked={false} onItemChecked={handleCheckboxItemChecked} />
//             </CheckboxColumn>
//             <CheckboxColumn title="Age">
//               <CheckboxListItem name="age2" label="18-24" id="age2-1" isChecked={false} onItemChecked={handleCheckboxItemChecked} />
//             </CheckboxColumn>
//             <CheckboxColumn title="Location">
//               <input type="checkbox" className="checkbox" />
//             </CheckboxColumn>
//             <CheckboxColumn title="Need">
//               <input type="checkbox" className="checkbox" />
//             </CheckboxColumn>
//             <CheckboxColumn title="Motivation">
//               <input type="checkbox" className="checkbox" />
//             </CheckboxColumn>
//         </div>
//       </BaseQuestion>
//   )
// }

// const ExtendedCheckboxesPageContent: React.FC = () => {

//   return (
//     <BaseQuestion>

//       <div className="flex">

//         <div className="flex-grow">
//           <ExtendedCheckboxListItem name="age" label="18-24" id="age-1" isChecked={false} onItemChecked={() => {}}>
//             Brands that are reliable, efficient, and effective. They are often associated with qualities such as intelligence, professionalism, and expertise.
//           </ExtendedCheckboxListItem>
//           <ExtendedCheckboxListItem name="age" label="18-24" id="age-1" isChecked={false} onItemChecked={() => {}}>
//             Brands that are reliable, efficient, and effective. They are often associated with qualities such as intelligence, professionalism, and expertise.
//           </ExtendedCheckboxListItem>
//           <ExtendedCheckboxListItem name="age" label="18-24" id="age-1" isChecked={false} onItemChecked={() => {}}>
//             Brands that are reliable, efficient, and effective. They are often associated with qualities such as intelligence, professionalism, and expertise.
//           </ExtendedCheckboxListItem>
//         </div>

//         <div className="flex-grow">
//           <ExtendedCheckboxListItem name="age" label="25-30" id="age-2" isChecked={false} onItemChecked={() => {}}>
//             Brands that are reliable, efficient, and effective. They are often associated with qualities such as intelligence, professionalism, and expertise.
//           </ExtendedCheckboxListItem>
//           <ExtendedCheckboxListItem name="age" label="25-30" id="age-2" isChecked={false} onItemChecked={() => {}}>
//             Brands that are reliable, efficient, and effective. They are often associated with qualities such as intelligence, professionalism, and expertise.
//           </ExtendedCheckboxListItem>
//           <ExtendedCheckboxListItem name="age" label="25-30" id="age-2" isChecked={false} onItemChecked={() => {}}>
//             Brands that are reliable, efficient, and effective. They are often associated with qualities such as intelligence, professionalism, and expertise.
//           </ExtendedCheckboxListItem>
//         </div>
//       </div>

//     </BaseQuestion>
//   )
// }