import { useState } from "react";
import { MenuButton } from "../sharing/buttons/menu_button";
import { useNavigate } from "react-router-dom";

export function AcademicRecord() {
  const [groupsList, setGroupsList] = useState([
    { id: 1, url: "/group/404/academic_records/", name: "404" },
    { id: 1, url: "/group/404/academic_records/", name: "404" },
    { id: 1, url: "/group/404/academic_records/", name: "404" },
    { id: 1, url: "/group/404/academic_records/", name: "404" },
    { id: 1, url: "/group/404/academic_records/", name: "404" },
  ]);
  const navigate = useNavigate();

  return (
    <section className=" flex flex-col gap-5 border-2 border-primary p-6 bg-white">
      <header>
        <h2>
          Семестр подходит к концу, проверьте академическую ведомость ваших
          групп и опубликуйте!
        </h2>
      </header>
      <div className="flex gap-3 w-full overflow-hidden">
        {groupsList.map((group) => {
          return (
            <MenuButton
              key={group.id}
              custom="px-4 py-2 bg-grey4 border border-grey4 hover:border-primary"
              onClickHandler={() => navigate(group.url)}
            >
              {group.name}
            </MenuButton>
          );
        })}
      </div>
    </section>
  );
}
