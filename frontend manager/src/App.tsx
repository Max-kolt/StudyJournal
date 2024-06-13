import { BrowserRouter, Route, Routes } from "react-router-dom";
import { LoginPage } from "./pages/login";
import { ErrorPage } from "./pages/error";
import { GroupsPage } from "./pages/groups";
import { ParentsPage } from "./pages/parents";
import { SpecializaationsPage } from "./pages/specializations";
import { StudentsPage } from "./pages/students";
import { TeachersPage } from "./pages/teachers";
import { TimetablePage } from "./pages/timetable";
import AuthProvider from "./hooks/AuthProvider";
import PrivateRoute from "./pages/router/private_router";
import { MainPage } from "./pages/main";
import { PlanPage } from "./pages/plan";

function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="*" element={<ErrorPage />} />
          <Route element={<PrivateRoute />}>
            <Route path="/plan" element={<PlanPage />} />
            <Route path="/" element={<MainPage />} />
            <Route path="/groups" element={<GroupsPage />} />
            <Route path="/parents" element={<ParentsPage />} />
            <Route path="/specializations" element={<SpecializaationsPage />} />
            <Route path="/students" element={<StudentsPage />} />
            <Route path="/teachers" element={<TeachersPage />} />
            <Route path="/timetable" element={<TimetablePage />} />
          </Route>
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;
