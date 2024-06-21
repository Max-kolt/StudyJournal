import { ImageButton } from "../../sharing/ui/buttons/image_button";
import TrashIcon from "../../../../public/trash.svg";

export function Specialization(props: {
  specialization: SpecializationType;
  onDelete: (id: number) => void;
  onClick: () => void;
  isActive: boolean;
}) {
  return (
    <div
      onClick={() => props.onClick()}
      className={
        "w-full  pr-20 flex p-5 rounded-2xl   relative items-center gap-4 " +
        (props.isActive
          ? "border-2 border-primary2 "
          : "border border-primary3")
      }
    >
      <h3>{props.specialization.name}</h3>
      {props.specialization.qualification && (
        <p className="p_small">{props.specialization?.qualification}</p>
      )}
      <ImageButton
        img={TrashIcon}
        onClickHandler={() => props.onDelete(props.specialization.id)}
        color="text-veryWhite"
        bgColor=""
        custom="absolute right-2"
      />
    </div>
  );
}
