import { useParams } from "react-router-dom";
import { DefaultButton } from "../sharing/buttons/default_button";
import EditIcon from "../../../public/edit.svg";
import EyeIcon from "../../../public/eye.svg";
import { useEffect, useState } from "react";
import { GroupTable } from "./contains/group_table";
import { get_subject_api } from "../../api/subjects_api";

export function GroupMarksBlock() {
  const groupID = useParams().groupID;
  const subjectID = useParams().subjectID;
  const [editMode, setEditMode] = useState(false);

  return (
    <div className="h-full w-full pl-6 pt-8">
      <div className=" p-5 flex items-center justify-between">
        <div className="flex flex-col gap-6">
          <h1>Оценки группы {groupID}</h1>
          <h3 className="text-primaryText2">{subjectID}</h3>
        </div>
        <DefaultButton
          text={editMode ? "Просмотр" : "Редактировать"}
          img={editMode ? EyeIcon : EditIcon}
          style={editMode ? "secondary" : "primary"}
          callbackHandler={() => setEditMode(!editMode)}
        />
      </div>
      <GroupTable
        canEdit={editMode}
        group={groupID}
        subject={subjectID }
      />
    </div>
  );
}
