import unittest

def nested_object(object, key):
    res = object
    for i in key:
        res = res.get(i, None)
        if res is None:
            return None
    return res

class TestNestedObject(unittest.TestCase):
    def test_nested_object_success(self):
        actual = nested_object({"a":{"b":{"c":"d"}}},["a","b","c"])
        expected = "d"
        self.assertEqual(actual, expected)
    
    def test_nested_object_fsilure(self):
        actual = nested_object({"a":{"b":{"c":"d"}}},["a","b","c"])
        expected = "e"
        self.assertEqual(actual, expected)

    def test_nested_object_exception(self):
        actual = nested_object({"a":{" ":{"c":"d"}}},["a","b","c"])
        expected = "e"
        self.assertEqual(actual, expected)






