import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt 

def prob5(): 

    '''
    Purpose: The purpose of this function is to build data visualizations and use csv files to look at speciic sub data using dataframes and matplotlib
    
    Paramaters: No parameters are passed through just manipulating the csv data that is pulled from planet csv. Please also note that I decided to put both plots on 
    one fig as subplots because in vscode for some reason when i used plt.show() it would only show one plot, so I looked up how to put two plots on one. 
    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html 
    
    Return: No returns. 
    '''
    planets = pd.read_csv("/Users/natcabrera101/Desktop/Data Science /Programming for DS/Problem Set 5 - Pandas II (1)/Files/planets.csv")
    print()
    
    df = planets.groupby('year')['number'].sum()
    display(df)
    
    q2 = planets.groupby('method')['number'].sum()
    display(q2)
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 16))
    
    df.plot(
        kind = 'line',
        title = 'Planets by number per year',
        xlabel = 'year', 
        ylabel ='planets', 
        grid=True, 
        colormap='viridis', 
        legend=True,
        ax=ax1
    )
    
    q2.plot(
        kind = 'bar',
        title = 'Planets discovered by method',
        xlabel = 'Method', 
        ylabel ='Planets',  
        grid=True, 
        colormap='viridis', 
        legend=True,
        ax=ax2)

    plt.show()
    
prob5()