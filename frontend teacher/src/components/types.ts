type NotificationType = {
  id: number;
  url: string;
  new: boolean;
  title: string;
  content: string;
};

type NotificationsListType = NotificationType[];

type GroupType = {
  id: string;
  specialization: string;
  qualification: string | null;
  course: number;
  students: string[];
  subjects: string[];
};

type studentMarksTable = {
  [key: number]: {
    id: number;
    name: string;
    marks: {
      [month: number]: number | undefined;
      mark: { [id: number]: string }[];
    }[];
    result: string;
  };
};

type studentAbsencesTable = {
  [key: number]: {
    id: number;
    name: string;
    marks: number[][];
  };
};
