import { LoginBlock } from "../components/auth_page_elements/LoginBlock";

export function LoginPage() {
  return (
    <div className="h-full w-full login_bg relative flex items-end">
      <h1 className="text-white p-5 leading-tight">
        КОЛЛЕДЖ <br /> ИНФОРМАЦИОННЫХ <br /> ТЕХНОЛОГИЙ
      </h1>
      <LoginBlock />
    </div>
  );
}
