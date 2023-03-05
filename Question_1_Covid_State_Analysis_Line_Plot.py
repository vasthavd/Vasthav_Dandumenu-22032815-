"""

 Question (1) - Line Plot visualization:
 Writing a program to visualize Covid data, 
 state-wise of the country India with the help of a line plot for 2020.

"""

# Importing all required modules/packages with general shortforms.
import pandas as pd
import matplotlib.pyplot as plt

# Defining a function covid_state_analysis.
def covid_state_analysis(covid_data, state):
    
    """
    
    This function takes two arguments, monthly Covid data and a selected state.
    And visualizes the Covid state-wise data analysis with the help of a 
    line plot.
    It doesn't return any value, just plots the selceted state data.
    
    Parameters
    ----------
        covid_data : (pd.DataFrame)
            Monthly covid data read through pandas.
        state : (str)
            Name of the state to be analysed with data.
        
    Returns
    -------
    None.
        
    """
    
    # Declaring state_title variable to use it in the title() function
    state_title = str(state)
    
    # Segregating data for a selected state.
    state = covid_data[covid_data['State/UnionTerritory'] == state]
    
    
    # Adjusting the figure size to 10x7 inches.
    plt.figure(figsize = (10, 7))
    
    
    # Plotting the data for Confirmed Indian National cases, 
    # Confirmed Foreign National cases, Cured cases, 
    # and Deaths registered during the selected month.
    
    
    plt.plot(state['Date'], state['ConfirmedIndianNational'], 
             label = "Confirmed Indian National", marker = 'o')
    
    plt.plot(state['Date'], state['ConfirmedForeignNational'], 
             label = "Confirmed Foreign National", marker = 'o')
    
    plt.plot(state['Date'], state['Cured'], 
             label = "Cured", marker = 'o')
    
    plt.plot(state['Date'], state['Deaths'], 
             label = "Deaths", marker = 'o')
    
    # Setting the x-axis label to "Days of the Month"
    plt.xlabel("Days of the Month")
    
    # Rotating the x-axis tick labels by 90 degrees for better readability
    plt.xticks(state['Date'], rotation=90)
    
    # Assigning the x-axis limits to the first,
    # and last dates from the selected state data.
    left, right = state.Date.values[[0, -1]]
    plt.xlim((left, right))
    
    # Setting the y-axis label to "Number of Covid Cases"
    plt.ylabel("Number of Covid Cases")
    
    # Adding a title to the plot based on the input selected state
    plt.title(f'Covid analysis of {state_title}, India')
    
    # Adding a legend to the plot to display labels
    plt.legend()
    
    # To show the plot
    plt.show()
    
    
# Reading march covid data of states from excel file
# 'March.xlsx' Link = https://docs.google.com/spreadsheets/d/1R9opFJAFmCWGj4tYyEOHBYmLYn9cWj8V/edit?usp=sharing&ouid=104617704634998031407&rtpof=true&sd=true
march_data = pd.read_excel('March.xlsx')

# Call the covid_state_analysis function for the states of Maharashtra & Kerala
covid_state_analysis(march_data, 'Maharashtra')
covid_state_analysis(march_data, 'Kerala')




