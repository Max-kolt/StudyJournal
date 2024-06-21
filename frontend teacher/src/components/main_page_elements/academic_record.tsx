import { useEffect, useState } from "react";
import { MenuButton } from "../sharing/buttons/menu_button";
import { useNavigate } from "react-router-dom";
import { get_group_api } from "../../api/get_group_api";

export function AcademicRecord() {
  const [groupsList, setGroupsList] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    get_group_api().then((value) => {
      setGroupsList(value.data);
    });
  }, []);

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
              onClickHandler={() =>
                navigate("/group/" + group.id + "/academic_records/")
              }
            >
              {group.id}
            </MenuButton>
          );
        })}
      </div>
    </section>
  );
}
