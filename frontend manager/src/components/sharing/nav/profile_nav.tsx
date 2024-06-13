import { useEffect, useState } from "react";
import ProfileAvatar from "/user.svg";
import { ProfilePopup } from "../popup/profile_popup";

export function ProfileButton() {
  const [isActive, setActive] = useState(false);

  const activate = () => {
    setActive(!isActive);
  };

  return (
    <>
      <div
        onClick={activate}
        className="p-3 bg-veryWhite rounded-lg flex items-center gap-2"
      >
        <div className="p-2 rounded-full bg-grey4">
          <img src={ProfileAvatar} alt="profile_avatar" />
        </div>
        <div className="p_bold">
          Руководитель
          <br />
          учебной части
        </div>
      </div>
      {isActive && <ProfilePopup clickHandler={activate} />}
    </>
  );
}
