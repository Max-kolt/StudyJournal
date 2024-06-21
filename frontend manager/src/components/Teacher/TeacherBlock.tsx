import { useEffect, useState } from "react";
import { Teacher } from "./contains/teacher";
import { get_teachers_api } from "../../api/teachers_api";
import { InlineInput } from "../sharing/ui/fields/inline_input";
import { DefaultButton } from "../sharing/ui/buttons/default_button";

export function TeacherBlock() {
  const [teachers, setTeachers] = useState<TeacherType[] | []>([]);
  const [active, setActive] = useState<TeacherType | null>(null);

  const submit = () => {};

  useEffect(() => {
    get_teachers_api()
      .then((value) => {
        setTeachers(value.data);
      })
      .catch(() => {
        alert("Что-то пошло не так");
      });
  }, []);

  return (
    <>
      <div className="flex justify-between gap-5">
        <div className="flex flex-col items-center w-2/3">
          {teachers.map((teacher) => {
            return (
              <Teacher
                key={teacher.id}
                teacher={teacher}
                onClick={() => setActive(teacher)}
                isActive={active?.id == teacher.id}
              />
            );
          })}
        </div>
        <div className="flex w-1/3 flex-col items-center">
          <form className="gap-3 w-full flex flex-col bg-white rounded-3xl p-6">
            <InlineInput label="Имя*" onChangeHandler={() => {}} />
            <InlineInput label="Фамилия*" onChangeHandler={() => {}} />
            <InlineInput label="Отчество" onChangeHandler={() => {}} />
            <InlineInput label="Почта*" onChangeHandler={() => {}} />
            <InlineInput label="Телефон" onChangeHandler={() => {}} />
            <InlineInput label="Пол*" onChangeHandler={() => {}} />
            <InlineInput label="Специальность*" onChangeHandler={() => {}} />
            <InlineInput label="Образование" onChangeHandler={() => {}} />
            <InlineInput label="Категория" onChangeHandler={() => {}} />
            <DefaultButton
              callbackHandler={submit}
              style="primary"
              text="Сохранить"
            />
          </form>
        </div>
      </div>
    </>
  );
}
