import pandas as pd 
from IPython.display import display

def prob3(): 
    '''
    Purpose: The purpose of this is to clean data, droping rows with nulls and also finding statistics about the data. 
    
    Paramaters: No parameters are passed through just manipulating the data that is pulled from file. 

    Return: No returns 
    '''
    file = pd.read_csv("/Users/natcabrera101/Desktop/Data Science /Programming for DS/Problem Set 5 - Pandas II (1)/Files/planets.csv")
    print("Head")
    print(file.head())
    print()
    
    cleaned_file = file.dropna(inplace=False)
    print("#2 Droped rows with describe:")
    print(cleaned_file.describe())
    print()
    
    print("#3 Median of orbital period for each method:")
    print(file.groupby('method')['orbital_period'].median())
    print()
    
    print("#4 Average number of planets discovered per year:")
    print(file.groupby('year')['number'].mean())
    print()
    
    print("Add column:")
    file['decade'] = (file['year']//10 * 10)
    
    print("Boolean mask:")
    mask = file['year'] >= 1980
    display(file[mask].groupby('decade')['number'].sum())

    
prob3()

