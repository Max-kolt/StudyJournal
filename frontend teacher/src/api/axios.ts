import axios from "axios";
import { useAuth } from "../hooks/AuthProvider";

export const apiInstance = axios.create({
  baseURL: `http://0.0.0.0:8000/api/v1`,
});

const authInterpretor = (config: any) => {
  config.headers.Authorization = `Bearer ${localStorage.getItem("token")}`;
  return config;
};
apiInstance.interceptors.request.use(authInterpretor);
apiInstance.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    console.log(error);
    if (error.response.status === 401) {
      const auth = useAuth();
      auth.logOut();
    }
    return error;
  }
);
