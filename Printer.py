#!/usr/bin/python
#print("Testing", 2, "Strings", True, sep=' \n$$\n ', end='End')
text = ' Shahar {} was here {}'.format('The king', 'today ')
print(text)
text = text.replace('here', 'there')
print(text)

#removes spaces in the beginning and end
print(text.strip())

# find returns index of substring
print(text[text.find('was'):])

#duplicate the string
print(text.strip()*2)

#counts the substring in the string
print(text.count('a'))

print(text.startswith(' Sha'))

#is the string composed of only letters (returns false if contains spaces as well)
print(text.isalpha())

#returns the sttring with first letter capitalized
print(text.strip().capitalize())

path = 'C:\\Visual\\OneVision\\Build.exe'

print(path[path.rfind('\\')+1:path.find('.exe')])

elements = path.split('\\')
elements.append('!')
print("".join(elements))
print("\n".join(dir(path)))
paragraph = """
This is a story
all about how
my life got flipped, turned upside down
"""
print(paragraph.splitlines())
