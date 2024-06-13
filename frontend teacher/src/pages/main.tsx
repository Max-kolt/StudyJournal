import { MainPageLessonsView } from "../components/current_lessons/main_page_view";
import { AcademicRecord } from "../components/main_page_elements/academic_record";

export function MainPage() {
  return (
    <div className="flex justify-between h-full relative">
      <div className="h-fit w-auto p-10">
        <AcademicRecord />
      </div>
      <MainPageLessonsView />
    </div>
  );
}
