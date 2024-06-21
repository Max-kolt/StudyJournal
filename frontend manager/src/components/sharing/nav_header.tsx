import { Link, useLocation } from "react-router-dom";
import { NotificationButton } from "./nav/notification_nav";
import { ProfileButton } from "./nav/profile_nav";

export function NavigationHeader() {
  const currentPage = useLocation().pathname;
  return (
    <div className="w-screen max-w-full h-20 flex justify-between pl-3 items-center z-40 bg-white border-b border-primary2">
      <nav className="flex gap-3">
        <Link
          to="/"
          className={
            currentPage == "/"
              ? "text-primary px-7 py-4 text"
              : "text-black px-7 py-4 rounded-lg hover:bg-grey4 hover:text-grey1 "
          }
        >
          Главная
        </Link>
        <Link
          to="/specializations"
          className={
            currentPage == "/specializations"
              ? "text-primary px-7 py-4 text"
              : "text-black px-7 py-4 rounded-lg hover:bg-grey4 hover:text-grey1 "
          }
        >
          Cпециализации
        </Link>
        <Link
          to="/plan"
          className={
            currentPage == "/plan"
              ? "text-primary px-7 py-4 text"
              : "text-black px-7 py-4 rounded-lg hover:bg-grey4 hover:text-grey1 "
          }
        >
          План
        </Link>
        <Link
          to="/timetable"
          className={
            currentPage == "/timetable"
              ? "text-primary px-7 py-4 text"
              : "text-black px-7 py-4 rounded-lg hover:bg-grey4 hover:text-grey1 "
          }
        >
          Расписание
        </Link>
        <Link
          to="/groups"
          className={
            currentPage == "/groups"
              ? "text-primary px-7 py-4 text"
              : "text-black px-7 py-4 rounded-lg hover:bg-grey4 hover:text-grey1 "
          }
        >
          Группы
        </Link>
        <Link
          to="/students"
          className={
            currentPage == "/students"
              ? "text-primary px-7 py-4 text"
              : "text-black px-7 py-4 rounded-lg hover:bg-grey4 hover:text-grey1 "
          }
        >
          Студенты
        </Link>

        <Link
          to="/teachers"
          className={
            currentPage == "/teachers"
              ? "text-primary px-7 py-4 text"
              : "text-black px-7 py-4 rounded-lg hover:bg-grey4 hover:text-grey1 "
          }
        >
          Преподаватели
        </Link>
      </nav>
      <div className="flex border-l items-center border-l-primary2 border-solid px-3 gap-2">
        {/* <NotificationButton /> */}
        <ProfileButton />
      </div>
    </div>
  );
}
