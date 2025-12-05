a = {'a' : {'b': 4}}

print(a.get("b"))

if a.get("a"):
    print("OK")

if a.get("b"):
    print("notOK")