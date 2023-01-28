import numpy as np
from numpy import exp
import matplotlib .pyplot as plt
from scipy import special 

def qxfunction(x):
    return 0.5 * special.erfc(x/np.sqrt (2.0))

def q1function(x):
    return exp(-1*(x**2)/2)

def q2function(x):
    return 0.25 * (exp(-1*(x**2))+ exp(-1*(x**2)/2))

def q3function(x):
    return (1/12) * exp(-1*(x**2)/2) + (1/4) * exp(-1* ((2*x)**2/3))

# step 2
def trapFnQ1 (x):
    return np.trapz(x=x,y=integralFn1(x))
def trapFnQ2 (x):
    return np.trapz(x=x,y=integralFn2(x))
def trapFnQ3 (x):
    return np.trapz(x=x,y=integralFn3(x))

def integralFn1 (x):
    return abs(q1function(x)-qxfunction(x))/abs(qxfunction(x))
def integralFn2 (x):
    return abs(q2function(x)-qxfunction(x))/abs(qxfunction(x))
def integralFn3 (x):
    return abs(q3function(x)-qxfunction(x))/abs(qxfunction(x))

start = 2
end = 7
x = np.arange(start ,end ,0.005)

q1=q1function(x)
q2=q2function(x)
q3=q3function(x)

font = {'family' :'serif','weight' : 'normal', 'size' : 16}
plt.rc('font', ** font)
# Plot Q function
plt.figure(num = 1, figsize = (10 ,8))
plt.xlabel('$x$',** font)
plt.ylabel('$Q(x)$')
plt.semilogy(x, qxfunction(x),label="Q(x)",) #original qfunction
plt.semilogy(x, q1,label="Q1",linestyle="--")
plt.semilogy(x, q2,label="Q2",linestyle="--")
plt.semilogy(x, q3,label="Q3",linestyle="--")
plt.tight_layout()
plt.legend()
plt.grid ()
plt.savefig('Qfunction.png')

q1error = trapFnQ1(x)
q2error = trapFnQ2(x)
q3error = trapFnQ3(x)

print(f'Q1 Error: {q1error:f}\nQ2 Error: {q2error:f}\nQ3 Error: {q3error:f}')
# print(q1error)
# print(q2error)
# print(q3error)


