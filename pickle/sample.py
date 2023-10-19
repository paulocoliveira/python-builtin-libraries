import pickle

# Test case data
test_case_data = {
    'test_name': 'Login Test',
    'browser': 'Firefox',
    'status': 'Passed',
    'duration': 120
}

# Serialize and write to a file
with open('test_case_data.pkl', 'wb') as file:
    pickle.dump(test_case_data, file)

# Deserialize and retrieve data
with open('test_case_data.pkl', 'rb') as file:
    loaded_data = pickle.load(file)

# Print the retrieved data
print("Retrieved Test Case Data:")
print(loaded_data)
