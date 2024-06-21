import { useState } from "react";
import { DefaultButton } from "../sharing/buttons/default_button";
import { InlineInput } from "../sharing/fields/inline_input";
import { PasswordInput } from "../sharing/fields/password_input";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../../hooks/AuthProvider";

export function LoginBlock() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const auth = useAuth();

  const submit = () => {
    // Логика запроса к API
    if (email == "" || password == "") {
      alert("Не все поля заполнены");
      return;
    }
    auth.logIn({ username: email, password: password });
  };

  return (
    <div className="absolute right-0 top-0 h-full w-1/2 max-[640px]:w-full bg-white flex flex-col gap-20 justify-center items-center">
      <h2>Авторизация</h2>
      <form className="flex flex-col gap-5 items-center w-1/2">
        <InlineInput
          label="Почта"
          onChangeHandler={(v: string) => setEmail(v)}
        />
        <PasswordInput onChangeHandler={(v: string) => setPassword(v)} />
        <DefaultButton callbackHandler={submit} text="Войти" style="primary" />
      </form>
    </div>
  );
}
