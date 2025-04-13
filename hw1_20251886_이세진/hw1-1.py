# Problem 1 Skeleton
salary = int(input("Enter the starting salary: "))
save_percentage= float(input("Enter the percent of your salary to save: "))# Your code goes here
home_cost = int(input("Enter the cost of your dream home: "))# Your code goes here
salary_increase_rate = float(input("Enter the semi annual raise, as a decimal: "))# Your code goes here

annual_interest_rate=0.043

total_savings = 0 # Your code goes here
target_savings = home_cost*0.25 # Your code goes here
monthly_interest_rate = annual_interest_rate/12 # Your code goes here

required_months = 0

while total_savings < target_savings:
    total_savings += total_savings * monthly_interest_rate
    total_savings = total_savings + salary/12 * save_percentage
    required_months += 1
    if required_months % 6 == 0:
        salary = salary * (1 + salary_increase_rate)
    

print(f'Number of months: {required_months}')