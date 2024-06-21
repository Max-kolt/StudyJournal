import { DefaultPopup } from "./default_popup";
import QuitIcon from "../../../../public/logout.svg";
import { useNavigate } from "react-router-dom";
import { MenuButton } from "../ui/buttons/menu_button";
import { useAuth } from "../../../hooks/AuthProvider";

type ProfilePopupProps = {
  clickHandler: () => void;
  profileId?: string;
};

export function ProfilePopup({ clickHandler }: ProfilePopupProps) {
  const navigator = useNavigate();
  const auth = useAuth();
  

  const profileLink = () => {
    navigator(`/profile/`);
  };

  const logoutLink = () => {
    auth.logOut();
    navigator("/login");
  };

  return (
    <DefaultPopup clickHandler={clickHandler}>
      <div className="fixed top-16 right-16 bg-veryWhite border border-primary2 rounded-lg">
        <MenuButton padding="p-2" onClickHandler={logoutLink}>
          <img src={QuitIcon} width={24} />
          <p className="p_small text-neg">Выйти</p>
        </MenuButton>
      </div>
    </DefaultPopup>
  );
}
