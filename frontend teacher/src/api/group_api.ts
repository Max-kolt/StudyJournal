import { AxiosResponse } from "axios";
import { apiInstance } from "./axios";

export const get_group_api = (): Promise<AxiosResponse> => {
  return apiInstance.get(
    `/groups/get_teacher_groups?teacher_id=${localStorage.getItem("id")}`
  );
};

export const get_current_group_api = (group: str): Promise<AxiosResponse> => {
  return apiInstance.get(
    `/groups/get_by_id/${group}?teacher=${localStorage.getItem("id")}`
  );
};

export const get_group_lesson_marks_api = (
  group: string,
  lesson: string
): Promise<AxiosResponse> => {
  return apiInstance.get(
    `/groups/get_group_marks?group=${group}&lesson=${lesson}`
  );
};
