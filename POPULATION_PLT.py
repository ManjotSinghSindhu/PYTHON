# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 11:19:51 2018

@author: Manjot singh
"""

import matplotlib.pyplot as plt

years=[1950,1955,1960,1965,1970,1975,1980,1985,1990,1995,2000,2005,2010,2015]

pops=[1.6,2.5,3.0,3.3,3.6,4.0,4.4,4.8,5.3,5.7,6.1,6.5,6.9,7.3]

deaths=[1.2,1.7,1.8,2.2,2.5,2.7,2.9,3,3.1,3.3,3.5,3.8,4.0,4.3]

plt.plot(years,pops,color=(255/255,100/255,100/255))
plt.plot(years,deaths,'--',color=(0.6,0.6,1))
plt.xlabel('YEARS')
plt.ylabel('POPULATION')
plt.title('POPULATION GROWTH')
plt.show()