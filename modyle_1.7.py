#1
my_dick = {'Ivan': 56, 'Maks': 34, 'Nikolay': 45}
print(my_dick)
print(my_dick['Ivan'])
print(my_dick.get('YY'))
my_dick.update({'Qwert': 34567, 'dvdjcsgcv': 348})
print(my_dick)
my_dick.pop('Ivan')
print(my_dick)
#2
my_set = set([1, 2, 2, 'qwe', 'wer', 'qwe', True])
print(my_set)
my_set.update([345, 'tyu'])
print(my_set)
my_set.discard(2)
print(my_set)