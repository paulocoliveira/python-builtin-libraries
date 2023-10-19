import configparser

# Initialize the ConfigParser
config = configparser.ConfigParser()

# Read the configuration file
config.read('config.ini')

# Retrieve a configuration value
url = config.get('Server', 'url')
print(f"The URL is: {url}")

# Update a configuration value
config.set('Server', 'url', 'https://www.lambdatest.com/selenium-playground/simple-form-demo')

# Retrieve a configuration value
url = config.get('Server', 'url')
print(f"The new URL is: {url}")

# Add a new section and option
config.add_section('Database')
config.set('Database', 'host', 'localhost')

# Retrieve updated configuration values
database_host = config.get('Database', 'host')
print(f"The Database Host is: {database_host}")

# Write the changes back to the configuration file
with open('config.ini', 'w') as configfile:
    config.write(configfile)
