#Assignment 3
#By Jose Fuentes 
#Q1: Meal recommendation program
# Prompt user for input
meal = input("What meal are you having (breakfast, lunch, or dinner)? ").lower()

# Using if-elif-else statements to recommend meals
if meal == "breakfast":
    print("How about some bacon and eggs?")
elif meal == "lunch":
    print("How about a chicken sandwich and a salad?")
elif meal == "dinner":
    print("How about some grilled salmon with vegetables?")
else:
    print("I only have recommendations for breakfast, lunch, or dinner.")

#Q2: Payroll program
wage = float(input("Enter the wage for the student: "))
hours = float(input("Insert hours worded by student: "))
gross_pay = wage * hours
#Using if-else for overtime:
if hours > 20:
    gross_pay = wage*hours*1.5
    print("The student worked over time and the gross pay is : ",gross_pay) 
elif hours <=20:
    gross_pay = wage*hours
    print("The student's gross pay is: ", gross_pay)

 #Q3: # Function to multiply the argument by 10
def times_ten():
    # Prompt user to input a number
    number = float(input("Insert number to calculate product: "))
    
    # Calculate the product
    product = number * 10
    
    # Display the result
    print(f"The product of {number} multiplied by 10 is: {product}")

times_ten()

#Q4: Find the errors, debug the program, and then execute to show the output.

def main():
    calories1 = float(input( "How many calories are in the first food?: "))
    calories2 = float(input( "How many calories are in the second food?: "))
    show_calories(calories1, calories2)

def show_calories(calories1, calories2):
    print("The total calories you ate today: ", format(calories1 + calories2, ".2f"))

main()
#Q5: 
def calculate_series():
    total = 0  # Initialize total to 0
    
    # Loop through numbers 1 to 30 and calculate the sum of the series
    for i in range(1, 31):
        total += i / (31 - i)  # Each term is i / (31 - i)
    
    # Display the total sum of the series:
    print(f"The total of the series is: {total:.2f}")

# Call the function to calculate and print the series sum
calculate_series()

#Q6: Write a function that computes the area of a triangle given its base and height.
def triangle_area():
    # Prompt the user to input base and height
    base = float(input("Enter the base of the triangle in inches: "))
    height = float(input("Enter the height of the triangle in inches: "))
    
    # Calculate the area of the triangle
    area = 0.5 * base * height
    
    # Print the result
    print(f"The area of the triangle is: {area:.2f}")

# Call the function
triangle_area()
