import { list } from "postcss";
import { useEffect, useState } from "react";
import { DefaultButton } from "../sharing/buttons/default_button";
import { MenuButton } from "../sharing/buttons/menu_button";
import { get_group_api } from "../../api/get_group_api";
import { useNavigate } from "react-router-dom";
import { SelectButton } from "../sharing/buttons/select_button";

export function GroupBlock() {
  const navigate = useNavigate();
  const [groupsList, setGroupsList] = useState<[GroupType] | []>([]);
  const [active, setActive] = useState<null | GroupType>(groupsList[0] || null);

  useEffect(() => {
    get_group_api()
      .then((value) => {
        const groups = value.data;
        setGroupsList(groups);
        setActive(groups[0]);
      })
      .catch(() => alert("Что-то пошло не так"));
  }, []);
  return (
    <div className="relative flex flex-col items-center h-full gap-10 max-h-full w-full">
      <div className="overflow-scroll flex items-center w-full justify-between no-scrollbar">
        <div className="flex flex-col gap-2 h-30">
          <div className="flex mb-10 pt-1 gap-6">
            <h1>Группа {active?.id}</h1>
            <h3 className="text-primaryText2">{active?.course} курс</h3>
          </div>
          <p>Специальность: {active?.specialization}</p>
          <p>
            Квалификация:{" "}
            {active?.qualification ? active?.qualification : "отсутствует"}
          </p>
        </div>
        {active && (
          <SelectButton
            text="Смотреть оценки"
            options={active.subjects.map((subject) => {
              return {
                text: subject,
                callbackHandler: () =>
                  navigate(`/groups/${active.id}/${subject}`),
              };
            })}
          />
        )}
      </div>
      <div className="flex flex-col gap-4 w-full">
        <p>Студенты группы </p>
        <div className=" grid gap-4 grid-cols-2 px-5">
          {active?.students.map((student) => {
            return (
              <div className="w-full p-3 bg-white rounded-xl">{student}</div>
            );
          })}
        </div>
      </div>

      <div className="absolute flex gap-2 bottom-5 p-3 border bg-white border-primary2 rounded-xl">
        {groupsList.map((group) => {
          return (
            <MenuButton
              onClickHandler={() => setActive(group)}
              padding="px-4 py-2"
              custom={group.id == active?.id ? "bg-primary3" : "bg-grey4"}
            >
              {group.id}
            </MenuButton>
          );
        })}
      </div>
    </div>
  );
}
