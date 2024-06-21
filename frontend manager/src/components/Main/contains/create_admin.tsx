import { useState } from "react";
import { DefaultButton } from "../../sharing/ui/buttons/default_button";
import { CreateAdminPopup } from "../../sharing/popup/create_admin_popup";

export function CreateAdmin() {
  const [click, isClicked] = useState(false);

  return (
    <div className="w-full border rounded-xl border-primary2 py-1 px-5 flex justify-between items-center gap-2">
      <h2>Создать нового админа</h2>
      <DefaultButton
        callbackHandler={() => isClicked(true)}
        text="Создать"
        style="primary"
      />
      {click && (
        <CreateAdminPopup outsideClickHandler={() => isClicked(false)} />
      )}
    </div>
  );
}
