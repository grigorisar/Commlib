import numpy as np
import textwrap as tw
import matplotlib.pyplot as plt
import math

def symbols(m):
    list = []
    for k in range(0, m+1):
        list.append(2*k -m +1)
    return list

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
    
def str_array(arr):
    return [str(i) for i in arr]

def match(com, binlist):
    temp = []
    for i in binlist:
        temp.append(com[i])
    return temp

def toBinary(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

firstname = "Grigoris"
lastname = "Arfanis"
chars = list(firstname + lastname) 

#get ascii code for each character given from user
ascii_chars = [ord(character) for character in chars]
# print([bin(b).replace('b', '', 1)  for b in ascii_chars])

#convert to binary and remove 'b' from name
binary = [bin(b).replace('b', '', 1)  for b in ascii_chars]

# join all bits together from list
binary = "".join(binary)

# split all bits to a list with one bit for each entry
bit_lst = tw.wrap(binary, 1)

#convert to int
bit_lst = [int(char) for char in bit_lst]
# print(bit_lst)

gray_array = [0] * len(bit_lst)  
# iterate through each bit ignoring first one applying xor, current new bit = old previous bit XOR old current bit
for idx in range(1, len(bit_lst)):
    prev = bit_lst[idx - 1]
    # print(f'prev = '+ str(prev))
    curr = bit_lst[idx]
    # print(f'curr = '+ str(prev))
    if prev + curr == 1 :
        gray_array[idx] = 1
    else:
        gray_array[idx] = 0
        
    # print(f'new for pos ' + str(idx) + ' = '+ str(bit_lst[char]))

#convert to string and join 
gray_array = str_array(gray_array)
# print(to_dec(gray_array))
# print(gray_array)
gray_array = ''.join(gray_array)

# My simplification
final_symb = [''] * 17
for M in [2,4,8,16]:
    i=int(math.log(M,2))
    # print(M,i)

    #create all gray code combinations for given m
    gray = gray_code(i)
    #create all possible values 
    symb = symbols(M) 
    #create dict with each gray code combination assigned to one possible value
    mcom = dict(zip(gray,symb))
    # split to 1 bit entrees in a list
    mbin = tw.wrap(pad(i,gray_array),i)
    # lookup each entry in dict above and get value from key
    final_symb[M] = match(mcom,mbin)
    test = match(mcom,mbin)

    data = test
    x = np.linspace(0, len(data), len(data))

    plt.grid(axis='x', color='0.95')    
    plt.axhline(y=0, color='0.65', linestyle='-')
    # plt.bar(x, data, align='center',color='red')
    plt.step(x, data, where='mid',color='orange')
    plt.plot(x, data, 'o-', color='gray', alpha=0.4)
   
    # Add labels and title
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude (V)')
    plt.title(f'{M}-PAM')

    #save figure
    plt.savefig(f"{M}-PAM.png")
    #clear plot
    plt.clf() 
    

