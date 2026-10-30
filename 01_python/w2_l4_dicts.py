# Week 2, Lesson 4: Dictionaries, one flight as a record

flight = {
    "airline": "DL",
    "number": 1287,
    "origin": "DTW",
    "destination": "ATL",
    "delay": 45,
}

print(flight)
print(flight["airline"], flight["number"])

flight["delay"] = 60 ## Update the delay value in the flight dictionary
flight['gate'] = "B12" ## Add a new key-value pair for the gate in the flight dictionary
print(flight)

print(flight.get("terminal")) ## This checks if there a terminal key is there in the dictionary and if it is not there then it will return None
print(flight.get("terminal", "unknown")) ##This checks if there a terminal key is there in the dictionary and if it is not there then it will return "unknown"

print("delay" in flight) ## This checks if there a delay key in the flight dictionary
print(len(flight)) ## This gives length of the dictionary
print(flight.keys()) ## This gives all the keys in the dictionary
print(flight.values()) ## This gives all the values in the dictionary


# Many flights = a list of dictionaries (this is basically a table)
flights = [
    {"airline": "DL", "number": 1287, "delay": 60},
    {"airline": "AA", "number": 999, "delay": 5},
]
print(flights[1]["airline"])
print(flights[0]["delay"] + flights[1]["delay"])
