import { useParams } from "react-router-dom";
import { AcademicRecordsBlock } from "../components/AcademicRecords/academic_records_block";

export function AcademicRecrdsPage() {
  const groupID = useParams().groupID;

  return (
    <>
      <AcademicRecordsBlock group={groupID} />
    </>
  );
}
