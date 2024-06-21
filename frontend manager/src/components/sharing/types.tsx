type NotificationType = {
  id: number;
  url: string;
  new: boolean;
  title: string;
  content: string;
};

type NotificationsListType = NotificationType[];

type SpecializationType = {
  id: number;
  name: string;
  qualification?: string;
};

type TeacherType = {
  user_id: string;
  specialization_id: number;
  education: string;
  category: string;
  id: number;
  user: {
    fname: string;
    lname: string;
    mname: string;
    mail: string;
    phone: string;
    gender: string;
    with_account: boolean;
  };
};
