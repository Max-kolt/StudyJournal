import { useNavigate } from "react-router-dom";
import { LessonViewBlockProps } from "../main_page_view";
import { ImageButton } from "../../sharing/buttons/image_button";
import TableIcon from "/grid-edit.svg";
import ActiveIcon from "/play.svg";

export function LessonBLock({
  id,
  group,
  state,
  lessonCount,
  lessonName,
  url,
}: LessonViewBlockProps) {
  const navigate = useNavigate();
  return (
    <div
      key={id}
      className="p-2 pr-20 relative flex flex-col justify-center bg-veryWhite rounded-lg"
    >
      <p className="text-primaryText2 items-center flex gap-2">
        Группа {group}
        <span className="small text-grey2">{lessonCount} пара</span>
      </p>
      <p className="p_small self-c">{lessonName}</p>
      {(state == "active" && (
        <ImageButton
          img={ActiveIcon}
          onClickHandler={() => {
            url && navigate(url);
          }}
          color="text-black"
          bgColor="posit"
          custom="absolute right-4 w-11"
        />
      )) ||
        (state == "passed" && (
          <ImageButton
            img={TableIcon}
            onClickHandler={() => {
              url && navigate(url);
            }}
            color="text-veryWhite"
            bgColor="primary2"
            custom="absolute right-4 w-11"
          />
        ))}
    </div>
  );
}
