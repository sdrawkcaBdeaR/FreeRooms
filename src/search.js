export function findStringsContainingSubstring(strings, s) {
  const result = strings.filter(str => str.includes(s.toUpperCase()));
  return result;
}
