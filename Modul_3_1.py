calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(st):
    count_calls()
    st_ = (len(st), st.upper(), st.lower())
    return st_

def is_contains(st, sp):
    count_calls()
    st.lower()
    sp_ = [x.lower() for x in sp]

    if st in sp_:
        fl = True
    else:
        fl = False
    return fl

print(string_info('caT'))
print(string_info('VolKi'))
print(is_contains('aa', ['aA', 'Ga', 'wHw']))
print(is_contains('aB', ['aA', 'Ga', 'wHw']))
print(calls)
