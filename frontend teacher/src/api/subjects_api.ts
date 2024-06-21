import { AxiosResponse } from "axios";
import { apiInstance } from "./axios";

export const get_subject_api = (lesson: int): Promise<AxiosResponse> => {
  return apiInstance.get(`/timetable/subject?lesson=${lesson}`);
};
