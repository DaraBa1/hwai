a = 17
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)

print(2 ** 10)
print(10 ** 3)

price = 249.99
count = 3
print(price * count)

print(type(7 / 2))
print(type(7 // 2))
print(type(7.0 // 2))

name = "Python"
print(name * 3)

text = "Привіт, " + "світ!"
print(text)

students = 28
desks = 6
print(students // desks)
print(students % desks)

seconds = 3725
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remainder_seconds = seconds % 60
print(hours)
print(minutes)
print(remainder_seconds)

minutes = 150
hours = minutes // 60
remainder_minutes = minutes % 60
print(hours)
print(remainder_minutes)

c = 36.5
f = c * 9 / 5 + 32
print(f)

rect_a = 12.5
rect_b = 8
area_rect = rect_a * rect_b
perimeter = 2 * (rect_a + rect_b)
print("Площа:", area_rect)
print("Периметр:", perimeter)

r = 7
pi = 3.14159
area_circle = pi * r ** 2
length = 2 * pi * r
print("Площа кола:", area_circle)
print("Довжина кола:", length)

price = 1200
discount = 15
discount_amount = price * discount / 100
final_price = price - discount_amount
print("Сума знижки:", discount_amount)
print("Фінальна ціна:", final_price)

salary = 25000
tax = 19.5
tax_amount = salary * tax / 100
net_salary = salary - tax_amount
print("Сума податку:", tax_amount)
print("Зарплата на руки:", net_salary)

speed = 90
time = 2.5
distance = speed * time
print("Відстань:", distance, "км")

a_num = 10
b_num = 11
c_num = 8
average = (a_num + b_num + c_num) / 3
print("Середнє арифметичне:", average)

n = 7
print(n % 2)

n = 473
print(n % 10)

hundreds = n // 100
tens = (n // 10) % 10
ones = n % 10
print("Сотні:", hundreds)
print("Десятки:", tens)
print("Одиниці:", ones)

n_three_digit = 859
hundreds = n_three_digit // 100
tens = (n_three_digit // 10) % 10
ones = n_three_digit % 10
sum_digits = hundreds + tens + ones
print(sum_digits)

x_str = "5"
y_str = "3"
print(x_str + y_str)

x_int = int(x_str)
y_int = int(y_str)
print(x_int + y_int)

float_val = 9.99
result = int(float_val)
print(result)

print(True + True + True)
print(True * 10)

swap_a = 5
swap_b = 10
swap_a = swap_a + swap_b
swap_b = swap_a - swap_b
swap_a = swap_a - swap_b
print(swap_a)
print(swap_b)

deposit = 10000
rate = 0.12
years = 3
total_amount = deposit * (1 + rate) ** years
print(total_amount)

print("-" * 20)
print("Результат: " + str(2 ** 20))