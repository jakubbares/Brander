import React from "react";

export type BaseQuestionProps = {
    children: React.ReactNode;
    questionNumber: number;
    label: string;
};

const BaseQuestion: React.FC<BaseQuestionProps> = (props) => {
    return (
        <div className="form-control w-full max-w-4xl flex items-center">
            {/* <div className="font-medium border border-black rounded-full text-xl w-10 h-10 text-center pt-1">{props.questionNumber}</div> */}
            <label className="text-center text-3xl font-semibold mt-9 mb-9 max-w-3xl">{props.label}</label>
            {props.children}

            <button className="btn bg-black">Continue</button>
        </div>
    );
}

export default BaseQuestion;