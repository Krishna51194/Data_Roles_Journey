delays = [45, 5, 120, 0, 30]
print(delays)
print(delays[0], delays[-1], delays[1:3])

print(len(delays), sum(delays), max(delays), min(delays))

avg_delays = sum(delays) / len(delays)
print(avg_delays)

delays.append(15)
print(delays)

print(sorted(delays))
print(delays)

delays.sort(reverse=True)
print(delays)

print(120 in delays)

flight_numbers_text = ["1287", "999", "45"]
print(sorted(flight_numbers_text))

flight_numbers = [1287, 999, 45]
print(sorted(flight_numbers))

route = "DTW-ATL-LAX".split("-")
print(route, len(route))

delays.sort()
print(delays)
print(len(delays))