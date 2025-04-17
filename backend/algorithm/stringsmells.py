# @Date: 2020-09-27
# @Description: This program checks for string smells in the dataset.

import re, matplotlib.pyplot as plt, io, base64, numpy as np, pandas as pd

integer_as_string_present = False
def detect_binary_missing_values(df):
    """
    Detect columns with mostly missing values, but where all non-missing values are 'Y'.
    This implies that missing values might represent 'N' vs truly missing data.
    """
    binary_missing_features = []
    code = ''
    s = ''
    try:
        for col in df.columns:
            # Calculate fraction of missing values
            fraction_missing = df[col].isna().mean()
            # Check if at least 90% are missing
            if fraction_missing >= 0.9:
                non_missing_vals = df[col].dropna().unique()
                # If all non-missing values are 'Y', consider this a binary missing column
                if len(non_missing_vals) == 1 and non_missing_vals[0] == 'Y':
                    binary_missing_features.append(col)

        if binary_missing_features:
            s = "There are columns with mostly missing values, but the non-missing values are 'Y'.\n"
            s += "Affected columns: " + str(binary_missing_features[:8])
            if len(binary_missing_features) > 8:
                s += "...\n"
            else:
                s += "\n"
            s += "These missing values may implicitly indicate 'N'.\n"

            code += f'''
# Example refactoring: Convert missing values to 'N' for columns identified
binary_missing_columns = {binary_missing_features}
for col in binary_missing_columns:
    df[col] = df[col].fillna('N')  # Treat missing as 'N'
'''
        else:
            s = "No columns with binary missing values detected.\n"
        return s, code

    except Exception as e:
        return f"Error in detect_binary_missing_values: {{str(e)}}\\n", ""

def refactor_binary_missing_values(df):
    """
    Refactor columns with binary missing values by filling missing entries with 'N'.
    """
    try:
        for col in df.columns:
            df[col] = df[col].fillna('N')  # Treat missing as 'N'
        return df
    except Exception as e:
        print(f"Error in refactor_binary_missing_values: {str(e)}")
        return df
def detect_unique_values(df):
    unique_identifier_features = []
    code = ''
    s = ''
    try:
        for col in df.columns:
            # Check if column is a unique identifier (all rows distinct)
            if df[col].nunique() == len(df):
                unique_identifier_features.append(col)

        if unique_identifier_features:
            s = "There are columns containing unique identifiers (uids) in the dataset.\n"
            s += "Affected columns: " + str(unique_identifier_features[:8])
            if len(unique_identifier_features) > 8:
                s += "...\n"
            else:
                s += "\n"
            s += "These columns appear to hold a primary key or unique ID.\n"

            code += f'''
# Example refactoring: drop or manage unique identifier columns
uid_columns = {unique_identifier_features}
df = df.drop(columns=uid_columns)  # if not needed
'''
        else:
            s = "No unique identifier columns detected.\n"
        return s, code

    except Exception as e:
        return f"Error in detect_unique_values: {str(e)}\n", ""

def refactor_unique_values(df):
    try:
        for col in df.columns:
            if df[col].nunique() == len(df):
                df = df.drop(columns=[col])
        return df
    except Exception as e:
        print(f"Error in refactor_unique_values: {str(e)}")
        return df


def detect_integer_as_string(df):
    integer_string_features = []
    code = ''; s = ''
    try:
        for col in df.columns:
            print("-----------------------*****************----------------------------------")
            print(type(df[col][1]))
            if df[col].dtype == 'object':
                print("-----------------------*****************----------------------------------")
                print(df[col][1])
                # Check each cell in the column for quoted integers
                def check_cell(cell):
                    if isinstance(cell, str):
                        return bool(re.match('^\d+$', cell))
                    return False
                
                if df[col].apply(check_cell).any():
                    integer_string_features.append(col)
        
        if len(integer_string_features) > 0:
            global integer_as_string_present
            integer_as_string_present = True
            s = "There are features with integers stored as strings in the dataset.\n"
            # ...existing code...
            s += "Affected features: " + str(integer_string_features[:len(integer_string_features)])
            if len(integer_string_features) > 8:
                s += "...\n"
            else:
                s += "\n"
            s += f' Code for refactoring: \n'
            code += f'''
    # Convert string integers to proper integer type
    for col in df.columns:
        if df[col].dtype == 'object':
            if df[col].dropna().str.match('^\d+$').all():
                df[col] = pd.to_numeric(df[col], errors='coerce')
    '''
        else:
            s = "No integers stored as strings detected in the dataset.\n"
        return s, code
    except Exception as e:
        return f"Error in detect_integer_as_string: {str(e)}\n", ""

special_char_present = False
# @Description: To check for special characters in the dataset
def detect_special_characters(df):
    special_char_features = []
    code = ''; s = ''
    try :
        for col in df.columns:
            if df[col].dtype == 'object':
                pattern = re.compile('[^A-Za-z0-9\s]+')
                match = pattern.search(df[col].iloc[0])
                if match:
                    special_char_features.append(col)
        if len(special_char_features) > 0:
            global special_char_present; special_char_present = True
            s = "There are features with special characters in the dataset.\n"
            s += "Features with special characters: " + str(special_char_features[:8] )
            if len(special_char_features) > 8:
                s += "...\n"
            else:
                s += "\n"
            s+= f' Code for refactoring: \n'
            code += f'''
    for col in df.columns:
        if df[col].dtype == 'object':
            pattern = re.compile('[^A-Za-z0-9\s]+')
            match = pattern.search(df[col].iloc[0])
            if match:
                # remove special characters
                df[col] = df[col].str.replace('[^A-Za-z0-9\s]+', '')
                # remove leading and trailing spaces
                df[col] = df[col].str.strip()
                # convert to lowercase
                df[col] = df[col].str.lower()
                print(df[col].head())\n'''
        else:
            s = "There are no features with special characters in the dataset."
    except Exception as e:
        s = "There are no features with special characters in the dataset."
        # s = "Nil."
        # print(e)
    return s, code


# @Description: This function generates a bargraph for the number of special characters in each feature.
def generate_bargraph_special_characters(df):
    if not special_char_present:
        return None
    try:
        pres = {num : 0 for num in df.columns if df[num].str.contains('[^A-Za-z0-9\s]+').sum()}
        for num in df.columns:
            if df[num].str.contains('[^A-Za-z0-9\s]+').sum():
                pres[num] = df[num].str.contains('[^A-Za-z0-9\s]+').sum()
        plt.bar(pres.keys(), pres.values())
        plt.xticks(rotation=90)
        # Save the plot to a BytesIO object
        img_bytes = io.BytesIO()
        plt.savefig(img_bytes, format='png')
        img_bytes.seek(0)
        # Encode the image data as base64 string
        img_base64 = base64.b64encode(img_bytes.read()).decode('utf-8')
        plt.close()

        return img_base64
    
    except Exception as e:
        # print(e)
        return None
    

def refactor_special_char(df):
    try:
        for col in df.columns:
            if df[col].dtype == 'object':
                pattern = re.compile('[^A-Za-z0-9\s]+')
                match = pattern.search(df[col].iloc[0])
                if match:
                    # Remove special characters
                    df[col] = df[col].str.replace('[^A-Za-z0-9\s]+', '', regex=True)
                    # Remove leading and trailing spaces
                    df[col] = df[col].str.strip()
                    # Convert to lowercase
                    df[col] = df[col].str.lower()
        return df
    except Exception as e:
        return df


def refactor_integer_as_string(df):
    try:
        for col in df.columns:
            if df[col].dtype == 'object':
                def convert_cell(cell):
                    if isinstance(cell, str):
                        # Check if string contains only digits
                        if cell.strip().isdigit():
                            return int(cell)
                    return cell
                
                # Apply conversion to each cell individually
                df[col] = df[col].apply(convert_cell)
        return df
    except Exception as e:
        print(f"Error in refactor_integer_as_string: {str(e)}")
        return df
# Detecting Trailng Spaces
'''# create a list to store the column names with trailing spaces
cols_with_trailing_spaces = []

# loop through each column in the dataset
for col in df.columns:
    # check if the column is a string type
    if df[col].dtype == 'object':
        # check if the column contains trailing spaces
        if df[col].str.endswith(' ').any():
            cols_with_trailing_spaces.append(col)

# print the columns with trailing spaces
if len(cols_with_trailing_spaces) > 0:
    print("There are columns with trailing spaces in the dataset.")
    print("Columns with trailing spaces:", cols_with_trailing_spaces)
else:
    print("There are no columns with trailing spaces in the dataset.")

    
# Check for different string interpretations due to capital letters usage
for col in df.select_dtypes(include=['object']):
    unique_vals = df[col].str.lower().unique()
    if len(unique_vals) != len(set(unique_vals)):
        print(f"Column '{col}' contains different string interpretations due to capital letters usage")'''

trailing_spaces_present = False
# @Description: This function detects trailing spaces in the dataset.
def trailing_spaces(df):
    code = ''; s = ''
    try:
        cols_with_trailing_spaces = []
        for col in df.columns:
            if df[col].dtype == 'object':
                if df[col].str.endswith(' ').any():
                    cols_with_trailing_spaces.append(col)
        if len(cols_with_trailing_spaces) > 0:
            global trailing_spaces_present; trailing_spaces_present = True
            s = "There are columns with trailing spaces in the dataset."
            s += "Columns with trailing spaces: " + str(cols_with_trailing_spaces[:8])
            if len(cols_with_trailing_spaces) > 8:
                s += "...\n"
            s+= f' Code for refactoring: \n'
            code += f'''
    # # refactoring: 
    # for col in df.select_dtypes(include=['object']):
    #     df[col] = df[col].str.strip()'''
        else:
            s = "There are no columns with trailing spaces in the dataset."
    except Exception as e:
        s = "There are no columns with trailing spaces in the dataset."
        # s = "Nil."
        # print(e)
    return s, code

def refactor_trailing_spaces(df):
    try:
        # Loop through each column and remove trailing spaces from string columns
        for col in df.columns:
            if df[col].dtype == 'object':  # Only consider object (string) columns
                df[col] = df[col].str.strip()  # Remove leading and trailing spaces
        return df
    except Exception as e:
        # If any exception occurs, return the original dataframe
        return df


# @Description: This function generates a bargraph for the number of trailing spaces in each feature.
def generate_bargraph_trailing_spaces(df):
    global trailing_spaces_present
    if not trailing_spaces_present:
        return None
    try: 
        pres = {num : 0 for num in df.columns if df[num].str.endswith(' ').sum()}
        for num in df.columns:
            if df[num].str.endswith(' ').sum():
                pres[num] = df[num].str.endswith(' ').sum()
        plt.bar(pres.keys(), pres.values())
        plt.xticks(rotation=90)
        # Save the plot to a BytesIO object
        img_bytes = io.BytesIO()
        plt.savefig(img_bytes, format='png')
        img_bytes.seek(0)
        # Encode the image data as base64 string
        img_base64 = base64.b64encode(img_bytes.read()).decode('utf-8')
        plt.close()

        return img_base64
    except Exception as e:
        return None

# Strings in Human Friendly Format

human_friendly_present = False
def human_friendly(df):
    code = ''; s = ''

    pattern = r'^\d{1,3}(,\d{3})*(\.\d+)?$'
    hum = False
    for col in df.columns:
        if df[col].dtype == 'object':
            if df[col].str.match(pattern).all():
                hum = True
    if hum:
        global human_friendly_present; human_friendly_present = True
        s = "There are human-friendly formats in the dataset."
        s+= f' Code for refactoring: \n'
        code += f'''
# # refactoring:
for col in df.columns:
    if df[col].dtype == 'object':
        if df[col].str.match(pattern).all():
            # detected human-friendly format
            # Convert human-friendly format to float
            df[col] = df[col].str.replace(',', '').astype(float)'''
    else:
        s = "There are no human-friendly formats in the dataset."
    return s, code

def refactor_human_friendly(df):
    try:
        pattern = r'^\d{1,3}(,\d{3})*(\.\d+)?$'
        for col in df.columns:
            if df[col].dtype == 'object':
                if df[col].str.match(pattern).all():
                    # Remove commas and convert to float
                    df[col] = df[col].str.replace(',', '').astype(float)
        return df
    except Exception as e:
        return df

def generate_bargraph_human_friendly(df):
    if not human_friendly_present:
        return None
    pattern = r'^\d{1,3}(,\d{3})*(\.\d+)?$'
    pres = {num : 0 for num in df.columns if df[num].str.match(pattern).all()}
    for num in df.columns:
        if df[num].str.match(pattern).all():
            pres[num] = df[num].str.match(pattern).all().sum()
    plt.bar(pres.keys(), pres.values())
    plt.xticks(rotation=90)
    # Save the plot to a BytesIO object
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    # Encode the image data as base64 string
    img_base64 = base64.b64encode(img_bytes.read()).decode('utf-8')
    plt.close()

    return img_base64


