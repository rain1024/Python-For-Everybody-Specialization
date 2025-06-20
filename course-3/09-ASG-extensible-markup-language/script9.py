import datetime

# The "Z" in an ISO 8601 timestamp like "2002-05-30T09:30:10Z"
# stands for "Zulu time", which is equivalent to Coordinated Universal Time (UTC).
# It indicates a zero UTC offset.

time_str = "2002-05-30T09:30:10Z"

# # For robust parsing across different Python 3 versions,
# # it's a good practice to replace 'Z' with '+00:00'.
# # Python 3.11+ `fromisoformat` handles 'Z' directly, but this ensures broader compatibility.
time_str = time_str.replace('Z', '+00:00')

try:
    # Parse the string into a timezone-aware datetime object
    dt_object = datetime.datetime.fromisoformat(time_str)

    print(f"Original time string: '{time_str}'")
    print(f"Parsed datetime object: {dt_object}")
    print(f"Timezone info: {dt_object.tzinfo}")
    print(f"UTC offset: {dt_object.utcoffset()}")

except ValueError as e:
    print(f"Error parsing time string: {e}")
