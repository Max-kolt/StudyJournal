import { Link } from "react-router-dom";
import { DefaultPopup } from "./default_popup";

type NotificationPopupProps = {
  clickHandler: () => void;
  notifications?: NotificationsListType;
};

export function NotificationPopup({
  clickHandler,
  notifications,
}: NotificationPopupProps) {
  return (
    <DefaultPopup clickHandler={clickHandler}>
      <div className="rounded-lg border max-w-60 border-primary2 p-2 w-fit bg-veryWhite fixed right-30 top-16">
        <h4 className="w-full border-b border-primary2 text-primaryText">
          Уведомления
        </h4>
        {notifications
          ? notifications.map((value) => {
              return (
                <Link to={value.url}>
                  <div className="py-1 pl-2 relative flex flex-col justify-center">
                    {value.new && (
                      <span className="absolute w-1 h-1 rounded -left-px bg-neg" />
                    )}
                    <span className="p_small whitespace-nowrap text-ellipsis overflow-hidden">
                      {value.title}
                    </span>
                    <span className="small whitespace-nowrap text-ellipsis overflow-hidden ">
                      {value.content}
                    </span>
                  </div>
                </Link>
              );
            })
          : "Уведомлений нет"}
      </div>
    </DefaultPopup>
  );
}
