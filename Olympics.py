"""
(2) - Pie Plot visualization:
    
Writing a program to visualize state-wise Covid data, 
of the country India with the help of a line plot.

"""

import pandas as pd
import matplotlib.pyplot as plt


def medals_percentage(olympics_data, gender, sport):
    
    """
    
    This function takes three arguments, Summer olympics data, gender and sport
    And visualizes the gender, sport wise medal percentage analysis 
    of whole world with the help of a Pie plot.
    It doesn't return any value, just plots the required data.
    
    Parameters
    ----------
    olympics_data : (pd.DataFrame)
        DESCRIPTION.
    gender : (str)
        Gender of the sport to be plotted with data.
    sport : (str)
        Type of the sport to be plotted with data.

    Returns
    -------
    None.

    """

    # Filter the DataFrame to include only men's medals in aquatics
    gender_sport = olympics_data[(olympics_data['Gender'] == gender) 
                                 & (olympics_data['Sport'] == sport)]

    # Counting the total number of medals won in each category
    gold_medal = gender_sport[gender_sport['Medal'] 
                              == 'Gold']['Medal'].count()
    silver_medal = gender_sport[gender_sport['Medal'] 
                                == 'Silver']['Medal'].count()
    bronze_medal = gender_sport[gender_sport['Medal'] 
                                == 'Bronze']['Medal'].count()

    # To create a list of the total medal count and respective labels
    total_medal_counts = [gold_medal, silver_medal, bronze_medal]
    all_medal_labels = ['Gold Medal', 'Silver Medal', 'Bronze Medal']

    # Creating the pie chart with percentage values
    plt.figure()
    plt.pie(total_medal_counts, labels=all_medal_labels, autopct='%1.1f%%')
    plt.title("{}'s Medals in {}".format(gender, sport))
    plt.show()


# Reading Summer Olympics data of 1896 - 2008 from an excel file
summer_olympics = pd.read_excel('https://public.tableau.com/app/sample-data/Summer_Olympic_medallists_1896-2008.xlsx', sheet_name='ALL MEDALISTS')

#Calling the medals_percentage function to plot the Women's football category
medals_percentage(summer_olympics, 'Women', 'Football')

