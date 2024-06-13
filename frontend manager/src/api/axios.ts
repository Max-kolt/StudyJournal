import axios from "axios";
import { useAuth } from "../hooks/AuthProvider";

const authInterpretor = (config: any) => {
  config.headers.Authorization = `Bearer ${localStorage.getItem("token")}`;
  return config;
};

export const apiInstance = axios.create({
  baseURL: `http://127.0.0.1:8000/api/v1`,
});

apiInstance.interceptors.request.use(authInterpretor);
