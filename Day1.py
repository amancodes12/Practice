#1. Number Palindrome
num = int(input("Enter number: "))
if str(num) == str(num) [::-1]:
  print("Palindrome")
else
  print("Not Palindrome")


#2. String Palindrome
s = input("Enter a string: ")
if s == s [::-1]:
  print("Palindrome")
else:
  print("Not Palindrome")


#3. Check if a number is Armstrong 
def is_armstrong(n):
  digits = str(n)
  power = len(digits)
  total = sum(int(d)**power for d in digits)
  return total == n
