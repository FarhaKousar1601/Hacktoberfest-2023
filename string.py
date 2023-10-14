str1 = input("Enter a string 1\n: ")
str2 = input("Enter string 2\n : ")
if len(str1) < len(str2):
   short = len(str2)
   long = len(str1)

else:
 short = len(str1)
long = len(str1)

matchcnt = 0
for i in range(short):
    if str1[i] == str2[i]:
        matchcnt += 1
        print("similarity between two strings :")
        print(matchcnt/long)
