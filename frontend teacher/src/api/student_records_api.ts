import { AxiosResponse } from "axios";
import { apiInstance } from "./axios";

export const get_student_records_api = (): Promise<AxiosResponse> => {
  return apiInstance.get("");
};

type StudAddRecordProps = {
  student_id: int;
  lesson_id: int;
  day: int;
  month: int;
  mark: string;
};

type StudRecordProps = {
  student_id: int;
  lesson_id: int;
  day: int;
  month: int;
};

export const post_student_records_api = <StudAddRecordProps>(
  body: StudAddRecordProps
): Promise<AxiosResponse> => {
  return apiInstance.post("/students/insert_mark", body);
};

export const delete_student_records_api = <StudRecordProps>(
  body: StudRecordProps
): Promise<AxiosResponse> => {
  return apiInstance.post("/students/remove_marks", body);
};
