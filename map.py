# Create an empty map
my_map = {}

# Add key-value pairs to the map
my_map["name"] ="Aditya\n"" joshi"
my_map["age"] = 21
my_map["address"] = "Niko homes1"

# Retrieve the value associated with a key
print(my_map["name"])
print(my_map["age"])

# Remove a key-value pair from the map
del my_map["address"]

# Check if a key exists in the map
if "address" in my_map:
    print("The key 'address' is in the map.")
else:
    print("The key 'address' is not in the map.")

