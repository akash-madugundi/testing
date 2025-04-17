# @Date: 2023-02-26
# @Description: This program checks for missing values, special missing values and generates a bargraph for the number of special missing values in each feature.
import matplotlib
matplotlib.use('Agg')  

import pandas as pd, numpy as np, io, base64, matplotlib.pyplot as plt, seaborn as sns

# Check for special missing value.
# Display a bar graph that tells the number of special missing values in each column of the dataset
def generate_bargraph_special_missing_values(df):
    special_missing_values = ['-', 'n/a', 'N/A', 'NA', '--', '?']
    pres = {num : 0 for num in df.columns if df[num].isin(special_missing_values).sum()}
    # If the graph is empty, return None
    if not pres:
        return None
    for num in df.columns:
        if df[num].isin(special_missing_values).sum():
            pres[num] = df[num].isin(special_missing_values).sum()
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

# Check for NaN values
# Display a bar graph that tells the number of NaN values in each column of the dataset
def generate_bargraph_nan_values(df):
    pres = {num : 0 for num in df.columns if df[num].isnull().sum() >0}
    # If the graph is empty, return None
    if not pres:
        return None
    for num in df.columns:
        if df[num].isnull().sum():
            pres[num] = df[num].isnull().sum()
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


# Check for special missing values
def SpecialMissingValues(df):
    s = ''; s2 = ''
    special_missing_values = ['-', 'n/a', 'N/A', 'NA', '--', '?']
    pres = {val: 0 for val in special_missing_values}
    for val in special_missing_values:
        pres[val] = df.isin([val]).sum().sum()
    sugg = ''
    splmissCols = []
    missingPer = []
    if any(pres.values()):
    #     print("There are special missing values in the dataset.")
    #     print("Number of special missing values:", sum(pres.values()))
    #     print("Percentage of special missing values:", round(sum(pres.values()) / (df.shape[0] * df.shape[1]) * 100, 2), "%")
    #     print("Special missing values in each column:")
    #     for col in df.columns:
    #         print(col, ":", df[col].isin(special_missing_values).sum())
    # else:
    #     print("There are no special missing values in the dataset.")
        s += f'''There are special missing values in the dataset.\n
    Number of special missing values: {sum(pres.values())}\n
    Percentage of special missing values: {round(sum(pres.values()) / (df.shape[0] * df.shape[1]) * 100, 2)} %\n
    Special missing values in each column:\n
    '''
        for col in df.columns:
            if df[col].isin(special_missing_values).sum():
                splmissCols.append(col)
                missingPer.append(str(df[col].isin(special_missing_values).sum()))
                s += f'''{col}: {df[col].isin(special_missing_values).sum()}\n'''
    
    # Refactorting :
        sugg + '# for each column, replace the special missing values with NaN values.\n'
        sugg += 'for col in df.columns:\n'
        sugg += '    df[col] = df[col].replace(special_missing_values, np.nan)\n'
        # sugg += '# check for NaN values again\n'
        sugg += 'df.isnull().sum().sum()\n'

        # sugg += '# for each column, replace the NaN values with the mean of the column if the column is numeric.\n'
        sugg += 'for col in df.columns:\n'
        sugg += '    if df[col].dtype == np.float64 or df[col].dtype == np.int64:\n'
        sugg += '        df[col] = df[col].fillna(df[col].mean())\n'
        # sugg += '# check for NaN values again\n'
        sugg += 'df.isnull().sum().sum()\n'

        # sugg += '# for each column, replace the NaN values with the mode of the column if the column is categorical.\n'
        sugg += 'for col in df.columns:\n'
        sugg += '    if df[col].dtype == np.object:\n'
        sugg += '        df[col] = df[col].fillna(df[col].mode()[0])\n'
        # sugg += '# check for NaN values again\n'
        
        # s += sugg
    else:
        s += "There are no special missing values in the dataset.\n"

    # Check for NaN values
    sugg_2 = ''
    if df.isnull().values.any():
        s2 += f'''There are NaN values in the dataset.\n
    Number of NaN values: {df.isnull().sum().sum()}\n
    Percentage of NaN values: {round(df.isnull().sum().sum() / (df.shape[0] * df.shape[1]) * 100, 2)} %\n
    NaN values in each column:\n
    '''
        lim = 10
        for col in df.columns:
            if df[col].isnull().sum() and lim:
                s2 += f'''{col}: {df[col].isnull().sum()}\n'''
                lim -= 1  
        if lim == 0:
            s2 += 'and few more...\n'
    # Refactoring :
        sugg_2 += '# for each column, replace the NaN values with the mean of the column if the column is numeric.\n'
        
        sugg_2 += 'for col in df.columns:\n'
        sugg_2 += '    if df[col].dtype == np.float64 or df[col].dtype == np.int64:\n'
        sugg_2 += '        df[col] = df[col].fillna(df[col].mean())\n'
        sugg_2 += '    elif df[col].dtype == np.object:\n'
        sugg_2 += '        df[col] = df[col].fillna(df[col].mode()[0])\n'
        sugg_2 += '# check for NaN values again\n'
        sugg_2 += 'df.isnull().sum().sum()\n'
        # s += sugg_2

        

    else:
        s2 += "\nThere are no NaN values in the dataset."

    return s,s2,sugg,sugg_2,splmissCols,missingPer


# Check for missing values
def missing_values(df):
    v = df.isnull().sum().sum()
    s = ''; sugg = ''; code = ''
    missCols = []
    missPer = []
    if not v:
        s += "There are no missing values in the dataset.\n"
    else:
        s += f'''There are missing values in the dataset.\n
    Number of missing values: {v}\n
    Percentage of missing values: {round(v / (df.shape[0] * df.shape[1]) * 100, 2)} %\n
    Missing values in each column:\n
    '''
        limit = 10
        for col in df.columns:
            if df[col].isnull().sum():
                missCols.append(col)
                missPer.append(str(df[col].isnull().sum()))
                s += f'''{col}: {df[col].isnull().sum()}\n'''
                if not limit:
                    break
                limit -= 1
        code += '# for each column, replace the missing values with the mean of the column if the column is numeric.\n'
        code += 'for col in df.columns:\n'
        code += '    if df[col].dtype == np.float64 or df[col].dtype == np.int64:\n'
        code += '        df[col] = df[col].fillna(df[col].mean())\n'
        code += '# check for missing values again\n'
        code += 'df.isnull().sum().sum()\n'
        code += '# for each column, replace the missing values with the mode of the column if the column is categorical.\n'
        code += 'for col in df.columns:\n'
        code += '    if df[col].dtype == np.object:\n'
        code += '        df[col] = df[col].fillna(df[col].mode()[0])\n'
        code += '# check for missing values again\n'
        code += 'df.isnull().sum().sum()\n'

    return s, code, missCols, missPer

def generate_bargraph_missing_values(df):    
    return generate_bargraph_nan_values(df)

     