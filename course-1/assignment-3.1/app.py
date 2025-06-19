hrs = input("Enter Hours:")
h = float(hrs)

rate_input = input("Enter Rate:")
r = float(rate_input)

if h > 40:
    regular_pay = 40 * r
    overtime_hours = h - 40
    overtime_pay = overtime_hours * r * 1.5
    pay = regular_pay + overtime_pay
else:
    pay = h * r
print(pay)