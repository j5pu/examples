import collections

#####
def default_factory():
    return 'default value'


d = collections.defaultdict(default_factory, foo='bar')
print('d:', d)
print('foo =>', d['foo'])
print('bar =>', d['bar'])

#######
key = 'file'
item = 1
dict_set = collections.defaultdict(set)

dict_set[key].add(item)

#####
"""Using list as the default_factory, 
it is easy to group a sequence of key-value pairs into a dictionary of lists:"""
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)
...
sorted(d.items())

"""When each key is encountered for the first time, it is not already in the mapping; 
so an entry is automatically created using the default_factory function which returns an empty list. 
The list.append() operation then attaches the value to the new list. When keys are encountered again, 
the look-up proceeds normally (returning the list for that key) and the list.append() operation adds 
another value to the list. This technique is simpler and faster than an equivalent technique using dict.setdefault():"""
d = {}
for k, v in s:
    d.setdefault(k, []).append(v)
...
print(sorted(d.items()))


"""Setting the default_factory to int makes the defaultdict useful for counting
(like a bag or multiset in other languages):"""
s = 'mississippi'
d = collections.defaultdict(int)
for k in s:
    d[k] += 1

print(sorted(d.items()))

"""When a letter is first encountered, it is missing from the mapping, so the default_factory function calls int() 
to supply a default count of zero. The increment operation then builds up the count for each letter.

The function int() which always returns zero is just a special case of constant functions. A faster and more flexible 
way to create constant functions is to use a lambda function which can supply any constant value (not just zero):"""
def constant_factory(value):
    return lambda: value
d = collections.defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
print('%(name)s %(action)s to %(object)s' % d)


"""Setting the default_factory to set makes the defaultdict useful for building a 
dictionary of sets:"""

s = [('red', 1), ('blue', 2), ('red', 3), ('blue', 4), ('red', 1), ('blue', 4)]
d = collections.defaultdict(set)
for k, v in s:
    d[k].add(v)

print(sorted(d.items()))


