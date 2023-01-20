# write your code here

import math

line = input()
# line = 'XOXOOXXXO'

print('---------')
i = 0
while i < 9:
    print('|',line[i],line[i + 1],line[i + 2],'|')
    i = i + 3
print('---------')

# this function returns the number of user inputs on the grid
def nums(a, input):
    new_line = [1 if n == a else 0 for n in input]
    number = 0
    for i in new_line:
        number = number + i
    return number
    
x = nums('X',line)
o = nums('O',line)
l = math.fabs(nums('X',line)-nums('O',line))

# this function returns the winner
def win(a, input):
    nl = [1 if n == a else 0 for n in input]
    if ((nl[0] + nl[1] + nl[2] == 3) or
    (nl[3] + nl[4] + nl[5] == 3) or
    (nl[6] + nl[7] + nl[8] == 3) or
    (nl[0] + nl[3] + nl[6] == 3) or
    (nl[1] + nl[4] + nl[7] == 3) or
    (nl[2] + nl[5] + nl[8] == 3) or
    (nl[0] + nl[4] + nl[8] == 3) or
    (nl[2] + nl[4] + nl[6] == 3)):
        return True

win('X', line)
win('O', line)

if (l > 1):
    print('Impossible')
elif(win('X', line) and win('O', line)):
    print('Impossible')
elif (win('X', line)):
    print('X','wins')
elif (win('O', line)):
    print('O','wins')
elif ((x + o) < 9):
    print('Game not finished')
elif ((x + o) == 9):
    print('Draw')
