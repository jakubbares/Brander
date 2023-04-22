import { useState } from "react";


interface CheckboxListItemProps {
    id: string;
    label: string;
    name: string;
    isChecked: boolean;
    onItemChecked: (name: string, isChecked: boolean, value: string) => void;
}

// interface CheckboxListProps {
//     // name: string;
//     // items: CheckboxListItem[];
//     onItemChecked: (id: string, isChecked: boolean) => void;
// }
  
  const CheckboxListItem: React.FC<CheckboxListItemProps> = (props) => {
    // const [listItems, setListItems] = useState<CheckboxListItem[]>(items);
    const [isChecked, setIsChecked] = useState<boolean>(props.isChecked);
  
    const handleItemChecked = (name: string, isChecked: boolean, value: string) => {
    //   const updatedListItems = listItems.map((item) => {
    //     if (item.id === id) {
    //       return { ...item, isChecked };
    //     }
    //     return item;
    //   });
    //   setListItems(updatedListItems);
        setIsChecked(isChecked);
        props.onItemChecked(name, isChecked, value);
    };
  
    return (
        <div className="form-control">
            <label 
                className="cursor-pointer label justify-start" 
                htmlFor={props.id}
            >
                <input type="checkbox" className="checkbox checkbox-md"
                    id={props.id}
                    name={props.name}
                    checked={isChecked}
                    onChange={(e) => handleItemChecked(props.name, e.target.checked, e.target.value)}
                    value={props.label}
                    />
                <span className="text-light pl-2">{props.label}</span>
            </label>
        </div>
    );
  };
  
  export default CheckboxListItem;