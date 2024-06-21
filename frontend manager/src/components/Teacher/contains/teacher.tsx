import { useEffect } from "react";
import { DefaultButton } from "../../sharing/ui/buttons/default_button";

export function Teacher({
  teacher,
  onClick,
  isActive,
}: {
  teacher: TeacherType;
  onClick: () => void;
  isActive: boolean;
}) {
  const create_account = () => {
    teacher.user.with_account = true;
  };

  useEffect(() => console.log(teacher.user.with_account), []);

  return (
    <div
      onClick={onClick}
      className={
        "flex items-center w-full pl-5 justify-between rounded-2xl gap-4 relative " +
        (isActive ? "border-2 border-primary2 " : "border border-primary3 ") +
        (teacher.user.with_account && " p-5")
      }
    >
      <h3>
        {teacher.user.fname} {teacher.user.lname}
      </h3>
      {teacher.user.with_account || (
        <DefaultButton
          style="primary"
          text="Создать аккаунт"
          callbackHandler={create_account}
        />
      )}
    </div>
  );
}
