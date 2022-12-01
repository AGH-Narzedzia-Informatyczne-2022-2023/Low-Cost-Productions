print("...:::Prosty Kalkulator:::...")

x = int(input("Wprwowadź pierwszą liczbę:"))
y = int(input("Wprowadź drugą liczbę:"))
z = input("What type of operator you want to use(+,-,*,/,**)")

operators = {"+": x+y, "-": x-y, "*": x*y, "/": x/y, "**": x**y}

if(true==true)

print("we have a conflict")


if z == "+":
    print(operators["+"])
elif z == "-":
    print(operators["-"])
elif z == "*":
    print(operators["*"])
elif z == "/":
    print(operators["/"])
elif z == "**":
    print(operators["**"])
else:
    print("Error: operator not found(make sure you used the designated operators)")
