#palindrome

str1=input("Enter a string:")
str2=str1[::-1]
if list(str1) == list(str2):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
