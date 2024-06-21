export function deleteFromCell(tableData: any, cellInfo: any) {
  const mark_index = tableData[
    cellInfo.stud as keyof typeof tableData
  ].marks.findIndex(
    (mark: any) => mark[cellInfo.month as keyof typeof mark] === cellInfo.day
  );

  tableData[cellInfo.stud as keyof typeof tableData].marks.splice(
    mark_index,
    1
  );
  return tableData;
}

export function addToCell(tableData: any, cellInfo: any, value: any) {
  const prevMarks: string[] = tableData[
    cellInfo.stud as keyof typeof tableData
  ].marks.filter((mark: any) => {
    if (mark[cellInfo.month as keyof typeof mark] == cellInfo.day) return mark;
  })[0].mark;

  const newCell = {
    mark: [...prevMarks, value],
    [cellInfo.month]: cellInfo.day,
  };
  return newCell;
}
