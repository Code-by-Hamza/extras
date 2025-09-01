import time

def add(x,y):
	return x + y

def subtract(x,y):
	return x-y
			
def multiply (x,y):
	return x * y
		
def divide(x,y):
	return x / y
	
def power(x,y):
	return x ** y	
	
while True:
	time.sleep(1)
	print("📟 BASIC CALCULATOR 📟".center(36, "="))
	menu = input("\n  Choose an option:\n"
            "   1 ➤ Add\n"
            "   2 ➤ Subtract\n"
            "   3 ➤ Multily\n"
            "   4 ➤ Divide\n"
            "   5 ➤ Power\n"
        "   6 ➤ Quit\n→ ")
	
	if menu == "1":
		time.sleep(0.5)
		print("  Addition")
		num1 = float(input("  Enter number 1: "))
		num2 = float(input("  Enter number 2: "))
		print(f"  Answer: {add(num1,num2)}")
	
	elif menu == "2":
		time.sleep(0.5)
		print("  Subtraction")
		num1 = float(input("  Enter number 1: "))
		num2 = float(input("  Enter number 2: "))
		print(f"  Answer: {subtract(num1,num2)}")
		
	elif menu == "3":
		time.sleep(0.5)
		print("  Multiplication")
		num1 = float(input("  Enter number 1: "))
		num2 = float(input("  Enter number 2: "))
		print(f"  Answer: {multiply(num1,num2)}")
		
	elif menu == "4":
		time.sleep(0.5)
		print("  Division")
		num1 = float(input("  Enter number 1: "))
		num2 = float(input("  Enter number 2: "))
		if num2 == 0:
			print("  Cannot divide by zero")
		else:
			print(f"  Answer: {divide(num1,num2)}")
		
	elif menu == "5":
		time.sleep(0.5)
		print ("  Power")
		num = float(input("  Enter a number: "))
		pow = float(input(f"  {num} up to the power of: "))
		print(f"  {num} to the power of {pow} is: {power(num,pow)}")
	

	elif menu == "6":
		time.sleep(0.5)
		print ("  Good bye 👋")
		break				

	else:
		print ("  Invalid Number")

