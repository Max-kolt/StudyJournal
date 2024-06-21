import DelIcon from "../../../public/trash.svg";
import { MenuButton } from "../sharing/buttons/menu_button";
import { DefaultPopup } from "./default_popup";

type MarksEditPopup = {
  clickHandler: () => void;
  putHandler: (func: "add" | "del", value?: string) => void;
  marks: string[];
  position: [number, number];
};

export function MarksEditPopup({
  clickHandler,
  putHandler,
  position,
  marks,
}: MarksEditPopup) {
  return (
    <DefaultPopup clickHandler={clickHandler}>
      <div
        className="fixed bg-primary p-px flex flex-col gap-px rounded-lg"
        style={{ top: position[0], left: position[1] }}
      >
        <div className="flex rounded-md bg-veryWhite">
          {marks.map((mark) => {
            return (
              <MenuButton
                key={mark}
                onClickHandler={() => {
                  putHandler("add", mark);
                }}
              >
                <p className="p_small px-3 py-2">{mark}</p>
              </MenuButton>
            );
          })}
          <p
            className="small cursor-pointer p-2 bg-neg rounded-md"
            onClick={() => {
              putHandler("del");
            }}
          >
            <img width={20} src={DelIcon} />
          </p>
        </div>
      </div>
    </DefaultPopup>
  );
}
