import json

# Loading JSON from a string
json_string = '{"name": "John Doe", "age": 30}'
data = json.loads(json_string)
print(data['name'])  # Output: John Doe

# Serializing an object to a JSON formatted string
person = {'name': 'Jane Smith', 'age': 25}
json_data = json.dumps(person)
print(json_data)  # Output: {"name": "Jane Smith", "age": 25}
