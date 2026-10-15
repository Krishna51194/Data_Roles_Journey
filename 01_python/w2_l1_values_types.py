# Week 2, Lesson 1: Values and types, using flight data

airline = "Delta"
flight_number = 1287
fare = 129.99
delay_minutes = 45
is_delayed = delay_minutes > 15
gate = None

print(airline, flight_number)
print(type(fare))
print(type(delay_minutes))
print(type(is_delayed))
print(type(gate))

fare_text = "120"
print(fare_text + "5")
print(int(fare_text) + 5)
print(int("Delta"))