import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
    
    
def data_manip(route1, route2, route3):

    #combine all 3 routes
    df = pd.concat([route1,route2,route3],axis = 0)
    #filter for Dockability & Rideability
    df = df[df['Dockability']*df['Releasability'] == 1] 
    
    #functions for creating categories
    def utcicat1(row):
        if row['utcivar1'] < -40:
            val = -5
        elif (-40 <= row['utcivar1'] and row['utcivar1'] <-27):
            val = -4
        elif (-27 <= row['utcivar1'] and row['utcivar1'] <-13):
            val = -3 
        elif (-13 <= row['utcivar1'] and row['utcivar1'] <0):
            val = -2 
        elif (0<= row['utcivar1'] and row['utcivar1'] <9):
            val = -1
        elif (9 <= row['utcivar1'] and row['utcivar1'] <26):
            val = 0
        elif (26 <= row['utcivar1'] and row['utcivar1'] <28):
            val = 1 
        elif (28 <= row['utcivar1'] and row['utcivar1'] <32):
            val = 2
        elif (32 <= row['utcivar1'] and row['utcivar1'] <38):
            val = 3
        elif (38 <= row['utcivar1'] and row['utcivar1'] <46):
            val = 4
        elif (row['utcivar1'] >= 46):
            val = 5
        return val

    def utcicat2(row):
        if row['utcivar2'] < -40:
            val = -5
        elif (-40 <= row['utcivar2'] and row['utcivar2'] <-27):
            val = -4
        elif (-27 <= row['utcivar2'] and row['utcivar2'] <-13):
            val = -3 
        elif (-13 <= row['utcivar2'] and row['utcivar2'] <0):
            val = -2 
        elif (0<= row['utcivar2'] and row['utcivar2'] <9):
            val = -1
        elif (9 <= row['utcivar2'] and row['utcivar2'] <26):
            val = 0
        elif (26 <= row['utcivar2'] and row['utcivar2'] <28):
            val = 1 
        elif (28 <= row['utcivar2'] and row['utcivar2'] <32):
            val = 2
        elif (32 <= row['utcivar2'] and row['utcivar2'] <38):
            val = 3
        elif (38 <= row['utcivar2'] and row['utcivar2'] <46):
            val = 4
        elif (row['utcivar2'] >= 46):
            val = 5
        return val

    def utcicat3(row):
        if row['utcivar3'] < -40:
            val = -5
        elif (-40 <= row['utcivar3'] and row['utcivar3'] <-27):
            val = -4
        elif (-27 <= row['utcivar3'] and row['utcivar3'] <-13):
            val = -3 
        elif (-13 <= row['utcivar3'] and row['utcivar3'] <0):
            val = -2 
        elif (0<= row['utcivar3'] and row['utcivar3'] <9):
            val = -1
        elif (9 <= row['utcivar3'] and row['utcivar3'] <26):
            val = 0
        elif (26 <= row['utcivar3'] and row['utcivar3'] <28):
            val = 1 
        elif (28 <= row['utcivar3'] and row['utcivar3'] <32):
            val = 2
        elif (32 <= row['utcivar3'] and row['utcivar3'] <38):
            val = 3
        elif (38 <= row['utcivar3'] and row['utcivar3'] <46):
            val = 4
        elif (row['utcivar3'] >= 46):
            val = 5
        return val

    def precipitationcat(row):
        if row['Precipitation'] == 0:
            val = 0
        else:
            val = 1
        return val

    def hourcat(row):
        if row['Hour'] <= 6: 
            val = 'midnight'
        elif row['Hour'] <= 10: 
            val = 'morning'
        elif row['Hour'] <= 13:
            val = 'early_afternoon'
        elif row['Hour'] <= 17:
            val = 'late_afternoon'
        elif row['Hour'] <= 23:
            val = 'evening'
        return val

    def countcat(row): 
        if row['count'] == 0: 
            val = 0 
        elif row['count'] <= 2:
            val = 1
        elif row['count'] >= 3: 
            val = 2
        return val

    def weekendcat(row):
        year = str(int(row['Year']))

        month = int(row['Month'])
        month = str(("0" if month < 10 else "")) + str(month)

        day = int(row['Day'])
        day = str(("0" if day < 10 else "")) + str(day)

        hour = int(row['Hour'])
        hour = str(("0" if hour < 10 else "")) + str(hour)

        inputstring = year + month + day + hour
        datetime = pd.to_datetime(inputstring,format='%Y%m%d%H')
        day = datetime.dayofweek
        isWeekend = 1 if day > 4 else 0
        return isWeekend
    
    #set up categorical predictors
    df['utcivar1_cat'] = df.apply(utcicat1, axis=1)
    df['utcivar2_cat'] = df.apply(utcicat2, axis=1)
    df['utcivar3_cat'] = df.apply(utcicat3, axis=1)
    df['precipitation_cat'] = df.apply(precipitationcat, axis=1)
    df['hour_cat'] = df.apply(hourcat, axis=1)
    df['count_cat'] = df.apply(countcat, axis=1)
    df['weekend'] = df.apply(weekendcat, axis=1)
    
    #drop unecessary columns
    df = df.drop(['DateTime','Dockability','Releasability'],axis =1)
    
    # hour_cat
    df['morning'] = (df['hour_cat'] == 'morning')*1
    df['evening'] = (df['hour_cat'] == 'evening')*1
    df['midnight'] = (df['hour_cat'] == 'midnight')*1
    
    return df