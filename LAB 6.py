#Instructions
#The rules for simple tax calculation is as follows:
#Personal allowance:		£11,850	 
#0 to 34,500 			taxed at 20%		
#34,501 to 150,000 		taxed at 40%		
#Over 150,000 			taxed at 45%		

#Step-by-Step Instructions:
#1.	Add a new file: tax.py and make it the startup file.
#2.	Create a function called getIncomeTax()
#3.	Calculate the income tax based on the simple tax calculation rules as seen above.
#Tip: You'll need to pass the salary to this function. Use a parameter called salary and base your calculations on the value held by the salary parameter.
#4.	After the calculation is finished you can return the tax amount.
#5.	In the main part of your code, just below where you defined the function, 
#write code to call getIncomeTax() and print the returned value. 
#To test your code, pass different values to the function to test its functionality.

def getIncomeTax(salary):
    if salary < 11850:
        return 0
    elif salary >= 11850 and salary <= 34500:
        return (salary - 11850) * 0.2
    elif salary >= 34501 and salary <= 150000:
        return 4530 + ((salary - 34500) * 0.4)
    else:
        return 50370 + ((salary - 150000) * 0.45)
    
salary = 85000
tax_amount = getIncomeTax(salary)

print(f"You will pay {tax_amount} for salary £{salary} is £{salary}") 
    