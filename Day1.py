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


#4. Factorial
def factorial(n):
  if n == 0 or n == 1:
    return 1
  return n * factorial(n-1)

num = int(input("Enter a number: "))
print("Factorial of", num, "is", factorial(num))


#5. Fibonnaci


#6. Electricity Bill
def e_bill(units):
  if units <= 100:
    return units*1
  elif units <= 200:
    return 100*1 + (units-100)*3
  else:
    return 100*1 + 100*3 + (units-200)*5
units = int(input("Enter no. of units: "))
print("Electricity bill is:", e_bill(units))
