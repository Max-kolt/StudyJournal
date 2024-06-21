import { AxiosResponse } from "axios";
import { apiInstance } from "./axios";

export const create_admin_api = <T>(body: T): Promise<AxiosResponse> => {
  return apiInstance.post("/admin/create", body);
};
