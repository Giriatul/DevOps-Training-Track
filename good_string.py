# Program to find a good string from a given input
def solve(s):
   res = []
   for ch in s:
      if res and res[-1] != ch and res[-1].lower() == ch.lower():
         res.pop()
      else:
         res.append(ch)
   return ''.join(res)

s = "popPpulaBbr"
print(solve(s))
