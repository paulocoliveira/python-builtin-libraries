import re

# Sample text containing URLs
sample_text = "Visit Python documentation website at https://docs.python.org for more information. To know more about LambdaTest, go to https://www.lambdatest.com."

# Define the URL pattern
url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+'

# Method 1: re.search()
search_result = re.search(url_pattern, sample_text)
if search_result:
    print(f"First URL found using re.search(): {search_result.group()}")

# Method 2: re.findall()
urls = re.findall(url_pattern, sample_text)
print("\nAll URLs found using re.findall():")
for url in urls:
    print(url)

# Method 3: re.match()
match_result = re.match(url_pattern, sample_text)
if match_result:
    print(f"\nFirst URL matched using re.match(): {match_result.group()}")

# Method 4: re.sub()
replaced_text = re.sub(url_pattern, 'REPLACED_URL', sample_text)
print(f"\nText after replacing URLs using re.sub():\n{replaced_text}")

# Method 5: re.compile()
pattern = re.compile(url_pattern)
compiled_result = pattern.findall(sample_text)
print(f"\nAll URLs found using re.compile() and pattern.findall():\n{compiled_result}")