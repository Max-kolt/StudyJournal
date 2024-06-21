import { useState } from "react";
import { InlineInput } from "../ui/fields/inline_input";
import { DefaultPopup } from "./default_popup";
import { DefaultButton } from "../ui/buttons/default_button";
import { create_admin_api } from "../../../api/admin_api";

type CreateAdminPopupProps = {
  outsideClickHandler: () => void;
};

export function CreateAdminPopup({
  outsideClickHandler,
}: CreateAdminPopupProps) {
  const [name, setName] = useState("");
  const [password, setPassword] = useState<null | string>(null);
  const passwordHandler = (v: string) => {
    if (v == "") setPassword(null);
    else setPassword(v);
  };

  const submit = () => {
    if (name != "") {
      create_admin_api({ name: name, password: password })
        .then((value) => {
          alert(
            `name: ${value.data["name"]} \npassword: ${value.data["password"]}`
          );
        })
        .catch((error) => {
          alert(error);
        });

      return;
    }
    alert("Введи уникальное имя!");
  };

  return (
    <DefaultPopup clickHandler={outsideClickHandler}>
      <div className=" top-1/3 left-1/3 p-8 fixed bg-veryWhite border  border-primary2 rounded-xl ">
        <form onSubmit={submit}>
          <InlineInput
            onChangeHandler={(v) => setName(v)}
            label="Уникальное имя пользователя"
          />
          <InlineInput
            onChangeHandler={(v) => passwordHandler(v)}
            label="Впиши пароль или мы придумаем его за тебя"
          />
          <DefaultButton
            callbackHandler={submit}
            text="Создать"
            style="primary"
          />
        </form>
      </div>
    </DefaultPopup>
  );
}
