import pandas as pd


## Reading csv file

Raw_Data = pd.read_csv("Raw_data.csv")
Raw_Data = pd.DataFrame(Raw_Data , columns = ["Time","Feedingscrew_F","Feedingscrew_Am","Rotarywing_F",
                                                  "Rotarywing_Am","Idfan_F","Idfan_Am","Temp_Inlet","Temp_Outlet"
                                                  ,"Temp_Exhaust","Feeding_rate","A","B"])

## Data cleaning

# Data shape
print (Raw_Data.shape)

# Removing exctra columns 
Raw_Data = Raw_Data.drop(columns = ["A" , "B"])

#  Nulls
#print (Raw_Data.isnull())
Nal_count = Raw_Data.isnull().sum()
totalNal_count = Raw_Data.isnull().sum().sum()
print (Nal_count,totalNal_count)
#Raw_Data = Raw_Data.dropna()

# Removing duplicated rows
#print(Raw_Data.duplicated())
Raw_Data.drop_duplicates(inplace = True)

#print (Raw_Data.shape)

# ## Data Validation
# print (Raw_Data.shape)
# print (Raw_Data.dtypes)
# print (Raw_Data.info())
# print (Raw_Data.describe())
# print (Raw_Data.tail(6))
# a = Raw_Data["Feedingscrew_F"].mean()
# b = Raw_Data["Feeding_rate"].max()
# print (a , b)

#print (Raw_Data.shape)

# temperature range check
a = Raw_Data["Feedingscrew_F"]

