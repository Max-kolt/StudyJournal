import { Navigate, Outlet } from "react-router-dom";
import { useAuth } from "../../hooks/AuthProvider";
import { DefaultLayout } from "../layouts/default";

const PrivateRoute = () => {
  const user = useAuth();
  if (!user.token) return <Navigate to="/login" />;
  return (
    <DefaultLayout>
      <Outlet />
    </DefaultLayout>
  );
};

export default PrivateRoute;
