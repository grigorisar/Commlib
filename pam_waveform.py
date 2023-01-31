import numpy as np
from kam import pam_constellation
from scipy import special
import textwrap as tw
from scipy import signal as sig
import matplotlib.pyplot as plt

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

    while len(arr) % t != 0:
        arr += '0'
    return arr
    
def graycode(length, binary):
    temp = binary
    first_half = temp.copy()
    sec_half = temp[::-1].copy()
    first_half = ['0' + bit for  bit in first_half ]
    sec_half = ['1' + bit for bit in sec_half] 
    temp = first_half + sec_half

    return temp

def to_dec(arr):
    return [int(i, 2) for i in arr]

def to_str(arr):
    return [str(i) for i in arr]

def symbols(m):
    list = []
    for k in range(0, m+1):
        list.append(2*k -m +1)
    return list

def match(com, binlist):
    temp = []
    for i in binlist:
        temp.append(com[i])
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

#get ascii code for each character given from user
ords = [ord(character) for character in chars]
# print([bin(b).replace('b', '', 1)  for b in ords])

#convert to binary and remove 'b' from name
binary_list = [bin(b).replace('b', '', 1)  for b in ords]

# join all bits together from list
binary = "".join(binary_list)

# split all bits to a list with one bit for each entry
bin2 = tw.wrap(binary, 1)

#convert to int
bin2 = [int(char) for char in bin2]
# print(bin2)

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

#convert to string and join 
gray_len1 = to_str(gray_len1)
# print(to_dec(gray_len1))
# print(gray_len1)
gray_len1 = ''.join(gray_len1)

# m4bin = tw.wrap(pad(2, gray_len1), 1)
# gray_len2 = graycode(2, m4bin)
# gray_len2 = to_str(gray_len2)
# print(gray_len2)
# gray_len2 = ''.join(gray_len2)



# m8bin = ''.join(gray_len2)
# m8bin = tw.wrap(pad(3, gray_len2), 2)
# gray_len3 = graycode(3, m8bin)
# gray_len3 = to_str(gray_len3)
# print(gray_len3)
# gray_len3 = ''.join(gray_len3)


# m16bin = ''.join(gray_len3)
# m16bin = tw.wrap(pad(4, gray_len3), 3)
# gray_len4 = graycode(4, m16bin)
# gray_len4 = to_str(gray_len4)
# binary = pad(4, binary)
# gray_len4 = graycode(4, binary)
# gray_len4 = to_str(gray_len4)
# # print(to_dec(gray_len4))
# print(gray_len4)


# dictionary generation of symbols for m = 2, 4, 8, 16
#create all gray code combinations for given m
gray = gray_code(1)
#create all possible values 
symb = symbols(2)
#create dict with each gray code combination assigned to one possible value
m2com = dict(zip(gray, symb))
# test = match(m2com, gray_len1)
# print(match(m2com, gray_len1))
print(m2com)

gray = gray_code(2)
symb = symbols(4)
m4com = dict(zip(gray, symb))
print(m4com)

gray = gray_code(3)
symb = symbols(8)
m8com = dict(zip(gray, symb))
print(m8com)

gray = gray_code(4)
symb = symbols(16)
m16com = dict(zip(gray, symb))
print(m16com)
# test = match(m16com, gray_len4)

#ignore this
final_symb = [''] * 17

#in order do:
# split to 1 bit entrees in a list
m2bin = tw.wrap(gray_len1, 1)
# lookup each entry in dict above and get value from key
test = match(m2com, m2bin)
final_symb[2] = test

#same as before but pad the bits first in case  and then split to 2-bit entrees in a list
m4bin = tw.wrap(pad(2, gray_len1), 2)
test = match(m4com, m4bin)
final_symb[4] = test

m8bin = tw.wrap(pad(3, gray_len1), 3)
test = match(m8com, m8bin)
final_symb[8] = test

m16bin = tw.wrap(pad(4, gray_len1), 4)
test = match(m16com, m16bin)
final_symb[16] = test

# maybe find how to combine all the dicts?
# combos = dict()
# combos.update(m2com)
# combos.update(m4bin)
# combos.update(m8bin)
# combos.update(m16bin)
# print(combos)
# print(match(m16com, gray_len4))

# Custom data
data = test
# Create x axis with data length
x = np.linspace(0, len(data), len(data))

# Plot data
plt.step(x, data, where='post')

# Add labels and title
plt.xlabel('Time (s)')
plt.ylabel('Amplitude (V)')
plt.title('Rectangular Pulse Waveform')

m = ['2', '4', '8', '16']
# loop to get 4 pngs? for some reason it shows the same one in all of them 
# for i in m:
data = final_symb[m[1]]
print(data)
plt.savefig(f'graph_' + m[1] + 'pam.png')
plt.show()
