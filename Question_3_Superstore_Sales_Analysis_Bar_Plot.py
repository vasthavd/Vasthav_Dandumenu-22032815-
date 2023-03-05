"""

 Question (3) - Bar Plot visualization:
 Writing a program to visualize Superstore data, 
 sales by Category, Sub-Category, Region and State with the help of a bar plot.

"""

# Importing all required modules/packages with general shortforms.
import pandas as pd
import matplotlib.pyplot as plt

# Defining a function superstore_sales_plot.
def superstore_sales_plot(store_data, type_variable):
    
    """
    
    This function takes two arguments, superstore data over several years &
    type of sales to be plotted. And visualizes the sales per selected type
    using a bar plot.
    It doesn't return any value, just plots the sales data.
    
    Parameters
    ----------
        store_data : (pd.DataFrame)
            Several years superstore data read through pandas.
        type_variable : (str)
            Type of the sales to be plotted with data by grouping.
        
    Returns
    -------
    None.
        
    """
    
    # Calculating the total sales for each type
    type_of_sales = store_data.groupby(type_variable)['Sales'].sum()
    
    # Adjusting the figure size to 10x6 inches.
    plt.figure(figsize = (10, 6))
    
    # Creating the bar plot with data based on the input
    plt.bar(type_of_sales.index, type_of_sales)
    
    # Setting the x-axis label based on the input
    plt.xlabel(f'Different types of {type_variable}')
    
    # if - else condition to rotate xticks values for better readability
    if type_variable in ['Category', 'Region']:
        
        plt.xticks(rotation = 0)
        
    elif type_variable in ['Sub-Category', 'State']:
        
        plt.xticks(rotation = 90)
    
    # Setting the y-axis label to 'Sales between 2014 - 2017'   
    plt.ylabel('Sales')
    
    # Adding a title to the plot based on the input
    plt.title(f'Total sales of the Superstore by {type_variable} between 2014 - 2017')
    
    # To show the plot
    plt.show()
    

# Load the Superstore dataset
super_store = pd.read_excel('https://public.tableau.com/app/sample-data/sample_-_superstore.xls', sheet_name='Orders')

# Calling the superstore_sales_plot function to plot total sales by four types
superstore_sales_plot(super_store, 'Category')
superstore_sales_plot(super_store, 'Sub-Category')
superstore_sales_plot(super_store, 'State')
superstore_sales_plot(super_store, 'Region')


































