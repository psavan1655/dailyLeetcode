function isIsomorphic(s: string, t: string): boolean {
  const characterMap: Record<string, string> = {};

  for (let i = 0; i < s.length; i++) {
    if (characterMap[s[i]]) {
      if (characterMap[s[i]] !== t[i]) return false;
    } else {
      if (Object.values(characterMap).some((val) => val === t[i])) return false;
      characterMap[s[i]] = t[i];
    }
  }

  return true;
}

console.log(isIsomorphic('badc', 'baba'));
