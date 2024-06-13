import React, { useState } from "react";
import ClockIcon from "/clock.svg";
import RightArrowIcon from "/arrow-right.svg";
import LeftArrowIcon from "/arrow-left.svg";
import { useNavigate } from "react-router-dom";
import { ImageButton } from "../sharing/buttons/image_button";
import { LessonBLock } from "./current_lesson_block/lesson_block";

export type LessonViewBlockProps = {
  id: number;
  group: string;
  lessonCount: number;
  lessonName: string;
  state: "active" | "passed" | "expected";
  url?: string;
};

type LessonsViewProps = {
  todayDate: Date;
  todayDateString: string;
  lessons: LessonViewBlockProps[];
};

export function MainPageLessonsView() {
  const navigate = useNavigate();

  const [lessonView, setLessonView] = useState<LessonsViewProps>({
    todayDate: new Date(2024, 2, 26),
    todayDateString: "26 февраля",
    lessons: [
      {
        id: 0,
        group: "404",
        lessonCount: 1,
        lessonName: "МДК07.01 Управление и автоматизация баз данных",
        state: "passed",
        url: "/lesson/32131",
      },
      {
        id: 1,
        group: "404",
        lessonCount: 2,
        lessonName: "МДК07.01 Управление и автоматизация баз данных",
        state: "active",
        url: "/lesson/32131",
      },
      {
        id: 2,
        group: "404",
        lessonCount: 3,
        lessonName: "МДК07.01 Управление и автоматизация баз данных",
        state: "expected",
        url: "/lesson/32131",
      },
    ],
  });

  const getNextDay = () => {
    console.log("get next day");
  };
  const getPreviusDay = () => {
    console.log("get previus day");
  };

  return (
    <section className="bg-white right-0 h-full min-w-96 p-4 flex flex-col items-center gap-2">
      <header className="flex gap-3 items-center text-primaryText2">
        <img src={ClockIcon} width={32} />
        <h3>Сегодня, {lessonView.todayDateString}</h3>
        <div className="text-black flex gap-1">
          <img
            className="cursor-pointer"
            onClick={getPreviusDay}
            src={LeftArrowIcon}
            width={24}
          />
          <img
            className="cursor-pointer"
            onClick={getNextDay}
            src={RightArrowIcon}
            width={24}
          />
        </div>
      </header>
      <div className="flex flex-col gap-3 w-full h-full">
        {lessonView.lessons.map((obj) => {
          return <LessonBLock {...obj} />;
        })}
      </div>
    </section>
  );
}
