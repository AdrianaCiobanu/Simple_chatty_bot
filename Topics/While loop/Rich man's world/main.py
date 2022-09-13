sum_of_deposit = int(input())
interest = 0.071
max_amount = 700000
years = 0
while sum_of_deposit < max_amount:
    sum_of_deposit = sum_of_deposit + (sum_of_deposit * interest)
    years += 1
print(years)
