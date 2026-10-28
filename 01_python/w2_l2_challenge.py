raw = " dl1287 , 2026-10-15 , ATLANTA , $129.99 "

split_raw = raw.split(",")

print(split_raw)

flight_details = split_raw[0].strip().upper()
print(flight_details)
flight_code = flight_details[:2]
flight_number = int(flight_details[2:])
print(flight_code, flight_number, type(flight_number))

date = split_raw[1].strip()
print(date)

city = split_raw[2].strip().title()
print(city)

price = float(split_raw[3].strip().replace("$", ""))
print(price)

month = date[5:7]
print(month)

print(f"{flight_code} {flight_number} flew to {city} in month {month} for ${price}")