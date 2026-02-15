import pandas as pd
from IPython.display import display

def prob4(): 

    '''
    Purpose: The purpose of this function is to use filters and group bys to visualize different
    aspects of the data. Also using methods to see statistics like mean, max, mean, idxmax. 
    
    Paramaters: No parameters are passed through just manipulating the data that is pulled from planet csv. 
    
    Return: No returns. 
    '''
    planets = pd.read_csv("/Users/natcabrera101/Desktop/Data Science /Programming for DS/Problem Set 5 - Pandas II (1)/Files/planets.csv")
    print()
    
    over_900 = planets.groupby('method').filter( lambda x: x['number'].sum() > 900)
    display(over_900)
    
    display(planets.groupby('method')['orbital_period'].agg(['max','min']))
    print()
    
    planets['numbers_each_years'] = planets.groupby('year')["number"].transform('sum')
    display(planets.head(10))
    
    max_orb = (planets.groupby('method')['orbital_period']).max()
    display(max_orb)
    print() 
    
    print(f"{max_orb.idxmax()} is the longest orbital period")
    
prob4()