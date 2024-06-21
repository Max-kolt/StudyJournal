import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { DefaultButton } from "../sharing/ui/buttons/default_button";
import { InlineInput } from "../sharing/ui/fields/inline_input";
import { PasswordInput } from "../sharing/ui/fields/password_input";
import { useAuth } from "../../hooks/AuthProvider";

export function LoginBlock() {
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();
  const auth = useAuth();

  const submit = () => {
    if (name == "" || password == "") {
      alert("Не все поля заполнены");
      return;
    }
    auth.logIn({username: name, password: password});
    navigate("/");
  };

  return (
    <div className="absolute right-0 top-0 h-full w-1/2 max-[640px]:w-full bg-white flex flex-col gap-20 justify-center items-center">
      <h2>Авторизация</h2>
      <form className="flex flex-col gap-5 items-center w-1/2">
        <InlineInput label="Имя" onChangeHandler={(v: string) => setName(v)} />
        <PasswordInput onChangeHandler={(v: string) => setPassword(v)} />
        <DefaultButton callbackHandler={submit} text="Войти" style="primary" />
      </form>
    </div>
  );
}
