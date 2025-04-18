import pandas as pd

# function reads a file and then returns a data frame 
def read(file):
    # read the file
    data = pd.read_csv(file)
    # return the data frame
    return data
