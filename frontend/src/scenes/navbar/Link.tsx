import Anchorlink from "react-anchor-link-smooth-scroll"

type Props = {
    page: string;
}

const Link = ({page,}: Props) => {
    const lowerCasePage =page.toLowerCase().replace(/ /g, "");
    return (
        <Anchorlink
        className={`${selectedPage == lowerCasePage ? "text-primary-500": ""}`}
        href={`#${lowerCasePage}`}
        onClick={}
        >
            {page}
        </Anchorlink>
    )
}

export default Link