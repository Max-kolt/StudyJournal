import React from "react";
import { useNavigate } from "react-router-dom";

export function ErrorPage() {
  const navigate = useNavigate();
  return (
    <div className="w-full flex flex-col gap-10 p-10 items-center">
      <h1>404. Такой страницы не существует</h1>
      <p
        onClick={() => navigate("/")}
        className="cursor-pointer underline text-primary2"
      >
        Вернуться на главную
      </p>
    </div>
  );
}
