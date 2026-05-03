#!/bin/python3

dictionary = {
        "roy": [{"apodo1": "marikon"}, {"apodo2": "jotailo"}, {"apodo3": "mari-jotailo"}]
}

i = 0
for key, value in dictionary.items():
    for _ in range(len(value)):
        print(value[i])
        i += 1
