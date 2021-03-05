
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def multiple_formatter(denominator=2, number=np.pi, latex='\pi'):
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a
    def _multiple_formatter(x, pos):
        den = denominator
        num = np.int(np.rint(den*x/number))
        com = gcd(num,den)
        (num,den) = (int(num/com),int(den/com))
        if den==1:
            if num==0:
                return r'$0$'
            if num==1:
                return r'$%s$'%latex
            elif num==-1:
                return r'$-%s$'%latex
            else:
                return r'$%s%s$'%(num,latex)
        else:
            if num==1:
                return r'$\frac{%s}{%s}$'%(latex,den)
            elif num==-1:
                return r'$\frac{-%s}{%s}$'%(latex,den)
            else:
                return r'$\frac{%s%s}{%s}$'%(num,latex,den)
    return _multiple_formatter

class Multiple:

    def __init__(self, denominator=2, number=np.pi, latex='\pi'):
        self.denominator = denominator
        self.number = number
        self.latex = latex

    def locator(self):
        return plt.MultipleLocator(self.number / self.denominator)

    def formatter(self):
        return plt.FuncFormatter(multiple_formatter(self.denominator, self.number, self.latex))


def a0():
    return np.pi/2

def coswave(n,x,l):
    if n%2==0:
        an=0
    else:
        an=0
    return an*np.cos(n*np.pi*x/l)

def sinwave(n,x,l):
    if n%2==0:
        bn=-1/n
    else:
        bn=-1/n
    return bn*np.sin(n*np.pi*x/l)


def plotter(waves,graphlim1,graphlim2,detail,no):
    y=[]
    for x in np.arange(graphlim1,graphlim2,1/detail):
        rumus=0
        for n in range(1,waves):
            rumus += sinwave(n,x,np.pi) + coswave(n,x,np.pi)
        y.append((a0()/2)+rumus)
    plt.plot(np.arange(graphlim1,graphlim2,1/detail),y,label=no)

fig=plt.figure(figsize=(30,5), dpi= 100, facecolor='w', edgecolor='k')

graphlim1=-3*np.pi
graphlim2=3*np.pi
detail=100
waves=[2,3,4,5,6,7,8,9,10]

for wave in waves:
    plotter(wave,graphlim1,graphlim2,detail,str(wave)+' Gelombang')


def phiplot():
    ax.yaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(np.pi / 12))
    ax.xaxis.set_major_locator(plt.MultipleLocator(np.pi / 2))
    ax.xaxis.set_minor_locator(plt.MultipleLocator(np.pi / 12))
    ax.xaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter()))
    ax.yaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter()))

plt.title('DERET FOURIER LETS GOOO')
ax = plt.gca()
ax.grid(True)
ax.axhline(0, color='black', lw=2)
ax.axvline(0, color='black', lw=2)
phiplot()
plt.legend()
plt.show()

