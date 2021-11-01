"""Demonstrations of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Intialize to an empty dictionary 
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal represention
print(schools)

# Access a value by its keeep -- "lookup"
print(f"UNC has {schools['UNC']} students")

# Remove a key value pair from a dictionary
# by its key
schools.pop("Duke")

# Test for the existence of a key 
is_duke_present: bool = "Duke" in schools 
print(f"Duke is present:{is_duke_present}")

# update / Reassign a key-value pair 
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Domonstration of dictionary literals

# Empty dictionary literal
schools = {}  # Same as dict()

# ALternatively, initialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

# what happens when a key does not exist? 
print(schools["UNCC"])
