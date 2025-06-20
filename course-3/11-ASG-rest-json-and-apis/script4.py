import json

text = """{ "id" : "001",
  "x" : "2",
  "name" : "Chuck"
}"""

a = json.loads(text)

print(a)

print(type(a))


