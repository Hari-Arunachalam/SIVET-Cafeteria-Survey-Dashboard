import pandas as pd

# Load the Excel file
file_path = '/Users/hariarunachalam/Documents/Code/Data Cleaning/Canteentest.xlsx'
excel_data = pd.ExcelFile(file_path)

# Load the specific sheet
sheet_data = pd.read_excel(file_path, sheet_name='AIDED -RECORD')

# Remove columns that are entirely null
df_aided_cleaned = df_aided.dropna(axis=1, how='all')

# Correcting spelling in the relevant column
sheet_data['What type of menu do you prefer for breakfast?'] = sheet_data['What type of menu do you prefer for breakfast?'].replace({
    'PASTHA': 'Pasta',
    'BREAD OMLATTE': 'BREAD OMELETTE',
    'Biriyani': 'Biryani'
     'Tea and biscuits' 
})

#Combite to Nothing
df_aided_cleaned.replace({'No': 'Nothing', 'Noo': 'Nothing', 'none': 'Nothing', 'no idea': 'Nothing', 'Nothing': 'Nothing'}, inplace=True)

#Replace "Bread" with "Bread Omelette"
df_aided_cleaned.replace({'Bread': 'Bread Omelette'}, inplace=True)

#Replace "Vegetable rice" with "Veg rice"
df_aided_cleaned.replace({'Vegetable rice': 'Veg rice'}, inplace=True)

#Consolidate anything with "Tea" into "Tea"
df_aided_cleaned = df_aided_cleaned.applymap(lambda x: 'Tea' if isinstance(x, str) and 'Tea' in x else x)

#Add "Vegetable Biriyani" and "Vegetable Rice"
df_aided_cleaned.replace({'Vegetable Biriyani': 'Veg Biriyani', 'Vegetable Rice': 'Veg Rice'}, inplace=True)

#Combine anything with "Sambar" together
df_aided_cleaned = df_aided_cleaned.applymap(lambda x: 'Sambar' if isinstance(x, str) and 'Sambar' in x else x)

#Combine "Biriyani" and "Biryani"
df_aided_cleaned.replace({'Biryani': 'Biriyani'}, inplace=True)


# Save the cleaned sheet back into a new file
cleaned_file_path = '/Users/hariarunachalam/Documents/Code/Data Cleaning/Canteentest_cleaned.xlsx'
with pd.ExcelWriter(cleaned_file_path, engine='xlsxwriter') as writer:
    # Write the cleaned data back to the same sheet
    sheet_data.to_excel(writer, sheet_name='AIDED -RECORD', index=False)

# Provide the link to the cleaned file
cleaned_file_path
