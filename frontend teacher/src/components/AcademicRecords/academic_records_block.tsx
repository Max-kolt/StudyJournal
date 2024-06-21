import { useEffect, useState } from "react";
import { get_group_api } from "../../api/get_group_api";
import { get_current_group_api } from "../../api/group_api";

export function AcademicRecordsBlock(group: str) {
  const [groups, setGroups] = useState();

  useEffect(() => {
    get_current_group_api(group).then((value) => {
      setGroups(value.data);
    });
  }, []);

  return <div></div>;
}
