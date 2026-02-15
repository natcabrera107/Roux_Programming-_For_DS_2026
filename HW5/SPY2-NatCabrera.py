import pandas as pd
from IPython.display import display

def prob2(): 
    '''
    Purpose: This function is designed to teach us and show how to merge dataframes and to use concat. 

    Paramaters: There are no parameters, just the creation, displaying and manipulation of dataframes. 

    Return: No returns.
    
    '''
    
    data1 = {'ID1': [1, 2, 3],
             'ID2': [101, 102, 103],
             'Value1': ['A', 'B', 'C']}
    df1 = pd.DataFrame(data1)
    print("DF1: ")
    display(df1)
    print()

    data2 = {'ID1': [2, 3, 4],
             'ID2': [102, 103, 104],
             'Value2': ['X', 'Y', 'Z']}
    df2 = pd.DataFrame(data2)
    print("DF2: ")
    display(df2)
    print()

    data3 = {'ID3': [101, 102, 103],
             'Value3': ['Apple', 'Banana', 'Cherry']}
    print("DF3: ")
    df3 = pd.DataFrame(data3)
    display(df3)
    print()
    
    res = pd.concat([df1, df2, df3])
    print("Concat: ")
    display(res)
    print()

    merge1 = pd.merge(df1, df2, on=['ID1','ID2'])
    print("Merge 1: ")
    display(merge1) 
    print() 
    
    merge2 = pd.merge(merge1, df3, left_on='ID2', right_on='ID3')
    print("Final Merge: ")
    display(merge2)
    
prob2()
    