def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [35, 'слово', [4, 5, 6]]
values_dict = {'a': 67, 'b': 'словарь', 'c': [6, 7, 8, 9]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [151, 'Street']
print_params(*values_list_2, 55)
