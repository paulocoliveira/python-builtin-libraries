from datetime import datetime, timedelta

# Get the current date and time
current_datetime = datetime.now()

# Parse a date string
date_str = '2023-10-17'
parsed_date = datetime.strptime(date_str, '%Y-%m-%d')

# Format a datetime object
formatted_date = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

# Calculate a duration
duration = current_datetime - parsed_date

# Add an example of using timedelta to represent a duration
duration_example = timedelta(days=5, seconds=3600)

# Add an example of using timedelta to represent a duration
date_adding_duration = current_datetime + duration_example

# Modify components of a datetime object
modified_datetime_2024 = current_datetime.replace(year=2024)

# Print results
print(f"Current Datetime: {current_datetime}")
print(f"Parsed Date: {parsed_date}")
print(f"Formatted Date: {formatted_date}")
print(f"Duration: {duration}")
print(f"Duration Example: {duration_example}")
print(f"Date Adding Duration: {date_adding_duration}")
print(f"Modified Datetime (Year 2024): {modified_datetime_2024}")