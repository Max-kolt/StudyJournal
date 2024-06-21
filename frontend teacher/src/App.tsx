import { BrowserRouter, Route, Routes, useParams } from "react-router-dom";
import AuthProvider from "./hooks/AuthProvider";
import { ErrorPage } from "./pages/error";
import { LoginPage } from "./pages/login";
import { PrivateRoute } from "./router/private_route";
import { MainPage } from "./pages/main";
import { ChangePasswordPage } from "./pages/change_password";
import { ProfilePage } from "./pages/profile";
import { GroupPage } from "./pages/groups";
import { GroupMarksPage } from "./pages/group_marks";
import { TimetablePage } from "./pages/timetable";
import { AcademicRecrdsPage } from "./pages/acadenic_records";

export function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          <Route path="*" element={<ErrorPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route element={<PrivateRoute />}>
            <Route path="/change_password" element={<ChangePasswordPage />} />
            <Route path="/" element={<MainPage />} />
            <Route path="/timetable" element={<TimetablePage />} />
            <Route path="/groups" element={<GroupPage />} />
            <Route path="/homeworks" element={<></>} />
            <Route
              path="/group/:groupID/academic_records"
              element={<AcademicRecrdsPage />}
            />
            <Route
              path="/groups/:groupID/:subjectID"
              element={<GroupMarksPage />}
            />
            <Route path="/profile" element={<ProfilePage />} />
          </Route>
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
}
