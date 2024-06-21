import { AxiosResponse } from "axios";
import { apiInstance } from "./axios";

export const get_teachers_api = (): Promise<AxiosResponse> => {
  return apiInstance.get("/teachers/get_all");
};
