import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { DefaultButton } from "../sharing/buttons/default_button";
import { PasswordInput } from "../sharing/fields/password_input";
import { change_password_api } from "../../api/auth_api";
import { useAuth } from "../../hooks/AuthProvider";

export function ChangePasswordBlock() {
  const [oldPassword, setOldPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [verifyPassword, setVerifyPassword] = useState("");
  const auth = useAuth();

  const navigate = useNavigate();

  const submit = () => {
    if (newPassword == verifyPassword) {
      change_password_api({
        id: auth.user,
        old_password: oldPassword,
        new_password: newPassword,
      })
        .then(() => {
          navigate("/");
          localStorage.setItem("not_new", "true");
        })
        .catch((reason) => {
          alert(reason);
        });
      return;
    }
    alert("Пароли не совпадают");
  };

  return (
    <div className="absolute right-0 top-0 h-full w-full bg-white flex flex-col gap-20 justify-center items-center">
      <h2>Смена пароля</h2>
      <form className="flex flex-col gap-5 items-center w-1/2">
        <PasswordInput
          label="Старый пароль"
          onChangeHandler={(v: string) => setOldPassword(v)}
        />
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
