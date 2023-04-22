import { useState } from 'react';

interface TextareaProps {
    // label: string;
    name: string;
    onChange: (value: string) => void;
    maxWordsCount?: number;
    footnote?: string;
}

const Textarea: React.FC<TextareaProps> = (props) => {
    const [text, setText] = useState<string>('');
    const [wordCount, setWordCount] = useState<number>(0);
    const [footnoteClass, setFootnoteClass] = useState<string>('text-sm text-light');
    const [hasError, setHasError] = useState<boolean>(false);

    const countWords = (text: string): number => {
        const words = text.trim().split(/\s+/);
        return words.length;
    };

    // const handleOnChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    const handleOnChange = (newText: string) => {
        const nWords = countWords(newText);

        setText(newText);
        setWordCount(nWords);

        const baseFootnoteClass = 'relative text-sm text-light';

        if (props.maxWordsCount && nWords > props.maxWordsCount) {
            setFootnoteClass(baseFootnoteClass + ' text-error font-bold');
            setHasError(true);
        } else {
            setFootnoteClass(baseFootnoteClass);
            setHasError(false);
        }

        props.onChange(newText);
    };

    return (
        <>
            <textarea
                placeholder="Type here"
                name={props.name}
                className="textarea textarea-bordered w-full text-lg h-80 py-3"
                onChange={(e) => handleOnChange(e.target.value)}></textarea>
            {props.maxWordsCount && (
                <label className="label w-full">
                    <span className="text-sm"></span>
                    {props.maxWordsCount && (
                        <span className={footnoteClass}>

                            {hasError && (
                                <span className="relative inline-flex h-3 w-3 mr-2">
                                    <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-error opacity-75"></span>
                                    <span className="relative inline-flex rounded-full h-3 w-3 bg-error"></span>
                                </span>  
                            )}
                            
                            <span>
                                {wordCount} / {props.maxWordsCount} words
                            </span>
                        </span>
                    )}
                </label>
            )}
        </>
    );
};

export default Textarea;