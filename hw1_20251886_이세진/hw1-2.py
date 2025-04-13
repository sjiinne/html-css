# Problem 2 (Skeleton)


def calculate_savings(salary, save_percentage, annual_interest_rate=0.04, years=3, salary_increase_rate=0.07):
    current_savings = 0 # Your code goes here
    montly_interest_rate = 0.04 / 12# Your code goes here

    for month in range(years * 12):
        current_savings += current_savings * 0.04 / 12
        current_savings += ( salary / 12 )* save_percentage

        if month % 6 == 5:
            salary += salary * 0.07

    return current_savings

def bisection_search(salary, target_savings=250000, acceptable_diff=100):
    current_diff = 100000 # Initial value(Any large number)
    upper_bound = 1.0# Your code goes here
    lower_bound = 0.0# Your code goes here
    current_savings = 0
    current_step = 0

    while abs(target_savings - current_savings) > acceptable_diff:
        
        save_percentage = (upper_bound + lower_bound) / 2# Your code goes here
        current_savings = calculate_savings(salary, save_percentage)
        current_diff = target_savings - current_savings# Your code goes here
        
        if target_savings > current_savings:
            lower_bound = save_percentage# Your code goes here
        else:
            upper_bound = save_percentage# Your code goes here
        
        current_step += 1
        
        if current_step > 100:
            break # To prevent infinite loop
    return save_percentage, current_savings, current_step

salary = int(input("Enter the starting salary: "))
save_percentage, current_savings, current_step = bisection_search(salary)# Your code goes here


"""
DO NOT CHANGE BELOW.
"""
current_savings = 0
annual_interest_rate=0.04
required_months = 0
salary_increase_rate = 0.07
target_savings = 250000
acceptable_diff= 100

while current_savings < target_savings:
    montly_savings = (salary / 12) * save_percentage
    current_savings += current_savings * annual_interest_rate / 12
    current_savings += montly_savings
    if required_months % 6 == 5:
        salary += salary * salary_increase_rate
    required_months += 1
    if required_months == 36:
        break

if abs(current_savings - target_savings) <= acceptable_diff:
    print(f"Best savings rate: {save_percentage:0.4f}, steps: {current_step}")
else:
    print("It is not possible to pay the down payment in three years.")