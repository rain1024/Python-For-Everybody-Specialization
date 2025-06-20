import datetime

date_string = "2002-05-30T09:30:10Z"
# The 'Z' at the end of the string means UTC.
# We can parse this into a timezone-aware datetime object.
# fromisoformat is a good way to parse ISO 8601 strings.
# We replace 'Z' with '+00:00' to make it compatible.
date_object = datetime.datetime.fromisoformat(date_string.replace("Z", "+00:00"))


print(f"Date string: {date_string}")
print(f"Date object: {date_object}")
print(f"Timezone: {date_object.tzinfo}")
print(f"UTC offset: {date_object.utcoffset()}")
print(f"Year: {date_object.year}")
print(f"Month: {date_object.month}")
print(f"Day: {date_object.day}")
print(f"Hour: {date_object.hour}")
print(f"Minute: {date_object.minute}")
print(f"Second: {date_object.second}")
