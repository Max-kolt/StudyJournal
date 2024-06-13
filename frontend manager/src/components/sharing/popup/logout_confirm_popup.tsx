import { useNavigate } from "react-router-dom";
import { useAuth } from "../../../hooks/AuthProvider";
import { DefaultButton } from "../ui/buttons/default_button";
import { DefaultPopup } from "./default_popup";

type LogoutConfirmPopupProps = {
  clickHandler: () => void;
};

export function LogoutConfirmPopup({ clickHandler }: LogoutConfirmPopupProps) {
  const navigator = useNavigate();
  const auth = useAuth();

  const logoutLink = () => {
    auth.logOut();
    navigator("/login");
  };
  return <DefaultPopup clickHandler={clickHandler}></DefaultPopup>;
}
