import string

# Create a template string
template = string.Template('$test_name has $status')

# Substitute values using a dictionary
result = template.substitute(test_name='Test 1', status='PASSED')

# Safe substitution with missing values
safe_result = template.safe_substitute(test_name='Test 2')

# Capitalize words in a string
capitalized_string = string.capwords('all tests of this test suite has passed')

# Format a string using Formatter
formatted_string = string.Formatter().vformat("{}, {}!", ["Visual", "test"], {})

# Parse a format string
parsed_format = list(string.Formatter().parse("{:.2f}"))

# Get the value of a field
field_value = string.Formatter().get_field('0', ["Integration", "test"], {})

# Print the outcomes of each operation
print(f"Result after substitution: {result}")
print(f"Safe result after substitution: {safe_result}")
print(f"Capitalized string: {capitalized_string}")
print(f"Formatted string: {formatted_string}")
print(f"Parsed format: {parsed_format}")
print(f"Field value: {field_value}")