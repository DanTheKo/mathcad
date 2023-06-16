def sum_all_numbers(file, n):
    f = open(file, 'r')
    _numbers = []
    for i in range(n):
        temp = f.readline()
        _numbers.append(int(temp[0:50]))
    return _numbers


numbers = sum_all_numbers('big.txt', 100)
print(str(sum(numbers))[0:10])
