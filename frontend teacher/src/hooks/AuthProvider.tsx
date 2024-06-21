import React, { useContext, createContext, useState } from "react";
import { useNavigate } from "react-router-dom";
import { login_api } from "../api/auth_api";

type AuthProviderProps = {
  children: React.ReactNode;
};

type LoginProps = {
  username: string;
  password: string;
};
type UserProps = {
  id: string | null;
  mail: string | null;
  username: string | null;
};
type contextProps = {
  token: null | string;
  user: UserProps | null;
  logIn: (data: LoginProps) => void;
  logOut: () => void;
};

const AuthContext = createContext<contextProps>({
  token: null,
  user: null,
  logIn: () => {},
  logOut: () => {},
});

const AuthProvider = ({ children }: AuthProviderProps) => {
  const [user, setUser] = useState<UserProps>({
    id: localStorage.getItem("id"),
    mail: localStorage.getItem("mail"),
    username: localStorage.getItem("user"),
  });
  const [token, setToken] = useState(localStorage.getItem("token") || null);
  const navigate = useNavigate();
  const logIn = (data: LoginProps) => {
    login_api(`username=${data.username}&password=${data.password}`)
      .then((value) => {
        // получение токена из ответа с сервера
        const token = value.data["access_token"];
        // сохранение токена в локальное хранилище пользователя
        localStorage.setItem("token", token);

        const user = value.data["user"];

        console.log(user);

        localStorage.setItem("id", user["id"]);
        localStorage.setItem("username", user["username"]);
        localStorage.setItem("mail", user["mail"]);

        setToken(token);
        setUser(user);
        if (localStorage.getItem("not_new")) navigate("/");
        else navigate("/change_password");
      })
      .catch(() => {
        alert("Неверный пароль или почта");
      });
  };

  const logOut = () => {
    setUser({ id: null, mail: null, username: null });
    setToken(null);
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    navigate("/login");
  };

  return (
    <AuthContext.Provider value={{ token, user, logIn, logOut }}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthProvider;

export const useAuth = () => {
  return useContext(AuthContext);
};
