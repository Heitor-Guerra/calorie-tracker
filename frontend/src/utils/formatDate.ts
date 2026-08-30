export function formatDate(date: Date | string) {
  const parsedDate = date instanceof Date ? date : new Date(date);

  return parsedDate.toLocaleDateString("pt-BR");
}
