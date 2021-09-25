
persons = [
 {
 "name": "John",
 "age": 36,
 "country": "Norway"
 },
 {
 "name": "Bob",
 "age": 36,
 "country": "Norway"
 }
]

persons = sorted(
				sorted(
						sorted(persons, key = lambda x: x["age"]),
                     	key = lambda x: x["name"]),
                key =  lambda x: x["country"]
			)

print(persons)