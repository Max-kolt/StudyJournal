import { MenuButton } from "../sharing/buttons/menu_button";
import { DefaultPopup } from "./default_popup";

type MarksPutPopup = {
  clickHandler: () => void;
  putHandler: (mark: string) => void;
  position: [number, number];
  marks: string[];
};

export function MarksPutPopup({
  clickHandler,
  putHandler,
  marks,
  position,
}: MarksPutPopup) {
  return (
    <DefaultPopup clickHandler={clickHandler}>
      <div
        className="fixed flex rounded-lg  border bg-veryWhite border-primary"
        style={{ top: position[0], left: position[1] }}
      >
        {marks.map((mark) => {
          return (
            <MenuButton
              key={mark}
              onClickHandler={() => {
                putHandler(mark);
              }}
            >
              <p className="p_small py-2 px-3">{mark}</p>
            </MenuButton>
          );
        })}
      </div>
    </DefaultPopup>
  );
}
