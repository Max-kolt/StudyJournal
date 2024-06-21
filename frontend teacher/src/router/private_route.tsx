import { useAuth } from "../hooks/AuthProvider";
import { Navigate, Outlet } from "react-router-dom";
import { TeacherPageLayout } from "../layouts/TeacherPageLayout";

export function PrivateRoute() {
  const auth = useAuth();
  if (!auth.token || auth.token == "") return <Navigate to="/login" />;

  return (
    <TeacherPageLayout>
      <Outlet />
    </TeacherPageLayout>
  );
}
