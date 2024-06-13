import { DefaultPopup } from "./default_popup";

type CreateAdminPopupProps = {
  outsideClickHandler: () => void;
};

export function CreateAdminPopup({
  outsideClickHandler,
}: CreateAdminPopupProps) {
  return (
    <DefaultPopup clickHandler={outsideClickHandler}>
      <div className="self-center bg-veryWhite border border-primary2 rounded-xl"></div>
    </DefaultPopup>
  );
}
