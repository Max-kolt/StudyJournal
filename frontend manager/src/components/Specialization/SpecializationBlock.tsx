import { useEffect, useState } from "react";
import { DefaultButton } from "../sharing/ui/buttons/default_button";
import TrashIcon from "../../../public/trash.svg";
import {
  create_specializatoin_api,
  delete_specializatoin_api,
  get_specializatoins_api,
} from "../../api/specializations_api";
import { ImageButton } from "../sharing/ui/buttons/image_button";
import { Specialization } from "./contains/specialization";
import { InlineInput } from "../sharing/ui/fields/inline_input";

type SpecializationList = SpecializationType[];

export function SpecializationBlock() {
  const [specializations, setSpecializations] = useState<
    SpecializationList | []
  >([]);

  const [active, setActive] = useState<SpecializationType | null>(null);
  const deleteSpec = (id: number) => {
    delete_specializatoin_api(id);
    setSpecializations([
      ...specializations.filter((spec) => {
        if (spec.id != id) return spec;
        else return;
      }),
    ]);
    setActive(null);
  };

  useEffect(() => {
    get_specializatoins_api()
      .then((value) => {
        setSpecializations(value.data);
      })
      .catch(() => {
        alert("Что-то пошло не так");
      });
  }, []);

  const [name, setName] = useState("");
  const [qualification, setQualification] = useState<null | string>(null);

  const changeQualification = (v: string) => {
    if (v == "") setQualification(null);
    else setQualification(v);
  };

  const submit = () => {
    create_specializatoin_api({ name: name, qualification: qualification })
      .then((value) => {
        setSpecializations([...specializations, value.data]);
      })
      .catch(() => {
        alert("Не получилось сохранить, обратитесь к администратору");
      });
  };

  return (
    <>
      <div className="flex justify-between gap-6 ">
        <div className="flex flex-col items-center gap-3 w-2/3">
          {specializations.map((spec) => {
            return (
              <Specialization
                key={spec.id}
                specialization={spec}
                onDelete={deleteSpec}
                onClick={() => {
                  setActive(spec);
                }}
                isActive={active?.id == spec.id}
              />
            );
          })}
        </div>
        <div className="w-1/3  flex flex-col gap-3">
          <form className="gap-5 flex flex-col bg-white rounded-3xl p-6">
            <InlineInput
              label="Название"
              onChangeHandler={(v: string) => setName(v)}
            />
            <InlineInput
              label="Квалификация (необязательно)"
              onChangeHandler={(v: string) => changeQualification(v)}
            />
            <DefaultButton
              callbackHandler={submit}
              style="primary"
              text="Сохранить"
            />
          </form>
          {active && (
            <form className="gap-5 flex flex-col bg-white rounded-3xl p-6"></form>
          )}
        </div>
      </div>
    </>
  );
}
