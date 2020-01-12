def number(num):
    f_num = num
    if(num >= 10000):
        f_num = f_num + int(num/10000)
        num = num % 10000;
    if(num >= 1000):
        f_num = f_num + int(num/1000)
        num = num % 1000;
    if(num >= 100):
        f_num = f_num + int(num/100)
        num = num % 100;
    if(num >= 10):
        f_num = f_num + int(num/10)
        num = num % 10;
    if(num >= 1):
        f_num = f_num + num

    return f_num

mylist = [1 for i in range(10001)]

for i in range(10001):
    if(number(i)<10001):
        mylist[number(i)] = 0

for i in range(10001):
    if(mylist[i] == 1):
        print(i)


