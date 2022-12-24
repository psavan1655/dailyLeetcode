function isSubsequence(s: string, t: string): boolean {
  let sPtr = 0;

  for (let i of t) {
    if (s[sPtr] === i) sPtr += 1;
  }

  return s.length === sPtr;
}

console.log(isSubsequence('axc', 'ahbgdc'));
