import pandas as pd
import numpy as np 
from IPython.display import display

def prob1(): 
    '''
    Purpose: The purpose of this function is to learn how to create, display and merge dataframes. 
    And transform null values. 
    
    Paramaters: There are no paramaters, but this is creating and manipulating dataframes. 

    Return: No returns 
    
    '''
    
    d1 = pd.DataFrame(
        {
            "Id":[1,2,3,4],
            "Value1":["A","B","C","D"]
        }, 
        index=['X','Y','Z','W']
    )
    
    print("d1: ")
    display(d1)
    print()

    d2 = pd.DataFrame(
        {
            "Id":[1,3,5],
            "Value2":["E","F","G"]
        }, 
        index=["X","Z","Q"]
    )
     
    print("d2: ")
    display(d2)
    print()
    
    merge1 = pd.merge(d1, d2, on = 'Id')
    print("merge1: ")
    display(merge1)
    print()
    
    merge2 = pd.merge(d1, d2, how='outer',left_index=True, right_index=True)
    print("merge2: ")
    display(merge2)
    print()
    
    d4 = pd.DataFrame({
        "Id_x":[0,1,2,3,4],
        "Value1":["A","B","C","D","E"],
        "Id_y":[0,1,2,3,4],
        "Value2":["A","B","C","D","E"]
    }, index=['Q','W','X','Y','Z'])
    print("D4")
    display(d4)
    
    print("New combined dataframe: ")
    combined_df = (merge2.combine_first(d4))
    display(combined_df)

prob1()