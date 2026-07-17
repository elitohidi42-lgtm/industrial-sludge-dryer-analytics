import pandas as pd


### Reading csv file
Raw_Data = pd.read_csv("Raw_data.csv")
Raw_Data = pd.DataFrame(Raw_Data , columns = ["Time","Feedingscrew_F","Feedingscrew_Am","Rotarywing_F",
                                                  "Rotarywing_Am","Idfan_F","Idfan_Am","Temp_Inlet","Temp_Outlet"
                                                  ,"Temp_Exhaust","Feeding_rate","Stage","Status"])

### Data Prepration

# Data inspection in first stage
print (f" the data shape is:{Raw_Data.shape}")
print (f" data type in columns is: {Raw_Data.dtypes}")
print (f"")

#  Nulls Report & Desicioning
null_report = pd.DataFrame({
    "Null Count": Raw_Data.isnull().sum(),
    "Null Percent": (Raw_Data.isnull().mean() * 100).round(2)
})
#print(null_report)
#print (f"based on the {null_report} we need to remove Stage & Status columns")
# Removing exctra columns that are nulls
Raw_Data = Raw_Data.drop(columns = ["Stage" , "Status"])
# checking Uniqe values
#print (Raw_Data["Feeding_rate"].unique())
#Raw_Data = Raw_Data.dropna()

# Removing duplicated rows
#print(Raw_Data.duplicated())
#Raw_Data.drop_duplicates(inplace = True)

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

