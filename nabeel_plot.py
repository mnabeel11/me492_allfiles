from matplotlib.pyplot import *
from numpy import *

t=arange(1,3,0.01)
T=6*log(t)-7*exp(0.2*t)
figure(1)
clf()
plot(t,T)
ylabel('Degrees Celsius')
xlabel('Minutes')
title('Nabeel-plot')
savefig('my_fig.png',dpi=300 ) 
show()
print('Hello World! I just wrote my first program. Yayyy')
print('Moaz Nabeel')

