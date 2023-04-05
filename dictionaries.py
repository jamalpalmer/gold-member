var = {}

print(var)

print(type(var))

var2 = {"number":386}

print(var2)

var2["fruit"] = "apple"

print (var2)

var2["number"] = 493

print (var2)

print(dir(var))

print(list(var2.keys()))
print(list(var2.values()))

for k, v in var2.items():
    print(k, v)