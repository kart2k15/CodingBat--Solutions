#Given a string, return a string where for every char in the original, there are two chars.
def double_char(str):
    s = ""
    for x in str:
        s = s + x * 2
    return s

#Return the number of times that the string "hi" appears anywhere in the given string.
def count_hi(str):
  return str.count("hi")

#Return True if the string "cat" and "dog" appear the same number of times in the given string.
def cat_dog(str):
    return str.count("dog") == str.count("cat")

#Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
def count_code(str):
    l = len(str) - 3
    res = 0
    i = 0
    while i < l:
        if str[i] == 'c' and str[i + 1] == 'o' and str[i + 3] == 'e':
            res = res + 1
            i = i + 4
        else:
            i = i + 1
    return res

#Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.
def end_other(a, b):
  a1=a.lower()
  b1=b.lower()
  return a1.endswith(b1) or b1.endswith(a1)

#Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
def xyz_there(str):
  l=len(str)-2
  i=0
  while(i<l):
    if str[i]=='x'and str[i+1]=='y' and str[i+2]=='z':
      if i==0 or str[i-1]!='.':
        return True
    i=i+1
  return False