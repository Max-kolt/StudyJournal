import React, { createContext, useContext, useState } from "react";
import { useNavigate } from "react-router-dom";

type props = { children: React.ReactNode };
type contextProps = {
  token: null | string;
  user: null | {
    username: string;
    id: string;
    email: string;
  };
  logIn: () => void;
  logOut: () => void;
};

const AuthContext = createContext<contextProps>({
  token: null,
  user: null,
  logIn: () => {},
  logOut: () => {},
});

export function AuthProvider({ children }: props) {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(localStorage.getItem("site") || "");
  const navigate = useNavigate();

  const logIn = () => {
    navigate("/");

    return;
  };
  const logOut = () => {
    navigate("/login");
  };

  return (
    <AuthContext.Provider value={{ user, token, logIn, logOut }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => {
  return useContext(AuthContext);
};
