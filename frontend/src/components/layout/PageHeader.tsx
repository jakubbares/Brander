import React from "react";

export type HeaderProps = {
    name?: string;
};

const PageHeader: React.FC<HeaderProps> = (props) => {
    return (
        <div className="fixed w-full top-0 left-0">
            <div className="flex flex-row justify-between container mx-auto py-5 px-2">
            <div>
                <div className="text-4xl font-bold mb-2">Brander</div>
            </div>
            <div className="flex items-center gap-5">
                <h1 className="text-4xl font-bold mb-2">Petr Pavel</h1>
                {/* <Image src="/img/profile_img.png" alt="Profile image" width={40} height={40} /> */}
                <img src="/img/profile_img.png" alt="Profile image" className="rounded-full h-16 w-16 mt-[-5px]" />
            </div>
            </div>
        </div>
    );
}

export default PageHeader;