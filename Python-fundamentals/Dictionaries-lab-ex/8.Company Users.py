company_info = {}

input_data = input()

while not input_data == "End":
    company_name, employee_id = input_data.split(" -> ")
    if company_name not in company_info:
        company_info[company_name] = []
        if employee_id not in company_info[company_name]:
            company_info[company_name].append(employee_id)
    elif company_name in company_info and employee_id not in company_info[company_name]:
        company_info[company_name].append(employee_id)
    input_data = input()

sorted_info = sorted(company_info.items())
for company, key in sorted_info:
    print(company)
    for s in key:
        print(f"-- {s}")
