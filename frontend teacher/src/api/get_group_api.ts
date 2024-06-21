import { AxiosResponse } from "axios";
import { apiInstance } from "./axios";

export const get_group_api = (): Promise<AxiosResponse> => {
  return apiInstance.get(
    `/groups/get_teacher_groups?teacher_id=${localStorage.getItem("id")}`
  );
};
