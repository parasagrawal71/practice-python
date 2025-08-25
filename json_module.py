import json

print("\n")
data = {
    "name": "Alice",
    "age": 30,
    "is_admin": True,
    "skills": ["Python", "Django", "AWS"]
}

json_data = json.dumps(data) # Convert Python dict to JSON
print(json_data)

print(json.dumps(data, indent=4))   # Pretty print with indentation
print(json.dumps(data, sort_keys=True))  # Sort keys alphabetically


json_str = '{"name": "Bob", "age": 25, "is_admin": false}'
python_obj = json.loads(json_str) # Convert JSON string → dict
print(python_obj)

# ################################################################
from datetime import datetime

# How it is working
def serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError("Type not serializable")

print(json.dumps({"time": datetime.now()}, default=serializer))


print("\n")