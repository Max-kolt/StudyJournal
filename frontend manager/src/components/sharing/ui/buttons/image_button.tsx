import React from "react";

type ImageButtonProps = {
  img: string;
  bgColor?: string;
  color?: string;
  children?: React.ReactNode;
  onClickHandler: () => void;
  custom?: string;
};

export function ImageButton({
  img,
  bgColor,
  color,
  children,
  onClickHandler,
  custom,
}: ImageButtonProps) {
  return (
    <div
      className={
        "cursor-pointer flex gap-1 p-2 items-center rounded-lg hover:border-primary2 border " +
        (bgColor
          ? `bg-${bgColor} border-${bgColor} `
          : "bg-veryWhite border-veryWhite ") +
        (custom && custom)
      }
      onClick={() => onClickHandler()}
    >
      <img width={36} height={36} className={color || "text-black"} src={img} />
      {children}
    </div>
  );
}
