#!/usr/bin/python
test_dict = dict()
test_dict['a'] = 11
test_dict['b'] = 22
dict2 = {'c': 55, 'b': "shake"}
print("a keys: " + str(test_dict.keys()))
print("b values: " + str(dict2.values()))
test_dict.update(dict2)
print("a.update: " + str(test_dict))

dict3 = dict()
for key, value in test_dict.items():
    dict3[value] = key

#print("switched dict: " + str(dict3))

