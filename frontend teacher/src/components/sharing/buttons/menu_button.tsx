import React from "react";

type MenuButtonProps = {
  children: React.ReactNode;
  padding?: string;
  hoverColor?: string;
  onClickHandler: () => void;
  custom?: string;
};

export function MenuButton({
  children,
  padding,
  hoverColor,
  onClickHandler,
  custom,
}: MenuButtonProps) {
  return (
    <div
      className={
        (padding && padding) +
        " cursor-pointer rounded-lg flex gap-2 hover:" +
        (hoverColor ? hoverColor : "bg-grey4 ") +
        (custom && custom)
      }
      onClick={() => onClickHandler()}
    >
      {children}
    </div>
  );
}
