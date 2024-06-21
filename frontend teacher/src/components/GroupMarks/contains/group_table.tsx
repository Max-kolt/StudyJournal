import { useEffect, useState } from "react";
import { MarksPutPopup } from "../../popup/marks_put_popup";
import { MarksEditPopup } from "../../popup/marks_edit_popup";
import { deleteFromCell, addToCell } from "./table_operations";
import { default_months } from "../../constants";
import { get_group_lesson_marks_api } from "../../../api/group_api";
import {
  delete_student_records_api,
  post_student_records_api,
} from "../../../api/student_records_api";
import { get_table_dates_api } from "../../../api/timatable_api";

type MarksTableProps = {
  canEdit: boolean;
  group: string;
  subject: string;
};

const MOCK_ABSENCES = {
  1: {
    id: 1,
    name: "Иванов Иван ",
    absence_dates: [
      [11, 5],
      [10, 3],
    ],
  },
  3: {
    id: 4,
    name: "Муравьев Иван ",
    absence_dates: [
      [11, 3],
      [9, 1],
    ],
  },
};
const MOCK_MARKS: studentMarksTable = {
  1: {
    id: 1,
    name: "Иванов Иван ",
    marks: [
      { mark: ["5"], 9: 3 },
      { mark: ["4"], 11: 2 },
      { mark: ["2"], 10: 10 },
      { mark: ["5", "5", "5", "5", "5"], 10: 11 },
      { mark: ["4"], 9: 21 },
      { mark: ["5"], 11: 18 },
    ],
    result: "4.4",
  },
  2: {
    id: 2,
    name: "Котин Иван ",
    marks: [
      { mark: ["5"], 9: 1 },
      { mark: ["4", "4"], 11: 2 },
      { mark: ["2"], 9: 5 },
      { mark: ["5", "4"], 10: 11 },
      { mark: ["4"], 9: 21 },
      { mark: ["5"], 10: 28 },
    ],
    result: "4.13",
  },
  3: {
    id: 3,
    name: "Муравьев Иван ",
    marks: [
      { mark: ["5"], 9: 1 },
      { mark: ["2", "3"], 10: 2 },
      { mark: ["2"], 9: 12 },
      { mark: ["5", "5", "5"], 11: 16 },
      { mark: ["4"], 10: 18 },
      { mark: ["5"], 11: 18 },
    ],
    result: "4.1",
  },
  4: {
    id: 4,
    name: "Муравьев Иван ",
    marks: [
      { mark: ["5"], 9: 1 },
      { mark: ["2", "3"], 10: 2 },
      { mark: ["2"], 9: 12 },
      { mark: ["5", "5", "5"], 11: 16 },
      { mark: ["4"], 10: 18 },
      { mark: ["5"], 11: 18 },
    ],
    result: "4.1",
  },
  5: {
    id: 5,
    name: "Колов Иван ",
    marks: [
      { mark: ["5"], 9: 1 },
      { mark: ["2", "3"], 10: 2 },
      { mark: ["2"], 9: 12 },
      { mark: ["5", "5", "5"], 11: 16 },
      { mark: ["4"], 10: 18 },
      { mark: ["5"], 11: 18 },
    ],
    result: "3.2",
  },
  6: {
    id: 6,
    name: "Пароаа Иван ",
    marks: [
      { mark: ["5"], 9: 1 },
      { mark: ["2", "3"], 10: 2 },
      { mark: ["2"], 9: 12 },
      { mark: ["5", "5", "5"], 11: 16 },
      { mark: ["4"], 10: 18 },
      { mark: ["5"], 11: 18 },
    ],
    result: "4.3",
  },
};

const MOCK_DATES = [
  {
    month: 1,
    year: 2024,
    days: [1, 2, 3, 5, 10, 11, 12, 16, 17, 18, 21, 22, 23, 27, 28, 30],
  },
  {
    month: 2,
    days: [1, 2, 3, 5, 10, 11, 12, 16, 17, 18, 21, 22, 23, 27, 28, 30],
  },
  {
    month: 3,
    days: [1, 2, 3, 5, 10, 11, 12, 16, 17, 18, 21, 22, 23, 27, 28, 30],
  },
];

export function GroupTable({ canEdit, group, subject }: MarksTableProps) {
  const [editCell, setEditCell] = useState<
    | { month: number; day: number; stud: number; mark?: any; ids?: string[][] }
    | false
  >(false);
  const [subjectId, setSubjectId] = useState(0);
  const [popupPosition, setPopupPosition] = useState<[number, number]>([0, 0]);
  const [studentMarksLesson, setStudentMarksLesson] =
    useState<studentMarksTable>();
  const [lessonDates, setLessonsDates] =
    useState<{ year: number; month: number; days: number[] }[]>();

  useEffect(() => {
    get_group_lesson_marks_api(group, subject)
      .then((value) => {
        setStudentMarksLesson(value.data["group_marks"]);
        setSubjectId(value.data["subject"]);

        get_table_dates_api({ group: group, lesson: value.data["subject"] })
          .then((value) => {
            setLessonsDates(value.data);
          })
          .catch(() => alert("Что-то пошло не так"));
      })
      .catch(() => alert("Что-то пошло не так"));

    // setStudentMarksLesson(MOCK_MARKS);
  }, []);

  useEffect(() => {
    if (!editCell && canEdit) {
      window.addEventListener("mousedown", mouseClick);
      return () => {
        window.removeEventListener("mousedown", mouseClick);
      };
    }
  }, [editCell]);

  const mouseClick = (e: MouseEvent) => {
    setPopupPosition([e.clientY, e.clientX]);
    window.removeEventListener("mousedown", mouseClick);
  };

  const putCell = (value: string) => {
    if (canEdit && editCell) {
      post_student_records_api({
        student_id: editCell.stud,
        lesson_id: subjectId,
        day: editCell.day,
        month: editCell.month,
        mark: value,
      }).then((value) => {
        if (value.data["new_result"]) {
          setStudentMarksLesson({
            ...studentMarksLesson,
            [editCell.stud]: {
              ...studentMarksLesson[editCell.stud],
              result: value.data["new_result"],
            },
          });
        }
      });

      const newMark = { mark: [value], [editCell.month]: editCell.day };
      let newMarksTable = Object.assign({}, studentMarksLesson);

      newMarksTable[
        editCell.stud as keyof typeof studentMarksLesson
      ].marks.push(newMark);

      setStudentMarksLesson(newMarksTable);
    }
    setEditCell(false);
  };

  const putEditCell = (func: "add" | "del", value?: string) => {
    if (canEdit && editCell) {
      let newMarksTable = Object.assign({}, studentMarksLesson);

      if (func == "del") {
        delete_student_records_api({
          student_id: editCell.stud,
          lesson_id: subjectId,
          day: editCell.day,
          month: editCell.month,
        })
          .then((value) => {
            setStudentMarksLesson({
              ...studentMarksLesson,
              [editCell.stud]: {
                ...studentMarksLesson[editCell.stud],
                result: value.data["new_result"],
              },
            });
          })
          .catch(() => alert("Что-то пошло не так"));
        newMarksTable = deleteFromCell(newMarksTable, editCell);
      } else if (func == "add" && value) {
        const data = {
          student_id: editCell.stud,
          lesson_id: subjectId,
          day: editCell.day,
          month: editCell.month,
          mark: value,
        };
        console.log(data);
        post_student_records_api(data).then((value) => {
          if (value.data["new_result"]) {
            setStudentMarksLesson({
              ...studentMarksLesson,
              [editCell.stud]: {
                ...studentMarksLesson[editCell.stud],
                result: value.data["new_result"],
              },
            });
          }
        });
        const newCell = addToCell(newMarksTable, editCell, value);
        newMarksTable = deleteFromCell(newMarksTable, editCell);
        newMarksTable[
          editCell.stud as keyof typeof studentMarksLesson
        ].marks.push(newCell);
      } else alert("Что-то пошло не так");
      setStudentMarksLesson(newMarksTable);
    }

    setEditCell(false);
  };

  const putAbsence = () => {
    setEditCell(false);
  };

  return (
    <div className="w-full relative overflow-scroll no-scrollbar">
      <div className="p_bold text-primaryText w-fit  flex border-b-2 border-primary">
        <div className="border-r-2 fixed bg-veryWhite border-primary p-2 h-14 w-48 flex justify-end items-end">
          Фамилия Имя
        </div>
        <div className="flex">
          {lessonDates?.map((months) => {
            return (
              <div
                key={`${months.month}`}
                className="border-r-2 border-primary h-14 first:ml-48 last:mr-20 last:border-0"
              >
                <p className="p-1 h-7 p_bold">
                  {default_months[months.month as keyof typeof default_months]}
                </p>
                <p className="p_bold h-7  flex">
                  {months.days.map((days) => {
                    return (
                      <div
                        key={`${days}`}
                        className="w-12 flex justify-center items-center last:border-0 border-r-2 border-primary"
                      >
                        {days}
                      </div>
                    );
                  })}
                </p>
              </div>
            );
          })}
        </div>
        <div className=" border-l-2   fixed right-0 bg-veryWhite border-primary p-2 h-14 w-20 flex justify-center items-center">
          Итог
        </div>
      </div>
      {studentMarksLesson &&
        Object.entries(studentMarksLesson).map(([id, stud]) => {
          return (
            <div
              key={id}
              className={
                "flex border-r-2 border-primary w-fit " +
                (Number.parseInt(id) % 2 == 1 ? "bg-grey4" : "bg-white")
              }
            >
              <div
                className={
                  (stud.id % 2 == 1 ? "bg-grey4" : "bg-white") +
                  " whitespace-nowrap whitespace-nowrap p_bold border-r-2 fixed border-primary p-2 h-10 w-48 flex justify-end items-end"
                }
              >
                {stud.name}
              </div>
              <div className="flex pl-48">
                {lessonDates?.map((month) => {
                  return (
                    <div className="flex border-r-2 border-primary last:border-0">
                      {month.days.map((day) => {
                        const date_mark = stud.marks.filter((mark) => {
                          if (mark[month.month as keyof typeof mark] == day) {
                            return mark;
                          }
                        });
                        if (date_mark.length > 0) {
                          const marks = date_mark[0].mark.map((mark) => {
                            return Object.values(mark);
                          });
                          const ids = date_mark[0].mark.map((mark) => {
                            return Object.keys(mark);
                          });

                          return (
                            <div
                              key={`${month} ${day}`}
                              onClick={() => {
                                setEditCell({
                                  month: month.month,
                                  day: day,
                                  stud: stud.id,
                                  mark: marks,
                                  ids: ids,
                                });
                              }}
                              className={
                                (canEdit && "hover:bg-veryWhite") +
                                " h-10  w-12 flex items-center justify-center border-r-2 border-primary last:border-0"
                              }
                            >
                              {marks.join(",")}
                            </div>
                          );
                        }
                        return (
                          <div
                            key={`${month} ${day}`}
                            onClick={() => {
                              setEditCell({
                                month: month.month,
                                day: day,
                                stud: stud.id,
                                mark: undefined,
                              });
                            }}
                            className={
                              (canEdit && "hover:bg-veryWhite") +
                              " h-10  w-12 flex items-center justify-center border-r-2 border-primary last:border-0"
                            }
                          ></div>
                        );
                      })}
                    </div>
                  );
                })}
              </div>
              <div
                className={
                  "w-20 fixed right-0 h-10 flex justify-center items-center border-l-2 border-primary " +
                  (stud.id % 2 == 1 ? "bg-grey4" : "bg-white")
                }
              >
                {`${stud.result}`.slice(0, 3)}
              </div>
            </div>
          );
        })}
      {editCell && editCell.mark && canEdit && (
        <MarksEditPopup
          position={[popupPosition[0], popupPosition[1]]}
          putHandler={putEditCell}
          marks={["2", "3", "4", "5", "Н"]}
          clickHandler={() => setEditCell(false)}
        />
      )}
      {editCell && !editCell.mark && canEdit && (
        <MarksPutPopup
          position={[popupPosition[0], popupPosition[1]]}
          putHandler={putCell}
          marks={["2", "3", "4", "5", "Н"]}
          clickHandler={() => setEditCell(false)}
        />
      )}
    </div>
  );
}
