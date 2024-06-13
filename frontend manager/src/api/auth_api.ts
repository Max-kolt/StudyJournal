import { AxiosResponse } from "axios";
import { apiInstance } from "./axios";

type AuthResponse = {
  accessToken: string;
};

export const login_api = <T>(body: T): Promise<AxiosResponse> => {
  return apiInstance.post<AuthResponse>("/auth/manager_login", body);
};
