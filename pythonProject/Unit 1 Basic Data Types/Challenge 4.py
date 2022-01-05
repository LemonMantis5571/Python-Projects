def getStr(s):
  s=s[:1] + s[0] + s[1:]# Transform the string
  s=s[:1] + s[0] + s[1:]
  s=s[:3] + s[3] + s[3:]
  s=s[:3] + s[3] + s[3:]
  s=s[:6] + s[6] + s[6:]
  s=s[:6] + s[6] + s[6:]
  s=s[:9] + s[9] + s[9:]
  s=s[:9] + s[9] + s[9:]
  # Update the length of string
  strlen = len(s)
  print(s, strlen)
  return [s, strlen]
[s, strlen] = getStr("abcd")