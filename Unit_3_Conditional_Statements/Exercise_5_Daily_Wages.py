# Enter time on shift, end shift.
# Calculate and print daily wages for workers, knowing that the hourly wage before 12 noon is 30.000 VND and after 12 noon is 40.000 VND. 
# The earliest on shift time is 6:00 and the latest end shift time is 18:00

on_shift_time = eval(input("Enter the on shift time: "))
end_shift_time = eval(input("Enter the end shift time: "))

wage_before_12 = 30000
wage_after_12 = 40000

if (on_shift_time < 6):
    on_shift_time = 6
if (end_shift_time > 18):
    end_shift_time = 18
if (on_shift_time < 12):
    if (end_shift_time > 12):
        total_wage = (end_shift_time - on_shift_time) * wage_before_12
    else:
        total_wage = (12 - on_shift_time) * wage_before_12 + (end_shift_time - 12) * wage_after_12
else:
    total_wage = (end_shift_time - on_shift_time) * wage_after_12

print("Total wage =", total_wage)
