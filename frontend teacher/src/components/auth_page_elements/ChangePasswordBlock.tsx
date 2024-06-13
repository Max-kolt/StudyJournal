import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { DefaultButton } from "../sharing/buttons/default_button";
import { PasswordInput } from "../sharing/fields/password_input";

export function ChangePasswordBlock() {
  const [newPassword, setNewPassword] = useState("");
  const [verifyPassword, setVerifyPassword] = useState("");

  const navigate = useNavigate();

  const submit = () => {
    if (newPassword == verifyPassword) {
      navigate("/");
      return;
    }
    alert("Пароли не совпадают");
  };

  return (
    <div className="absolute right-0 top-0 h-full w-1/2 bg-white flex flex-col gap-20 justify-center items-center">
      <h2>Смена пароля</h2>
      <form className="flex flex-col gap-5 items-center w-1/2">
        <PasswordInput
          label="Новый пароль"
          onChangeHandler={(v: string) => setNewPassword(v)}
        />
        <PasswordInput
          label="Подтверждение пароля"
          onChangeHandler={(v: string) => setVerifyPassword(v)}
        />
        <DefaultButton
          callbackHandler={submit}
          text="Продолжить"
          style="primary"
        />
        <Link to="/" className="button text-primaryText2">
          Не менять
        </Link>
      </form>
    </div>
  );
}
