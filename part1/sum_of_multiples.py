from functools import reduce

if __name__ == '__main__':
    INPUT = 1000

    wanted_numbers = filter(
        lambda i: True if (i % 3 == 0 or i % 5 ==0) else False,
        [i for i in range(1, INPUT+1)]
    )
    wanted_numbers = [i for i in wanted_numbers]
    
    ans = reduce(lambda acc, i: acc+i, wanted_numbers, 0)
    print(ans)
    