import { useEffect, useState } from "react";
import { get_timetable_api } from "../../api/timatable_api";

const MOCK_TABLE = {
  Понедельник: [
    { lesson_number: 1, name: "Программирование", group: "404", cabinet: 402 },
    { lesson_number: 2, name: "Программирование", group: "404", cabinet: 402 },
    {
      lesson_number: 3,
      name: "МДК11.01 Технология разработки и защиты баз данных",
      group: "404",
      cabinet: 402,
    },
    {
      lesson_number: 4,
      name: "МДК11.01 Технология разработки и защиты баз данных",
      group: "404",
      cabinet: 402,
    },
    { lesson_number: 5, name: "Программирование", group: "404", cabinet: 402 },
    { lesson_number: 6, name: "Программирование", group: "404", cabinet: 402 },
  ],
  Вторник: [
    { lesson_number: 3, name: "Программирование", group: "404", cabinet: 402 },
    { lesson_number: 4, name: "Программирование", group: "404", cabinet: 402 },
    {
      lesson_number: 5,
      name: "МДК11.01 Технология разработки и защиты баз данных",
      group: "404",
      cabinet: 402,
    },
    {
      lesson_number: 6,
      name: "МДК11.01 Технология разработки и защиты баз данных",
      group: "404",
      cabinet: 402,
    },
  ],
  Среда: [
    { lesson_number: 1, name: "Программирование", group: "404", cabinet: 402 },
    { lesson_number: 2, name: "Программирование", group: "404", cabinet: 402 },
    {
      lesson_number: 3,
      name: "МДК11.01 Технология разработки и защиты баз данных",
      group: "404",
      cabinet: 402,
    },
    {
      lesson_number: 4,
      name: "МДК11.01 Технология разработки и защиты баз данных",
      group: "404",
      cabinet: 402,
    },
  ],
  Четверг: [
    { lesson_number: 1, name: "Программирование", group: "404", cabinet: 402 },
    { lesson_number: 2, name: "Программирование", group: "404", cabinet: 402 },
    {
      lesson_number: 5,
      name: "МДК11.01 Технология разработки и защиты баз данных",
      group: "404",
      cabinet: 402,
    },
    {
      lesson_number: 6,
      name: "МДК11.01 Технология разработки и защиты баз данных",
      group: "404",
      cabinet: 402,
    },
  ],
  Пятница: [
    {
      lesson_number: 5,
      name: "МДК11.01 Технология разработки и защиты баз данных",
      group: "404",
      cabinet: 402,
    },
    {
      lesson_number: 6,
      name: "МДК11.01 Технология разработки и защиты баз данных",
      group: "404",
      cabinet: 402,
    },
  ],
};

export function TimetableBlock() {
  const [lessonsTimetable, setLessonsTimetable] = useState(MOCK_TABLE);

  useEffect(() => {
    get_timetable_api().then((value) => {
      setLessonsTimetable(value.data);
    });
  }, []);

  return (
    <div className="flex gap-3 h-full justify-center p-7">
      <div className="w-24 h-full grid gap-3 grid-rows-4 items-start justify-center pt-10">
        {[1, 2, 3, 4].map((num) => {
          return <div className="">{num} пара</div>;
        })}
      </div>
      {lessonsTimetable &&
        Object.entries(lessonsTimetable).map(([day, lessons]) => {
          lessons.sort((a, b) => a.lesson_number - b.lesson_number);
          return (
            <div className="justify-start w-32 h-full flex flex-col items-center ">
              <p className="mb-4">{day}</p>
              <div className="grid grid-rows-4 gap-3 h-full w-full">
                {lessons.map((lesson, index) => {
                  const lesson_number = {
                    1: 1,
                    2: 1,
                    3: 2,
                    4: 2,
                    5: 3,
                    6: 3,
                    7: 4,
                    8: 4,
                  }[lesson.lesson_number];
                  const index_depth = lesson_number - index;
                  console.log(index_depth, lesson_number);
                  return (
                    lesson.lesson_number % 2 == 1 && (
                      <>
                        {index_depth < 0 && <div></div>}
                        <div
                          className={
                            lesson_number +
                            " bg-white border flex flex-col items-center justify-between border-primary3 hover:border-primary2 w-full h-full p-2 row-span-1 "
                          }
                        >
                          <p className="text-primaryText w-full h-20 overflow-hidden text-ellipsis">
                            {lesson.name}
                          </p>
                          <div className="flex flex-col items-center">
                            <p className="small">
                              Кабинет: {lesson.cabinet || "Д/О"}
                            </p>
                            <p className="text-primaryText2">
                              {lesson.group} группа
                            </p>
                          </div>
                        </div>
                      </>
                    )
                  );
                })}
              </div>
            </div>
          );
        })}
    </div>
  );
}
