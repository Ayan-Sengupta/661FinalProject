import read 
import pandas as pd

def data_clean():
    
    df = read.read('/home/ayan/work/MachineLearning/FinalProject/data/education_career_success.csv')
    # our target variable is 'no .of job offers recieved'
    # check if there is missing variables in that column
    print("Missing values in 'Job_Offers' column:")
    print(df['Job_Offers'].isnull().sum())

    # convert gender to dummt variables, then convert to binary for the resulting columns
    df = pd.get_dummies(df, columns=['Gender'] )
    # comvert column to binary - 1 for TRUE, 0 for FALSE
    df[['Gender_Female', 'Gender_Male', 'Gender_Other']] = df[['Gender_Female', 'Gender_Male', 'Gender_Other']].astype(int)

    # convert 'Current_Job_Level' to herearchical numerical values
    df['Current_Job_Level'] = df['Current_Job_Level'].apply(lambda x: 1 if x == 'Entry' else (2 if x == 'Mid' else (3 if x == 'Senior' else 4)))

    # convert 'Field_of_Study' to dummy variables, then convert to binary for the resulting columns
    df = pd.get_dummies(df, columns=['Field_of_Study'])
    # 'Field_of_Study_Arts', 'Field_of_Study_Business',
    #    'Field_of_Study_Computer Science', 'Field_of_Study_Engineering',
    #    'Field_of_Study_Law', 'Field_of_Study_Mathematics',
    #    'Field_of_Study_Medicine'
    # convert resulting columns to binary
    df[['Field_of_Study_Arts', 'Field_of_Study_Business', 'Field_of_Study_Computer Science', 'Field_of_Study_Engineering', 'Field_of_Study_Law', 'Field_of_Study_Mathematics', 'Field_of_Study_Medicine']] = df[['Field_of_Study_Arts', 'Field_of_Study_Business', 'Field_of_Study_Computer Science', 'Field_of_Study_Engineering', 'Field_of_Study_Law', 'Field_of_Study_Mathematics', 'Field_of_Study_Medicine']].astype(int)
   
    #  convert 'Entrepreneurship' to binary 
    df['Entrepreneurship'] = df['Entrepreneurship'].apply(lambda x: 1 if x == 'Yes' else 0)
    
    # write the df back as a csv file in the data dir, call it "cleaned_data.csv"
    df.to_csv('/home/ayan/work/MachineLearning/FinalProject/data/clean/education_career_success_clean.csv', index=False)


data_clean()
   


    





