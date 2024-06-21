import { AxiosResponse } from "axios";
import { apiInstance } from "./axios";

export const get_specializatoins_api = (): Promise<AxiosResponse> => {
  return apiInstance.get("/specializations/get_all");
};

type CreateSpecializatoinProps = {
  name: string;
  qualification: string | null;
};

export const create_specializatoin_api = <CreateSpecializatoinProps>(
  body: CreateSpecializatoinProps
): Promise<AxiosResponse> => {
  return apiInstance.post("/specializations/create", body);
};

export const delete_specializatoin_api = (
  body: number
): Promise<AxiosResponse> => {
  return apiInstance.delete(
    "/specializations/delete?specialization_id=" + body
  );
};
