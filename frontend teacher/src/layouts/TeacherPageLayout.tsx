import React from "react";
import { Link, useLocation } from "react-router-dom";
import { NotificationButton } from "../components/nav/notification_nav";
import { ProfileButton } from "../components/nav/profile_nav";

type props = { children: React.ReactNode };

export function TeacherPageLayout({ children }: props) {
  const currentPage = useLocation().pathname;

  return (
    <>
      <div className="fixed w-screen h-20 flex justify-between pl-3 items-center z-40 bg-white border-b border-primary2">
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
            Мои группы
          </Link>
          {/* <Link
            to="/homeworks"
            className={
              currentPage == "/homeworks"
                ? "text-primary px-7 py-4 text"
                : "text-black px-7 py-4 rounded-lg hover:bg-grey4 hover:text-grey1 "
            }
          >
            Домашние задания
          </Link> */}
        </nav>
        <div className="flex border-l items-center border-l-primary2 border-solid px-3 gap-2">
          {/* <NotificationButton /> */}
          <ProfileButton />
        </div>
      </div>
      <div className="pt-20 h-full">{children}</div>
    </>
  );
}
