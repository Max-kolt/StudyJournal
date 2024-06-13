import React from "react";
import { LoginBlock } from "../components/Auth/LoginBlock";

export function LoginPage() {
  return (
    <div className="h-full w-full login_bg relative flex items-end">
      <h1 className="text-white p-5 leading-tight max-[640px]]:hidden">
        КОЛЛЕДЖ <br /> ИНФОРМАЦИОННЫХ <br /> ТЕХНОЛОГИЙ
      </h1>
      <LoginBlock />
    </div>
  );
}
