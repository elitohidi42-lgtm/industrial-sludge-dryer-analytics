import pandas as pd


### Reading csv file


Raw_Data = pd.read_csv("Raw_data.csv")

# Assigning predefined column names because the exported HMI file contains two unnamed columns.
Raw_Data = pd.DataFrame(Raw_Data , columns = ["Time","Feedingscrew_F","Feedingscrew_Am","Rotarywing_F",
                                                  "Rotarywing_Am","Idfan_F","Idfan_Am","Temp_Inlet" ,
                                                  "Temp_Outlet","Temp_Exhaust","Feed(kg/min)","Stage"
                                                  ,"Status"])



### Data Prepration


# Rename the columns name
Raw_Data = Raw_Data.rename(columns={"Feedingscrew_F": "feedingscrew_fereq",
                                     "Feedingscrew_Am": "feedingscrew_ampes" , 
                                     "Rotarywing_F": "rotarywing_fereq",
                                     "Rotarywing_Am": "rotarywing_ampes" , 
                                     "Idfan_F": "idfan_fereq" ,
                                     "Idfan_Am": "idfan_ampes",
                                     "Temp_Inlet": "temp_inlet" ,
                                     "Temp_Outlet": "temp_outlet" ,
                                     "Temp_Exhaust": "temp_exhaust" ,
                                     "Feed(kg/min)": "feeding_rate"})



# Data inspection in first stage
print (f" the data shape is:\n {Raw_Data.shape}")
print (f" data type in columns is:\n {Raw_Data.dtypes}")

#  Nulls Report & Desicioning
null_report = pd.DataFrame({
    "Null Count": Raw_Data.isnull().sum(),
    "Null Percent": (Raw_Data.isnull().mean() * 100).round(2)})
print (f"here is null reports:\n {null_report} ")

#checking Uniqe values
print (f"the uniqe value of Feeding rate is:{Raw_Data["feeding_rate"].unique()} the feeding rate is increased and decreased in a stepwise manner." )

# Removing exctra columns that are nulls
print (f'\n based on the null & uniqe values two columns {"Stage" , "Status"} will be deleted')
Raw_Data = Raw_Data.drop(columns = ["Stage" , "Status"])


### Time column
Raw_Data["Time"] = pd.to_datetime(Raw_Data["Time"])
Raw_Data = Raw_Data.set_index("Time")


### Data Validation


# Range of numeric parameters
summary = pd.DataFrame({
    "Min": Raw_Data.min(numeric_only=True),
    "Max": Raw_Data.max(numeric_only=True),
})
summary["Range"] = summary["Max"] - summary["Min"]
print(summary)

# Parameter modification (rotarywing_ampes)
print (Raw_Data.loc[Raw_Data["rotarywing_ampes"] < 0, "rotarywing_ampes"].describe())
Raw_Data.loc[Raw_Data["rotarywing_ampes"] < 0, "rotarywing_ampes"] = 0

# checking valuse
print (Raw_Data.dtypes)
print (Raw_Data.info())
print (Raw_Data.describe())
print (Raw_Data.tail(6))
print (Raw_Data.head(11))