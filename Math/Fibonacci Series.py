i = raw_input('How many loops do you want? ')

try:
    i = int(i)
except:
    print('Please re-run the program and enter an integer')
    raise SystemExit()

x = 0
y = 1
total = 0
print x
print y

for t in range (1,i):
    total = x + y
    x = y
    y = total
    print total


