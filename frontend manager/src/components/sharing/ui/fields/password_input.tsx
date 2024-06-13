import { useState } from "react";
import EyeIcon from "/eye.svg";

type PasswordInputProps = {
  onChangeHandler: (v: string) => void;
  label?: string;
};

export function PasswordInput({ onChangeHandler, label }: PasswordInputProps) {
  const [visible, setVisible] = useState(false);
  return (
    <div className="flex  flex-col gap-1 w-full">
      <label htmlFor="password">{label ? label : "Пароль"}</label>
      <div className="relative w-full flex items-center">
        <input
          type={!visible ? "password" : "text"}
          name="password"
          id="password"
          onChange={(v) => onChangeHandler(v.currentTarget.value)}
          className="rounded-md w-full max-h-10 p-2 bg-white border border-primary"
        />
        <img
          src={EyeIcon}
          alt="eye"
          className="absolute right-1 bg-white"
          onClick={() => setVisible(!visible)}
        />
      </div>
    </div>
  );
}
