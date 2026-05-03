#!/bin/python3


dictionary = {
        "key1": [{"sub-llave": "valor1"}, {"test": "valor2"}, {"foo": "valor3"}]
}

print(dictionary["key1"][0]["sub-llave"])
print(dictionary["key1"][1]["test"])
print(dictionary["key1"][2]["foo"])
