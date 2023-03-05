
"""
Question (2) - Pie Plot visualization:
    
Writing a program to visualize Summer Olympics medallists data from 1896-2008, 
of  all the countries of the world with the help of a Pie plot.

"""

# Importing all required modules/packages with general shortforms.
import pandas as pd
import matplotlib.pyplot as plt

# Defining a function medals_percentage.
def medals_percentage(olympics_data, gender, sport):
    
    """
    
    This function takes three arguments, Summer olympics data, gender and sport
    And visualizes the gender, sport wise medal percentage analysis 
    of whole world with the help of a Pie plot.
    It doesn't return any value, just plots the required data.
    
    Parameters
    ----------
    olympics_data : (pd.DataFrame)
        Summer Olympics medallists data from 1896-2008 read through pandas.
    gender : (str)
        Gender of the sport to be plotted with data.
    sport : (str)
        Type of the sport to be plotted with data.

    Returns
    -------
    None.

    """

    # Filtering the input DataFrame to include only required category of medals
    gender_sport = olympics_data[(olympics_data['Gender'] == gender) 
                                 & (olympics_data['Sport'] == sport)]

    # Counting the total number of medals won in each category by rank
    gold_medal = gender_sport[gender_sport['Medal'] 
                              == 'Gold']['Medal'].count()
    silver_medal = gender_sport[gender_sport['Medal'] 
                                == 'Silver']['Medal'].count()
    bronze_medal = gender_sport[gender_sport['Medal'] 
                                == 'Bronze']['Medal'].count()

    # Creating a list of the total medals count and corresponding labels
    total_medal_counts = [gold_medal, silver_medal, bronze_medal]
    all_medal_labels = ['Gold Medal', 'Silver Medal', 'Bronze Medal']

    # Creating the pie chart with percentage values
    plt.figure()
    plt.pie(total_medal_counts, labels = all_medal_labels, autopct='%1.1f%%')
    
    # Adding a title to the plot based on the input
    plt.title(f"{gender}'s Medals in {sport}")
    
    # To show the plot
    plt.show()


# Reading Summer Olympics data of 1896 - 2008 from an excel file
summer_olympics = pd.read_excel('https://public.tableau.com/app/sample-data/Summer_Olympic_medallists_1896-2008.xlsx', sheet_name='ALL MEDALISTS')

# Calling the medals_percentage function to plot the Women's football category
medals_percentage(summer_olympics, 'Women', 'Football')
# Calling the medals_percentage function to plot the Women's football category
medals_percentage(summer_olympics, 'Men', 'Football')