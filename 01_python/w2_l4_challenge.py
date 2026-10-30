flight = {"airline": "ua", "number": "0456", "origin": "ORD", "delay": 20}

flight["airline"] = flight["airline"].upper()
print(flight["airline"])

flight["destination"] = "DEN"
print(flight)

flight["delay"] = flight["delay"] + 25
print(flight['delay'])

print(flight.get("terminal", "Not assigned"))

print("delay" in flight)

print(f"{flight["airline"]} {flight["number"]} from {flight["origin"]} to {flight["destination"]} delayed {flight["delay"]} min")