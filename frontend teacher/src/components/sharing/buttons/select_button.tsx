import { DefaultButton } from "./default_button";
import ArrowIcon from "../../../../public/arrow-down.svg";
import { useState } from "react";
import { DefaultPopup } from "../../popup/default_popup";
import { MenuButton } from "./menu_button";

type OptionProps = {
  text: string;
  callbackHandler: () => void;
};

type SelectButtonProps = {
  text: string;
  options: OptionProps[];
};

export function SelectButton({ text, options }: SelectButtonProps) {
  const [active, setActive] = useState(false);

  return (
    <>
      <DefaultButton
        style="primary"
        text={text}
        img={ArrowIcon}
        callbackHandler={() => setActive(true)}
      />
      {active && (
        <DefaultPopup clickHandler={() => setActive(false)}>
          <div className="bg-white border fixed right-2 top-56 border-primary3 rounded-xl">
            {options.map((option) => {
              return (
                <MenuButton
                  padding="p-3"
                  onClickHandler={option.callbackHandler}
                >
                  {option.text}
                </MenuButton>
              );
            })}
          </div>
        </DefaultPopup>
      )}
    </>
  );
}
