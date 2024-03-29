import time

### By default data type return of timestamp is string.

timestamp = time.strftime('%H:%M:%S')
print(timestamp)

timestamp = time.strftime('%H')
print(timestamp)

timestamp = time.strftime('%M')
print(timestamp)

timestamp = time.strftime('%S')
print(timestamp)

# https://docs.python.org/3/library/time.html#time.strftime

timestamp = time.strftime('%a') # Locale’s abbreviated weekday name.
print(timestamp)

timestamp = time.strftime('%A') # Locale’s full weekday name.
print(timestamp)

timestamp = time.strftime('%b') # Locale’s abbreviated month name.
print(timestamp)

timestamp = time.strftime('%B') # Locale’s full month name.
print(timestamp)

timestamp = time.strftime('%c') # Locale’s appropriate date and time representation.
print(timestamp)

timestamp = time.strftime('%d') # Day of the month as a decimal number [01,31]
print(timestamp)

timestamp = time.strftime('%H') # Hour (24-hour clock) as a decimal number [00,23]
print(timestamp)

timestamp = time.strftime('%I') # Hour (12-hour clock) as a decimal number [01,12]
print(timestamp)

timestamp = time.strftime('%j') # Day of the year as a decimal number [001,366]
print(timestamp)

timestamp = time.strftime('%m') # Month as a decimal number [01,12]
print(timestamp)

timestamp = time.strftime('%M') # Month as a decimal number [01,12]
print(timestamp)

timestamp = time.strftime('%p') # Locale’s equivalent of either AM or PM
print(timestamp)

timestamp = time.strftime('%S') # Second as a decimal number [00,61]
print(timestamp)

timestamp = time.strftime('%U') # Week number of the year (Sunday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Sunday are considered to be in week 0.
print(timestamp)

timestamp = time.strftime('%w') # Weekday as a decimal number [0(Sunday),6].
print(timestamp)

timestamp = time.strftime('%W') # Week number of the year (Monday as the first day of the week) as a decimal number [00,53]. All days in a new year preceding the first Monday are considered to be in week 0.
print(timestamp)

timestamp = time.strftime('%x') # Locale’s appropriate date representation.
print(timestamp)

timestamp = time.strftime('%X') # Locale’s appropriate time representation.
print(timestamp)

timestamp = time.strftime('%y') # Year without century as a decimal number [00,99].
print(timestamp)

timestamp = time.strftime('%Y') # Year with century as a decimal number.
print(timestamp)

timestamp = time.strftime('%z') # Time zone offset indicating a positive or negative time difference from UTC/GMT of the form +HHMM or -HHMM, where H represents decimal hour digits and M represents decimal minute digits [-23:59, +23:59].
print(timestamp)

timestamp = time.strftime('%Z') # Time zone name (no characters if no time zone exists). Deprecated.
print(timestamp)

timestamp = time.strftime('%%') # Year with century as a decimal number.
print(timestamp)

timestamp = time.strftime('%c') # Microseconds as a decimal number [000000,999999]
print(timestamp)


