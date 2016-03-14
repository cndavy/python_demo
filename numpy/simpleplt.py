import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0.0,6.0,0.1)
plt.plot(x, [xi**2 for xi in x],label = 'First',linewidth = 4,color = 'black')
plt.plot(x, [xi**2+2 for xi in x],label = 'second',color = 'red')
plt.plot(x, [xi**2+5 for xi in x],label = 'third')
plt.axis([0,7,-1,50])
plt.xlabel(r"$\alpha$",fontsize=20)
plt.ylabel(r'y')
plt.title('simple plot')
plt.legend(loc = 'upper left')
plt.grid(True)
#plt.savefig('simple plot.pdf',dpi = 200)
print mpl.rcParams['figure.figsize']       #return 8.0,6.0
print mpl.rcParams['savefig.dpi']          #default to 100              the size of the pic will be 800*600
#print mpl.rcParams['interactive']
plt.show()

x = np.random.randn(12,20)
y = np.random.randn(12,20)
mark = ['s','o','^','v','>','<','d','p','h','8','+','*']
for i in range(0,12):
    plt.scatter(x[i],y[i],marker = mark[i],color =(np.random.rand(1,3)),s=50,label = str(i+1))
plt.legend()
plt.show()
