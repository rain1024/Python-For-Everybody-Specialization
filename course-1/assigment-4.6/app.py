def computepay(h, r):
    if h > 40:
        regular_pay = 40 * r
        overtime_pay = (h - 40) * r * 1.5
        total_pay = regular_pay + overtime_pay
    else:
        total_pay = h * r
    return total_pay

hrs = float(input("Enter Hours:"))
r = float(input("Enter Rate:"))
p = computepay(hrs, r)
print("Pay", p)