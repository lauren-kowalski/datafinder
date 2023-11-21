###My code for associating a timestep interval with a Month and Year in MMMYY format.

#import libraries
import pandas as pd
import os

#create pandas dataframe of data
df = pd.read_excel('MMMYY_TimeStepInt.xlsx')
	#Column headers: 'MMMYY','Time Step Interval'
	#your data could have more than 2 columns...

#create function that pulls timestep(s) from MMMYYs
def timestep(N):
	int = df.loc[df.MMMYY == N, 'Time Step Interval'].values[0] 
	#locates N's row (N = a specific month and year) and then identified data in the same row but in
	#the column 'Time Step Interval' 
	print(int) #prints the desired time step interval per specified date.

 #when using function need to include ''s around date


==========================================================

###Editable code

#import libraries
#import pandas as pd
#import os

#create pandas dataframe of data                   
#df = pd.read_excel('<your data file>.xlsx')
        #Column headers: 'MMMYY','Time Step Interval'
        #your data could have more than 2 columns...

#create function that pulls timestep(s) from MMMYYs
#def timestep(N):
        #int = df.loc[df.<your searchable column> == N, <'your desired data column>'].values[0]
        #print(int) #prints the desired time step interval per specified date.


#ensure that when using timestep, N is in the same format as the data you are calling
