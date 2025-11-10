n = 43261596
binary_num = bin(n)
# remove first bits
binary_num = binary_num[2:]
bin_len = len(binary_num)
padding = ""
# add extra bits to 32 bit num
for i in range(0,(32-bin_len)):
    padding = padding + "" + "0"
binary_num = padding + "" + binary_num

# reverse order
reversed = []
for bit in binary_num:
    reversed.insert(0,bit)
result = ''.join(reversed)
int_result = int(result,2)
print(reversed)
print(binary_num)