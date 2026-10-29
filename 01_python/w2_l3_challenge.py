delays = [45, 0 , 120, 15, 30, 75]

delays.append(200)
print(delays)

delays.remove(0)
print(delays)

print(len(delays))
print(sum(delays))

avg_delay = round(sum(delays) / len(delays), 1)
print(avg_delay)

print(f"worst delay: {max(delays)} and best delay: {min(delays)}")
print(delays)
print(sorted(delays, reverse=True)[:3])

print(15 in delays)

route = "DTW-ATL-LAX-SEA"

each_airpot = route.split("-")
print(each_airpot)
first_airport = each_airpot[0]
last_airport = each_airpot[-1]
print(f"first airport: {first_airport} and last airport: {last_airport}")
between_airports = each_airpot[1:-1]
print(f"between airports: {between_airports} and {len(between_airports)}")
