__author__ = 'jc451631'
choice = int(input("Enter a positive value ; "))
sales = float(input("Enter your sale"))
while choice >= 0:
     if sales<1000:
        bonus = 0.1*sales
        print("bonus is ",bonus)

     elif sales>=1000:
        bonus=0.15*sales
        print("bonus is",bonus)
     choice = int(input("Enter a positive value ; "))
print("thank you")
