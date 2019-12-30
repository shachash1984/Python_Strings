#!usr/bin/python
a = [1, 2, 3, 4]
#print(a[2:4])

a, b, *c = [1, 2, 3, 4]
#print(a, b, c)
d = [6, 5, 4]
d += c
#print(d)
c.extend(d)
#print(c)
while d:
    print("d Popped: " + str(d.pop()))
e = list(c)
f = e
while e:
    item = e.pop(0)
    print("e Popped: " + str(item))

del f[:2]
print("f: " + str(f))

list_of_names = """ido
shahar
hizu
boaz
""".splitlines()
list_of_names.remove('hizu')
print(list_of_names)

sorted_array = ["c", "a", 'b', 'z']
sorted_array.sort(reverse=True)
print(str(sorted_array))
num_list = ['4', '7', '2', '12', '5']
sorted_num_list = sorted(num_list, key=int)
print(str(sorted_num_list))


