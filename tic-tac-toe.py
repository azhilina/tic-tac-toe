# write your code here
line = input()
# line = 'XXXOO__O_'
# line1 = 'XOXOXOXXO'
# line2 = 'XOOOXOXXO'
# line3 = 'XOXOOXXXO'
# line4 = 'XO_OOX_X_'
# line5 = 'XO_XO_XOX'
# line6 = '_O_X__X_X'
# line7 = '_OOOO_X_X'
# print(line)

print('---------')
i = 0
while i < 9:
   print('|',line[i],line[i + 1],line[i + 2],'|')
   i = i + 3
print('---------')

def place(c,inp):
    cond = False
    number = 3 * (int(c[0]) - 1) + (int(c[1]) - 1)
    if (inp[number] == "X" or inp[number] == 'O'):
        cond = True
    return cond
    
def nums(a, input):
    new_line = [1 if n == a else 0 for n in input]
    number = 0
    for i in new_line:
        number = number + i
    return number
    
step = True
while(step):
    k = input().split(' ')
    if (k[0] in ['1','2','3'] and k[1] in ['1','2','3']):
        if (not place(k, line)):
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
    
