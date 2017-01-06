one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100

print bin(1)
for x in range(2,6):
    print bin(x)

shift_right = 0b1100
shift_left = 0b1

shift_right= shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right)
print bin(shift_left)

print bin(0b1110 & 0b101)

print bin(0b1111)

def check_bit4(value):
    mask = 0b1000
    if (mask & value)>0:
        return "on"
    else:
        return "off"

a = 0b10111011
mask = 0b100
a = a | mask
print bin(a)

a = 0b11101110
mask = 0b11111111
print bin(a^mask)

def flip_bit(number, n):
    mask = 0b1 << n-1
    result = number ^ mask
    return bin(result)