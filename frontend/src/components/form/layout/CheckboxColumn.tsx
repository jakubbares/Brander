
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

export default CheckboxColumn;