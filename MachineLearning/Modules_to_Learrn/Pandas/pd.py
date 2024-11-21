import re

import pandas as pd

pd.set_option("display.max_columns",None)



# data = pd.read_csv("pokemon_data.csv",chunksize=5) # read the csv file


# print(data.head(1)) # (number of data you want to display) - display the first 5 datas
# print(data.columns) # display the columns header
# print(data[["Name","HP"]]) # display the specific by columns
# print(data.iloc[1:4]) # Display the row data by column or it can be slices

# for index ,row in data.iterrows(): # Display the row data by column
#     print(index,row)

# print(data.loc[data["Type 1"] == "Fire"]) # Display conditional statements

# print(data.describe()) # Describe data
# print(data.sort_values("Name",ascending=False)) # Display the data alphabetically and by number. ascending= for reverse
# print(data.sort_values(["Type 1","Generation"])) # ascending=[1 for True ,0 for False] it depends on how many parameter does the bracket have

############################################ SLICES

# datas = data.squeeze().head() ##### SQUEEZE COLUMNS INTO A 1 STRAIGHT LINE
# df = datas.to_string(index=False)
# print(df)
#
# data["Total"] = data["HP"] + data["Attack"] # Add new column
# print(data.drop(columns="Total")) # Drop a column

# # datap = zip(data["Name"],data["Type 1"])
#
# print(list(datap))

# cols = list(data.columns.values) # Provide the list of the column's header

# print(data[cols[0:4] + [cols[-1]] + cols[4:11]]) # Just slices

############################################# SAVE
# cols = list(data.columns.values)
#
# datas = data[cols[0:4] + [cols[7]]]
# datas.to_csv("My_Sample_files.csv") # Use to save the data into csv index=False to remove the index, sep= To seperate
# datas.to_excel("Sample.xlsx") # For straight excel

############################################# FILTERING DATA PART 2 BY REGEX

# datas = data.loc[(data["Type 1"] == "Grass") & (data["Type 2"] == "Poison")] # MULTI- filter data

# print(datas.reset_index()) # RESET THE INDEX #########################################
# print(datas.reset_index(drop=True)) # drop= Drop the index

# print(data.loc[data["Name"] == "Pikachu"])

# print(data.loc[data["Name"].str.contains("chu")]) # Display only the given contains, use ~ at start of the loc for reverse

# print(data.loc[data["Type 1"].str.contains("Fire|Grass",flags=re.IGNORECASE,regex=True)]) # display multi valued columns,flags=re.IGNORECASE
                                                                                            # IGNORE case
                                                                                            # Basta anything about regex for shortcut HAHAHAHA
                                                                                            # Sample pi[a-z]*


################################### CONDITIONAL DATA
# data.loc[data["Type 1"] == "Grass","Legendary"] = True # TO CHANGE DATA CONDITION BY COLUM N
# data.loc[data["Sp. Atk"] > 100,["Generation","Legendary"]] = "TEST VALUE" # TO CHANGE MULTIPLE DATA COLLECTION BY COLUMNS

################################### AGGREGATE STATISTICS

# datas = data.groupby(["Type 1","Type 2"]).count() # LITERAL NA DATASET
# print(datas)

################################### BIG DATAS BY CHUNKS

# for i,data in enumerate(pd.read_csv("pokemon_data.csv",chunksize=5)):
#     datas = data.squeeze()
#     df = datas.to_string(index=False)
#     print(f"Data {i + 1}")
#     print(df)

