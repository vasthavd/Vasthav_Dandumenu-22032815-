# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 11:51:07 2023

@author: vasth
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



Covid = pd.read_excel('March.xlsx')

Count = Covid.pivot_table(index= ['State/UnionTerritory'], aggfunc= 'size').sort_values(ascending = False)
Count.columns = 'Total'


def  plot(Selected_state):
    
    Selected_state = Covid[ Covid['State/UnionTerritory'] == Selected_state ]
    left, right = Selected_state.Date.values[[0, -1]]
    plt.figure(figsize = (10,7))
    plt.xlim((left, right))
    plt.plot(Selected_state['Date'], Selected_state['ConfirmedIndianNational'], label="Confirmed Indian National", marker = 'o')
    plt.plot(Selected_state['Date'], Selected_state['ConfirmedForeignNational'], label="Confirmed Foreign National", marker = 'o')
    plt.plot(Selected_state['Date'], Selected_state['Cured'], label="Cured", marker = 'o')
    plt.plot(Selected_state['Date'], Selected_state['Deaths'], label="Deaths", linestyle='dashed', marker='o',
     markerfacecolor='red')
    plt.xlabel("Months")
    plt.xticks(Selected_state['Date'], rotation = 90)
    plt.ylabel("Confirmed Indian Nationals")
    plt.legend()
    plt.show()


Covid_Analysis = plot('Kerala')
print(Count)
#Covid_Analysis = plot(input("Enter a State: "))



#def extract_state(a):
    
    #State = Covid[ Covid['State/UnionTerritory'] == a ]
    #return State

#Kerala = extract_state('Kerala')


#Delhi = extract_state('Delhi')
#Telengana = extract_state('Telengana')
#Rajasthan = extract_state('Rajasthan')
#Uttar_Pradesh = extract_state('Uttar Pradesh')