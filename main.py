# Author: Abel Ismael agi5031@psu.edu
# Collaborator Ryan Dang rvd5465@psu.edu
# Collaborator Yash Raj yqr5113@psu.edu
# Collaborator Zhe Han zxh5206@psu.edu

temp1 = input("Enter temperature: ")
temp1 = float(temp1)
unit = input("Enter unit in F/f or C/c: ")
if (unit == "f" or unit == "F"):
  temp2 = ((temp1 - 32)/1.8)
  print (f"{(temp1)}° in Fahrenheit is equivalent to {(temp2)}° Celsius.")
elif (unit == "c" or unit == "C"):
  temp2 = ((temp1 * (1.8)+ 32))
  print (f"{(temp1)}° in Celsius is equivalent to {(temp2)}° Fahrenheit.")
else:
  print(f"Invalid unit ({unit}).");