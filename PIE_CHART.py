# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 11:36:25 2018

@author: Manjot singh
"""

import matplotlib.pyplot as plt

labels='PYTHON','JAVA','C++','PERL','PHP','ARDUINO'
sizes=(33,52,12,17,60,84)
seprated=[1,0,0,0,0,0]

plt.pie(sizes,labels=labels,autopct='%1.2f%%')

plt.axis('equal')
plt.show()