import React, { Children } from "react";
import { type BaseQuestionProps } from "./BaseQuestion";
import BaseQuestion from "./BaseQuestion";
import Textarea from "../form/Textarea";


interface TextQuestionProps extends BaseQuestionProps {
    inputName: string;
    maxWordCount?: number;
    onChange: (value: string) => void;
}

const TextQuestion: React.FC<TextQuestionProps> = (props) => {
    return (
        <BaseQuestion label={props.label}>
            <Textarea name={props.inputName} onChange={props.onChange} maxWordsCount={props.maxWordCount} />
            {/* <input type="text" placeholder="Type here" className="input input-bordered w-full text-lg h-16" />
            <label className="label w-full">
                <span className="text-sm"></span>
                <span className="text-sm text-light">{props.footnote}</span>
            </label> */}
        </BaseQuestion>
    );
}

export default TextQuestion;
