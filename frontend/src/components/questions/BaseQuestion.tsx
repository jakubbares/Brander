import React from "react";

export type BaseQuestionProps = {
    children: React.ReactNode;
};

const BaseQuestion: React.FC<BaseQuestionProps> = (props) => {
    return (
        <div className="form-control w-full max-w-4xl flex items-center">
            {props.children}

            {/* <button className="btn bg-black">Continue</button> */}
        </div>
    );
}

export default BaseQuestion;