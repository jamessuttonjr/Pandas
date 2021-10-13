import pandas as pd

grades_dict = {'Wally':[87,96,70],
                'Eva':[100,87,90],
                'Sam':[94,77,90],
                'Katie':[100,81,82],
                'Bob':[83,65,85]}

# Whenever we convert a dictionary to a data fram the keys become the columns and the values become the rows in the data frame

grades = pd.DataFrame(grades_dict)

grades.index = ['Test1','Test2','Test3']

print(grades)

#print(grades.T) will transpose it and flit rows and columns for grades
# each column in data frame is a series in a one dimensional array

#print(grades['Eva'])

#print(grades.Sam)

#using loc and iloc methods

#print(grades.loc['Test2'])

#print(grades.iloc[1])
#both above give same result

#For consecutive rows
print(grades.loc['Test1':'Test3'])

print(grades.iloc[0:3])
#both above give same result

#For non-consecutive rows
print(grades.loc[['Test1','Test3']])
print(grades.iloc[[0,2]])


#view only Eva's and Katie's grades for Test1 and Test2

print(grades.loc['Test1':'Test2',['Eva','Katie']])

#view only Sam's THRU Bob's grades for Test1 and Test3

print(grades.loc[['Test1','Test3'], 'Sam':'Bob'])

#Select everyone with an A grade
grades_A = grades[grades>=90]

print(grades_A)

#Select everyone with a B grade
grades_B = [(grades>=80) & (grades < 90)]

print(grades_B)

# create a dataframe for everyone with a A or B grade
grades_A_B = [(grades>=90) | (grades >= 80)]

print(grades_A_B)


pd.set_option('precision', 2)

print(grades.T.describe())


print(grades.sort_index(ascending=False))


#puts column index in alphabetical order
print(grades.sort_index(axis=1))

#puts column index in  reverse alphabetical order
print(grades.sort_index(axis=1, ascending=False))


#this sorts it by test 1 and by columns so the highest scores are first
print(grades.sort_values(by='Test1', axis=1, ascending=False))

#we want the columns to be the test and the students name to be the rows you just transpose it and take out the axis
print(grades.T.sort_values(by='Test1', ascending=False))


#This gets rid of column two and three and just gives column 1
print(grades.loc['Test1'].sort_values(ascending=False))

#sort_index and sort_values return a copy of the original DataFrame

