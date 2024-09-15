import sys



int1 = int(sys.argv[1])
int2 = int(sys.argv[2])

sum = int(int1) + int(int2)

if  sum <= 0:
    print('You have chosen the path of destitution')

elif sum <= 100:
    print('You have chosen the path of plenty')
else:
    print("You have chosen the path of excess")