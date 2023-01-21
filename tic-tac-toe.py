# write your code here

import math

# line = input()
# line = 'XOXOOXXXO'
line = '         '

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

# this function takes c(the list of two coodinates) and the list of values as a parameter
# and returns true if this coordinate is occupied with 'X' or 'O'
def place(c,inp):
    cond = False
    number = 3 * (int(c[0]) - 1) + (int(c[1]) - 1)
    if (inp[number] == "X" or inp[number] == 'O'):
        cond = True
    return cond

exit_line = line    

finish = True

while(finish):
    step = True
    while(step):
        k = input().split(' ')
        if (k[0] in ['1','2','3'] and k[1] in ['1','2','3']):
            if (not place(k, exit_line)):
                step = False
                number = 3 * (int(k[0]) - 1) + (int(k[1]) - 1)
                exit_line = []
                l = 0
                while (l < 9):
                    if l == number:
                        exit_line.append('X')
                        l = l + 1
                    else:
                        exit_line.append(line[l])
                        l = l + 1
            else:
                print('This cell is occupied! Choose another one!')
        elif (k[0].isdigit() and k[1].isdigit()):
            print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')


    print('---------')
    i = 0
    while i < 9:
        print('|',exit_line[i],exit_line[i + 1],exit_line[i + 2],'|')
        i = i + 3
    print('---------')

    x = nums('X',exit_line)
    o = nums('O',exit_line)
    l = math.fabs(nums('X',exit_line)-nums('O',exit_line))

    line = exit_line
    if (win('X', exit_line)):
        print('X','wins')
        break
    elif (win('O', exit_line)):
        print('O','wins')
        break
    elif ((x + o) == 9):
        print('Draw')
        break

    step = True
    while(step):
        k = input().split(' ')
        if (k[0] in ['1','2','3'] and k[1] in ['1','2','3']):
            if (not place(k, exit_line)):
                step = False
                number = 3 * (int(k[0]) - 1) + (int(k[1]) - 1)
                exit_line = []
                l = 0
                while (l < 9):
                    if l == number:
                        exit_line.append('O')
                        l = l + 1
                    else:
                        exit_line.append(line[l])
                        l = l + 1
            else:
                print('This cell is occupied! Choose another one!')
        elif (k[0].isdigit() and k[1].isdigit()):
            print('Coordinates should be from 1 to 3!')
        else:
            print('You should enter numbers!')


    print('---------')
    i = 0
    while i < 9:
        print('|',exit_line[i],exit_line[i + 1],exit_line[i + 2],'|')
        i = i + 3
    print('---------')

    x = nums('X',exit_line)
    o = nums('O',exit_line)
    l = math.fabs(nums('X',exit_line)-nums('O',exit_line))
    line = exit_line

    if (win('X', exit_line)):
        print('X','wins')
        break
    elif (win('O', exit_line)):
        print('O','wins')
        break
    elif ((x + o) == 9):
        print('Draw')
        break
