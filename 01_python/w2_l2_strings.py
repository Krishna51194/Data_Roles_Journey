# Week 2, Lesson 2: Strings, cleaning messy flight data

code = "DL1287"
airline_code = code[:2]
flight_number = code[2:]
print(airline_code, flight_number)
print(code[-1])

date = "2026-10-15"
year = date[:4]
month = date[5:7]
day = date[-2:]
print(year, month, day)

raw_airline = "  delta air lines  "
print(len(raw_airline))
clean_airline = raw_airline.strip().title()
print(clean_airline)
print(len(clean_airline))

price_text = "$129.99"
price = float(price_text.replace("$", ""))
print(price, type(price))

route = "DTW-ATL-LAX"
stops = route.split("-")
print(stops)

print(f"Flight {airline_code}{flight_number} on {date} costs ${price}")

messy = "  united "

messy.strip()
print(f"[{messy}]")


print(code[2:50])
## print(code[10])

delays = [45, 5, 120]
delays.append(30)
result = delays.append(60)
print(result)
print(delays)