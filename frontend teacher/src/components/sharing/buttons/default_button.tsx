type DefaultButtonProps = {
  callbackHandler: () => void;
  img?: string;
  text: string;
  style: "primary" | "secondary";
};

export function DefaultButton({
  callbackHandler,
  img,
  text,
  style,
}: DefaultButtonProps) {
  return (
    <div
      className={
        "m-4 cursor-pointer flex items-center justify-center gap-10 max-h-44 min-w-40 h-auto py-2 px-8 rounded-3xl border border-primary button " +
        (style == "primary" && "bg-primary text-white ") +
        (style == "secondary" && " bg-white text-primaryText")
      }
      onClick={() => callbackHandler()}
    >
      {text} {img && <img src={img} width={24} />}
    </div>
  );
}
