import locale

# Set the locale to 'en_US.UTF-8'
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Get the LC_MONETARY locale
lc_monetary_locale = locale.getlocale(locale.LC_MONETARY)

# Perform currency formatting
currency_format = locale.currency(1000.50, symbol=True, grouping=False)

# Use format_string
formatted_string = locale.format_string('%d', 12345, grouping=True)

# Use str
string_locale = locale.str(locale.LC_MONETARY)

# Use normalize
normalized_locale = locale.normalize('fr_FR.UTF-8')

# Reset LC_MONETARY to original value
locale.setlocale(locale.LC_MONETARY, lc_monetary_locale)

# Explanation for the output
print(f"LC_MONETARY Locale: {lc_monetary_locale}")
print(f"Currency Format: {currency_format}")
print(f"Formatted String: {formatted_string}")
print(f"String Locale: {string_locale}")
print(f"Normalized Locale: {normalized_locale}")
