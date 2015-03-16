input = raw_input('What text would you like to convert to Binary?')
m = 'Your binary is:'


for index in input:
    binary = bin(ord(index))
    binary = binary[2:]
    binary = -len(binary) % 8 * '0' + binary
    m = m + ' ' + binary
    
print m
																								
    
    
    

