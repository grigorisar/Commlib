import numpy as np
from kam import pam_constellation
from scipy import special
import textwrap as tw


def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

def Qfunction(x):
    return 0.5 * special.erfc(x/np.sqrt (2.0))

def gray_code(m): 
    if m==1:
        g = ['0','1']
    elif m>1:
        gs = gray_code(m-1)
        gsr = gs[::-1]
        gs0 = ['0' + x for x in gs] 
        gs1 = ['1' + x for x in gsr] 
        g= gs0 + gs1
    return g

def pad(t, arr):
    pad_times = 0
    pad = ''
    if len(binary) % t != 0 :
        pad_times = (len(arr) % 3) 
        pad = ''
    for i in range(1, pad_times):
        pad = pad + '0'

    arr = arr + pad
    return arr
    
def graycode(leng, binary):
    temp = binary
    for i in range(1, leng):
        first_half = temp
        sec_half = temp
        first_half = ['0' + bit for bit in first_half]
        sec_half = ['1' + bit for bit in sec_half] 
        temp = first_half + sec_half
    return temp

# name = "Grigoris Arfanis"
# # print (toBinary(name))
# # print (len(gray_code(8)))

# pam = pam_constellation(M=2,title="This is a test")
# pam.set_symbols(toBinary(name))
# pam.set_gray_bits(m=4)
# pam.plot()




name = input("Enter name:").title()
surname = input("Enter surname:").title()
chars = list(name + surname) 

# print(string2bin(chars))

# print(chars)

ords = [ord(character) for character in chars]
# print([bin(b).replace('b', '', 1)  for b in ords])

binary_list = [bin(b).replace('b', '', 1)  for b in ords]

binary = "".join(binary_list)

bin2 = tw.wrap(binary, 1)

bin2 = [int(char) for char in bin2]
print(bin2)

gray_len1 = [0] * len(bin2)  
# iterate through each bit ignoring first one applying xor, current new bit = old previous bit XOR old current bit
for idx in range(1, len(bin2)):
    prev = bin2[idx - 1]
    # print(f'prev = '+ str(prev))
    curr = bin2[idx]
    # print(f'curr = '+ str(prev))

    if prev + curr == 1 :
        gray_len1[idx] = 1
    else:
        gray_len1[idx] = 0
        
    # print(f'new for pos ' + str(idx) + ' = '+ str(bin2[char]))

print(gray_len1)



binary = pad(2, binary)
gray_len2 = graycode(2, binary)
print(gray_len2)


binary = pad(3, binary)
gray_len3 = graycode(3, binary)
print(gray_len3)

binary = pad(4, binary)
gray_len4 = graycode(4, binary)
print(gray_len4)
