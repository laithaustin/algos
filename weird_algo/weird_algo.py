def weird_algo(num):
    if (num == 1):
        print(num)
        return
    print(num, end=' ')
    num = int(num / 2) if (num % 2) == 0 else int((num * 3) + 1)
    weird_algo(num)

if __name__ == '__main__':
    num = int(input(""))
    weird_algo(num)
