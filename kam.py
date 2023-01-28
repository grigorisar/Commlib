import numpy as np
import matplotlib.pyplot as plt
from scipy import special

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
def str_to_bitsarray(a):
  l,m=[],[]
  for i in a:
    l.append(ord(i))
  for i in l:
    m.append(int(bin(i)[2:]))
  return m

class Constellation:
    def __init__(self, title = None): 
        self.map = {}
        self.bits = []
        self.bits_str = [] 
        self.symbols = []
        self.title = title 
        self.m = None
    def avg_power(self):
        return np.mean( np.abs(self.symbols) ** 2.0)
    def plot(self, figure_no = None, plot_type = 'o'):
        if figure_no is None: 
            plt.figure()
        else:
            plt.figure(figure_no)
        cr = np.real(self.symbols)
        ci = np.imag(self.symbols) 
        plt.plot(cr, ci, plot_type) 
        plt.xlabel('Real') 
        plt.ylabel('Imag')
        
        if self.title is not None: 
            plt.title(self.title)
        plt.savefig("plotfn.png")

    def plot_map( self, figure_no = None, disp_x = 0.0, disp_y = 0.0, rotation = 90, plot_type = 'bo', axis_equal = True):
        self.plot( figure_no = figure_no, plot_type = plot_type)
        for i, bits in enumerate(self.bits_str):
            symbol = self.symbols[i]
            bits_str = self.bits_str[i]
            plt.text( np.real(symbol) + disp_x, np.imag(symbol) + disp_y,bits_str,rotation = rotation)
        if self.title is not None: 
            plt.title(self.title)
        if axis_equal: 
            plt.axis('equal')

    def set_symbols( self, symbols ): 
        self.symbols = symbols

    def set_gray_bits( self, m ): 
        g = gray_code( m )
        self.m = m
        for i, cw in enumerate(g): 
            self.bits_str.append(cw)
            self.bits.append( str_to_bitsarray( cw ) ) 
            self.map[ cw ] = self.symbols[ i ]

    def bits_to_symbols( self, bits, return_groups = False ): 
        symbols = []
        bitgroups = [] 
        i=0
        j=0
        if not isinstance(bits, str): 
            bits = array_to_str(bits)
        while i < len(bits):
            key = bits[ i : i + self.m ] 
            bitgroups.append( key ) 
            symbols.append( self.map[ key ] ) 
            i += self.m
            j += 1
        if not return_groups:
            return np.array(symbols)
        else:
            return np.array(symbols), bitgroups
    def find_closest( self, sample ):
        return np.abs( self.symbols - sample ).argmin()
    def decode( self, sample ):
        i = self.find_closest( sample )
        return [self.symbols[i], self.bits[i], self.bits_str[i] ]



def Qfunction(x):
    return 0.5 * special.erfc(x/np.sqrt (2.0))
    
class pam_constellation(Constellation):
    def __init__(self, M, beta = 1, title = None, SNRbdB = None):
        super().__init__(title = title)
        self.M = M
        self.m = np.log2(M).astype(int) 
        self.SNRbdB = SNRbdB
        symbols = np.zeros( M ) 
        for i in range( M ):
            symbols [ i ] = 2 * i - M + 1
        self.set_symbols( symbols ) 
        self.set_gray_bits( self.m )
    def ser(self):
        SNRb = 10 ** ( self.SNRbdB / 10)
        q = 6 * SNRb * self.m / (self.M ** 2.0 - 1)
        return 2 * (self.M-1) / self.M * Qfunction ( np.sqrt(q) )
    def ber(self):
        return self.ser() / self.m

