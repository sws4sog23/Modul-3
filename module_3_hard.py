data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
sum_=0
spis=[]
v=spis
def sum_t(sp):
    global sum_
    global spis
    for s in sp:
        if type(s) is int:
            sum_+=s
        if type(s) is str:
            sum_+=len(s)
    return sum_
def calculate_structure_sum(*args):
    cal(args)
    return sum_t(v)
def cal(*args):
    for i in args:
        if isinstance(i, (int,str)):
            spis.append(i)
            return cal(args[1:])
        if isinstance(i, dict):
            i = list(i.items())
        for j in i:
           cal(j)


result = calculate_structure_sum(data_structure)
print(result)