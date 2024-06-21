import { AxiosResponse } from "axios";
import { apiInstance } from "./axios";

type AuthResponse = {
  accessToken: string;
};

export const login_api = <T>(body: T): Promise<AxiosResponse> => {
  return apiInstance.post<AuthResponse>("/auth/teacher_login", body);
};

export const change_password_api = <T>(body: T): Promise<AxiosResponse> => {
  return apiInstance.post<AuthResponse>("/user/change_password", body);
};

