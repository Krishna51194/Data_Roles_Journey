# Week 2, Lesson 1: Values and types - challenge, using flight data

f1_fare = "250"
f2_fare = "180.50"
f3_fare = "99"

f1_delay_minutes = 30
f2_delay_minutes = 5
f3_delay_minutes = 50

f1_int_fare = int(f1_fare)
f2_float_fare = float(f2_fare)
f3_int_fare = int(f3_fare)

total_fare = f1_int_fare + f2_float_fare + f3_int_fare

print(total_fare)
print(type(total_fare))

is_f1_delayed = f1_delay_minutes > 15
is_f2_delayed = f2_delay_minutes > 15
is_f3_delayed = f3_delay_minutes > 15

total_delays = is_f1_delayed + is_f2_delayed + is_f3_delayed
print(total_delays)