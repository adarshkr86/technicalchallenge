def nested_object(object, key):
    res = object
    for i in key:
        res = res.get(i, None)
        if res is None:
            return None
    return res

print(nested_object({"a":{"b":{"c":"d"}}},["a","b","c"]))
print(nested_object({"x":{"y":{"z":"a"}}},["x","y","z"]))



