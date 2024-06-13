import { useState } from "react";
import { ImageButton } from "../sharing/buttons/image_button";
import Notification from "/notification.svg";
import { NotificationPopup } from "../popup/notification_popup";

export function NotificationButton() {
  const [notifications, setNotifications] = useState<NotificationsListType>([
    {
      id: 1,
      url: "",
      new: true,
      title: "Всем преподавателям",
      content: "Присутсвовать на собрании 27.12 dasdsadsdadgsewf",
    },
  ]);
  const [newNotifications, setNewNotifications] = useState(true);
  const [isActive, setActive] = useState(false);

  const activate = () => {
    setNewNotifications(false);
    setActive(!isActive);
    if (isActive == true) {
      setNotifications(
        notifications.map((obj) => {
          if (obj.new) obj.new = false;
          return obj;
        })
      );
    }
  };

  return (
    <>
      <ImageButton
        custom="relative"
        onClickHandler={activate}
        img={Notification}
      >
        {newNotifications && (
          <span className="bg-neg absolute top-1 right-1 rounded-full w-3 h-3" />
        )}
      </ImageButton>
      {isActive && (
        <NotificationPopup
          notifications={notifications}
          clickHandler={activate}
        />
      )}
    </>
  );
}
