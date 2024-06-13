import { BrowserRouter, Route, Routes, useParams } from "react-router-dom";
import { AuthProvider } from "./hooks/AuthProvider";
import { ErrorPage } from "./pages/error";
import { LoginPage } from "./pages/login";
import { PrivateRoute } from "./router/private_route";
import { MainPage } from "./pages/main";
import { ChangePasswordPage } from "./pages/change_password";

export function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          <Route path="*" element={<ErrorPage />} />
          <Route path="/login" element={<LoginPage />} />
          <Route path="/change_password" element={<ChangePasswordPage />} />
          <Route element={<PrivateRoute />}>
            <Route path="/" element={<MainPage />} />

            <Route path="/timetable" element={<>Таблица</>} />
            <Route path="/groups/:groupId" element={<>Группы</>} />
            <Route path="/homeworks" element={<>Дзшки</>} />
            <Route
              path="/groups/:groupId/marks"
              element={<>Какая-то группа {useParams().groupId}</>}
            />
            <Route path="/profile/:profileId" element={<>Профиль</>} />
          </Route>
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
}
