import sys
if len(sys.argv) ==2:
    script_name=sys.argv[0]
    salary=sys.argv[1]
    print("user provides values")
else:
    script_name=sys.argv[0]
    salary="50000"
    print("user does not provide values")
bonus=0.1*int(salary)
total_salary=int(salary)+bonus
print("Script Name:",script_name)
print("Salary:",salary)
print("Bonus:",bonus)
