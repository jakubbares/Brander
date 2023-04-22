import { useState } from "react";


interface CheckboxListItemProps {
    children: React.ReactNode;
    id: string;
    label: string;
    name: string;
    isChecked: boolean;
    onItemChecked: (name: string, isChecked: boolean, value: string) => void;
}

  
  const CheckboxListItem: React.FC<CheckboxListItemProps> = (props) => {
    const [isChecked, setIsChecked] = useState<boolean>(props.isChecked);
  
    const handleItemChecked = (name: string, isChecked: boolean, value: string) => {
        setIsChecked(isChecked);
        props.onItemChecked(name, isChecked, value);
    };
  
    return (
        <div className="form-control my-5">
            <label 
                className="cursor-pointer label justify-start items-start" 
                htmlFor={props.id}
            >
                <div>
                    <input type="checkbox" className="checkbox checkbox-lg"
                        id={props.id}
                        name={props.name}
                        checked={isChecked}
                        onChange={(e) => handleItemChecked(props.name, e.target.checked, e.target.value)}
                        value={props.label}
                        />

                </div>
                <div className="pl-3 pt-[2px]">
                    <div className="font-bold text-2xl mb-2">{props.label}</div>
                    <p className="text-light">{props.children}</p>
                </div>
            </label>
        </div>
    );
  };
  
  export default CheckboxListItem;