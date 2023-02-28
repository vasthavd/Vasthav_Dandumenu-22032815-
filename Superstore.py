# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:58:06 2023

@author: vasth
"""

import pandas as pd
import matplotlib.pyplot as plt

def scatter_plot(data, x_var, y_var):
    """
    Generate a scatter plot of two variables from the Superstore dataset.
    
    Parameters:
        data (pd.DataFrame): The Superstore dataset.
        x_var (str): The name of the variable to use for the x-axis.
        y_var (str): The name of the variable to use for the y-axis.
    """
    # Create the scatter plot
    plt.scatter(data[x_var], data[y_var])
    plt.xlabel(x_var)
    plt.ylabel(y_var)
    plt.title(f'Superstore {x_var} vs. {y_var}')
    plt.show()
    
# Load the Superstore dataset
superstore_df = pd.read_excel('SS.xls')

# Generate a scatter plot of Sales vs. Profit
scatter_plot(superstore_df, 'Sales', 'Profit')

def bar_plot(data, cat_var):
    """
    Generate a bar plot of total sales for each category in the Superstore dataset.
    
    Parameters:
        data (pd.DataFrame): The Superstore dataset.
        cat_var (str): The name of the categorical variable to use for grouping.
    """
    # Compute the total sales for each category
    sales_by_cat = data.groupby(cat_var)['Sales'].sum()
    
    # Create the bar plot
    plt.figure(figsize=(10,6))
    plt.bar( sales_by_cat.index, sales_by_cat)
    plt.xlabel(cat_var)
    if cat_var in ['Category', 'Region']:
        plt.xticks(rotation=0)
    elif cat_var in ['Sub-Category', 'State']:
        plt.xticks(rotation=90)
    plt.ylabel('Total Sales')
    plt.title(f'Superstore Total Sales by {cat_var}')
    #for i, v in enumerate(sales_by_cat):
        #plt.text(i, v, f"${v:,.0f}", ha='center', va='bottom')
    plt.legend()
    plt.show()
    

# Generate a bar plot of total sales by category


bar_plot(superstore_df, 'Category')
bar_plot(superstore_df, 'Sub-Category')
bar_plot(superstore_df, 'State')
bar_plot(superstore_df, 'Region')







































