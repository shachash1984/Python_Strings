#!/usr/bin/python
def reverser(list_of_100):
    return sorted(list_of_100, key=int, reverse=True)


test_list = list(range(0, 101))
test_list.sort()

print(reverser(test_list))
