import time

# Get the current time in seconds since January 1, 1970
current_time = time.time()

# Format the current time with commas and decimal places
# {} : This is a placeholder where the number will be inserted.
# :  : This is used to introduce the format specifications for the number.{:f} {:d}...
# ,  : This is used as a thousand separator.
# .4f: This is used to format the number as a floating point number with 4 digits after the decimal point.
formatted_time = "{:,.4f}".format(current_time)

# Format the current time in scientific notation
scientific_notation = "{:.2e}".format(current_time)

# Format the current date as "Month Day Year"
formatted_date = time.strftime("%b %d %Y")

# Print the formatted output
print("Seconds since January 1, 1970:", formatted_time, "or", scientific_notation, "in scientific notation")
print(formatted_date)
