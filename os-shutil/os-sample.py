import os

# Check if a file exists
file_exists = os.path.exists('sample-file.txt')
print(f"File Exists: {file_exists}")

# Create a directory and write a file
os.makedirs('test_directory', exist_ok=True)
with open('test_directory/sample.txt', 'w') as file:
    file.write('Sample content.')
