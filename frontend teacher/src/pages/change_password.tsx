import { ChangePasswordBlock } from "../components/auth_page_elements/ChangePasswordBlock";

export function ChangePasswordPage() {
  return (
    <div className="h-full w-full login_bg relative flex items-end">
      <h1 className="text-white p-5 leading-tight">
        КОЛЛЕДЖ <br /> ИНФОРМАЦИОННЫХ <br /> ТЕХНОЛОГИЙ
      </h1>
      <ChangePasswordBlock />
    </div>
  );
}
