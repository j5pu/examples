a = {1:2, 3:4}
print(a)
s = set()
s.add(tuple(a.items()))
print(tuple(a.items()))
print(s)

new_a = dict()
for tup in s:
    new_a = dict(tup)
    print(dict(tup))
    print(new_a)

print(new_a)