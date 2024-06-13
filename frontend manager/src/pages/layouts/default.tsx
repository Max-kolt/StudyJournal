import { ReactNode } from "react";
import { NavigationHeader } from "../../components/sharing/nav_header";

type props = {
  children: ReactNode;
};

export function DefaultLayout({ children }: props) {
  return (
    <>
      <NavigationHeader />
      <div className="relativ h-full">{children}</div>
    </>
  );
}
