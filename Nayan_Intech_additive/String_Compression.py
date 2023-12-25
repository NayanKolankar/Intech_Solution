def compress(s):
   res = ""
   count = 1
   res += s[0]
   for i in range(len(s) - 1):
       if s[i] == s[i + 1]:
           count += 1
       else:
           res += str(count)
           count = 1
           res += s[i + 1]


   if s[-1] == s[-2]:
       res += str(count)
   else:
       res += "1"


   return res




def secondcomp(s):
   res = ""
   res += s[0]
   cha = []
   freq = []


   i = 0
   while i < len(s):
       x = ord(s[i])
       if x >= 97 and x <= 122:
           cha.append(s[i])
       else:
           f = ""
           # print(x)
           if x >= 48 and x <= 57:
               f += chr(x)


           num = int(f)
           freq.append(f)
       i += 1


   # print(cha,freq)


   i = 0
   while i < len(freq) - 1:
       if freq[i] == freq[i + 1]:
           res += cha[i + 1]
       else:
           res += str(freq[i])
           res += cha[i + 1]
       i += 1


   res += str(freq[len(freq) - 1])
   return res




def decompress(s):
   res = ""
   cha = []
   freq = []
   j = 0
   for i in range(len(s)):
       x = ord(s[i])
       if x >= 97 and x <= 122:
           cha.append(s[i])
           j += 1
       else:
           f = ""
           if x >= 48 and x <= 57:
               f += chr(x)


           # i -= 1
           num = int(f)
           while j > 0:
               freq.append(num)
               j -= 1
           j = 0


   for i in range(len(cha)):
       x = freq[i]
       while x > 0:
           res += cha[i]
           x -= 1
   return res




x = compress("aaabbbcccbbc")
print(x)
y = secondcomp(x)
print(y)
z = decompress(y)
print(z)
