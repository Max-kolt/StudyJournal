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
type UserProps = null | string;
type contextProps = {
  token: null | string;
  user: UserProps;
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
  const [user, setUser] = useState<UserProps>(null);
  const [token, setToken] = useState(localStorage.getItem("token") || null);
  const navigate = useNavigate();
  const logIn = (data: LoginProps) => {
    login_api(`username=${data.username}&password=${data.password}`)
      .then((value) => {
        const token = value.data["access_token"];
        localStorage.setItem("token", token);
        setToken(token);
        setUser(data.username);
        navigate("/");
      })
      .catch(() => {
        alert("Неверный пароль или имя пользователя");
      });
  };

  const logOut = () => {
    setUser(null);
    setToken(null);
    localStorage.removeItem("token");
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
