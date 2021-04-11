mylist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[0:(int(len(mylist)/2))]
b = mylist[(int(len(mylist)/2)):]
print(a, b)
b.extend(a)
print(b)