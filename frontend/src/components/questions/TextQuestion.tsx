import React, { Children } from "react";
import { type BaseQuestionProps } from "./BaseQuestion";
import BaseQuestion from "./BaseQuestion";
import Textarea from "../form/Textarea";


interface TextQuestionProps extends BaseQuestionProps {
    footnote: string;
}

const TextQuestion: React.FC<TextQuestionProps> = (props) => {
    return (
        <BaseQuestion questionNumber={1} label={props.label}>
            <Textarea footnote={props.footnote} name="tst" onChange={(value) => {console.log(value)}} maxWordsCount={2} />
            {/* <input type="text" placeholder="Type here" className="input input-bordered w-full text-lg h-16" />
            <label className="label w-full">
                <span className="text-sm"></span>
                <span className="text-sm text-light">{props.footnote}</span>
            </label> */}
        </BaseQuestion>
    );
}

export default TextQuestion;
