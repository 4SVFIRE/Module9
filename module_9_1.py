def apply_all_func(int_list, *functions):
    result = {}
    re={}
    for function in functions:
        try:
            result[function.__name__] = function(int_list)
        except TypeError as e:
            print(f'Ошибка выполнения функции {function.__name__}: {e}')
    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))