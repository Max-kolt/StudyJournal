import { useState } from "react";

type InlineInputProps = {
  onChangeHandler: (v: string) => void;
  label?: string;
};

export function InlineInput({ onChangeHandler, label }: InlineInputProps) {
  return (
    <div className="flex flex-col gap-1 w-full">
      <label htmlFor={label}>{label}</label>
      <input
        type="text"
        name={label}
        id={label}
        className={"rounded-md max-h-10 p-2 bg-white border border-primary"}
        onChange={(v) => onChangeHandler(v.currentTarget.value)}
      />
    </div>
  );
}
