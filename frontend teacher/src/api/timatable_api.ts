import { AxiosResponse } from "axios";
import { apiInstance } from "./axios";

export const get_timetable_api = (): Promise<AxiosResponse> => {
  return apiInstance.get(
    `/timetable/get_teacher_timetable?teacher_id=${localStorage.getItem("id")}`
  );
};

type tableDatesProps = {
  group: string;
  lesson: string;
};

export const get_table_dates_api = ({
  group,
  lesson,
}: tableDatesProps): Promise<AxiosResponse> => {
  return apiInstance.get(
    `/timetable/get_lesson_dates?group=${group}&lesson=${lesson}`
  );
};
