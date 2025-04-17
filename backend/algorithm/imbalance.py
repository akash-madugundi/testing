# @Date: 2023-03-06
# @Title: This program checks for class imbalance and binary categorical columns with high cardinality in the dataset.
# It also contains the code to generate infographs for the dataset


import numpy as np, matplotlib.pyplot as plt, io, base64
import pandas as pd
from sklearn.utils import resample

'''for col in df.columns:
    # check if the column is categorical
    if df[col].dtype == 'object':
        # check the number of unique values
        unique_vals = len(df[col].unique())
        # set a threshold for high cardinality
        threshold = 10
        if unique_vals > threshold:
            print(f"The '{col}' column has high cardinality with {unique_vals} unique values.")'''
bin_cat_present = False
# @Use: To check for binary categorical columns with high cardinality in the dataset
def binning_cat(df):
    present = False
    binCols = []
    unqVals = []
    s = ''; code = '' 
    # for each column, check if the column is categorical
    for col in df.columns:
        if df[col].dtype == 'object':
            # check the number of unique values
            unique_vals = len(df[col].unique())
            # set a threshold for high cardinality
            threshold = 20
            if unique_vals > threshold:
                binCols.append(col)
                unqVals.append(str(unique_vals))
                present = True; global bin_cat_present; bin_cat_present = True
                # print(f"The '{col}' column has high cardinality with {unique_vals} unique values.")
                s += f'''The '{col}' column has high cardinality with {unique_vals} unique values.\n
                '''


                # # create a list of the top 10 most frequent categories
                # top_10 = df[col].value_counts().sort_values(ascending=False).head(10).index
                # # replace all other categories with 'Other'
                # df[col] = np.where(df[col].isin(top_10), df[col], 'Other')
                # # check if the code worked
                # print(df[col].value_counts())
                # print()

    if present == False:
        s += '''No categorical column with high cardinality'''
    else:
        s += f'The following code can be used to bin the categorical columns with high cardinality:'
        code += f'''
for col in df.columns:
    if df[col].dtype == 'object':
        unique_vals = len(df[col].unique())
        threshold = 10
        if unique_vals > threshold:
            # create a list of the top 10 most frequent categories
            top_10 = df[col].value_counts().sort_values(ascending=False).head(10).index
            # replace all other categories with 'Other'
            df[col] = np.where(df[col].isin(top_10), df[col], 'Other')
            # check if the code worked
            print(df[col].value_counts())
            print()\n'''

    return s, code, binCols, unqVals


def refactor_binning_cat(df):
    present = False
    binCols = []
    unqVals = []
    s = ''; code = '' 
    # for each column, check if the column is categorical
    for col in df.columns:
        if df[col].dtype == 'object':
            unique_vals = len(df[col].unique())
            threshold = 10
            if unique_vals > threshold:
                # create a list of the top 10 most frequent categories
                top_10 = df[col].value_counts().sort_values(ascending=False).head(10).index
                # replace all other categories with 'Other'
                df[col] = np.where(df[col].isin(top_10), df[col], 'Other')
                print(df[col].value_counts())
                print()
    return df

'''Refer this:
imb = False; nu = 1
# Check for class imbalance
for col in df.columns:
    class_counts = df[col].value_counts()
    if class_counts.min() / class_counts.max() < 0.1 and not col in ['Date', 'Time', 'Name' ]:
            # if all values are unique, then continue
        if  len(df[col].unique()) == len(df):
            continue
        # print(f"{nu}) Class imbalance detected in column {col} with ", end= '')
        imb = True        
        # print("Class imbalance ratio:", round(class_counts.min() / class_counts.max(), 2),'\n')
        nu += 1
        # ck = class_counts.to_dict()
        # # print few elements of dictionary
        # print("Class counts:", {k: ck[k] for k in list(ck)[:5]}, '... etc')

if imb:
    print("Potential mitigation strategies:")
    print("- Use appropriate sampling techniques to balance the classes.")
    print("- Use appropriate evaluation metrics like F1 score, precision, recall, etc. as accuracy is not a good metric for imbalanced datasets.")
    print("- Use appropriate regularization techniques like class weights to combat bias.")
else:
    print("There is no class imbalance in the dataset.")
    print("No mitigation strategies are required.")
'''
class_imbal_present = False
# @Use: To check for class imbalance in the dataset
def class_imbal(df, threshold = 0.01):
    global class_imbal_present
    s = ''; code = ''; nu = 1
    imbCols = []
    imbRatio = []
    # Check for class imbalance
    for col in df.columns:
        class_counts = df[col].value_counts()
        if class_counts.min() / class_counts.max() < threshold and not col in ['Date', 'Time', 'Name' ]:
                # if all values are unique, then continue
            if  len(df[col].unique()) == len(df) or len(df[col].unique()) >= 5:
                continue
            class_imbal_present = True
            imbCols.append(col)
            imbRatio.append(str(round(class_counts.min() / class_counts.max(), 2)))
            s += f"{nu}) Class imbalance detected in column {col} with Class imbalance ratio: {round(class_counts.min() / class_counts.max(), 2)}\n"
            nu += 1
            # ck = class_counts.to_dict()
            # # print few elements of dictionary
            # print("Class counts:", {k: ck[k] for k in list(ck)[:5]}, '... etc')

    if class_imbal_present:
        s += f'''Potential mitigation strategies:
        - Use appropriate sampling techniques to balance the classes.   
        - Use appropriate evaluation metrics like F1 score, precision, recall, \netc. as accuracy is not a good metric for imbalanced datasets.
        - Use appropriate regularization techniques like class weights to combat bias.\n'''

    else:
        s += f'''There is no class imbalance in the dataset.
        No mitigation strategies are required.\n'''

    return s, code, imbCols, imbRatio

def refactor_class_imbal(df, threshold=0.1):
    imbCols = []
    
    for col in df.columns:
        if  len(df[col].unique()) == len(df) or len(df[col].unique()) >= 5:
                continue
        class_counts = df[col].value_counts()
        if class_counts.min() / class_counts.max() < threshold and len(df[col].unique()) != len(df):
            imbCols.append(col)
            # Resampling to handle class imbalance
            major_class = class_counts.idxmax()
            minor_class = class_counts.idxmin()

            # Separate the majority and minority classes
            df_majority = df[df[col] == major_class]
            df_minority = df[df[col] == minor_class]

            # Upsample the minority class to match the majority class size
            df_minority_upsampled = resample(df_minority,
                                             replace=True,  # Sample with replacement
                                             n_samples=(len(df_majority)-len(df_minority))/10,  # Match the majority class size
                                             random_state=42)  # For reproducibility

            # Combine the majority class with the upsampled minority class
            df = pd.concat([df, df_minority_upsampled])

    return df



def generate_bargraph_class_imbal(df, threshold = 0.1):
    # The bar graph show show the ratio of max_count/(min_count + 1) for culprit columns

    pres = {num : 0 for num in df.columns if df[num].dtype != 'object' and not num in ['Date', 'Time', 'Name' ] and len(df[num].unique()) != len(df) and df[num].value_counts().min() / (df[num].value_counts().max() + 1 ) < threshold}
    # If the graph is empty, return None
    if not pres:
        return None
    global class_imbal_present
    if class_imbal_present == False:
        return None
    
    for num in df.columns:
        if df[num].dtype != 'object' and not num in ['Date', 'Time', 'Name' ] and len(df[num].unique()) != len(df) and df[num].value_counts().min() / (df[num].value_counts().max() + 1 ) < threshold:
            pres[num] = df[num].value_counts().max() / (df[num].value_counts().min() + 1 )
    plt.bar(pres.keys(), pres.values())
    plt.xticks(rotation=90)
    # Save the plot to a BytesIO object
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    # Seek to the start of the stream
    img_bytes.seek(0)
    img_base64 = base64.b64encode(img_bytes.read()).decode('utf-8')
    plt.close()

    return img_base64


# @Use: To generate a bar graph for categorical columns with high cardinality
def generate_bargraph_binning_cat(df):
    # Check for categorical column with high cardinality.
    # Display a bar graph that tells the number of special missing values in each column of the dataset
    pres = {num : 0 for num in df.columns if df[num].dtype == 'object' and len(df[num].unique()) > 10}
    # If the graph is empty, return None
    if not pres:
        return None
    global bin_cat_present
    if bin_cat_present == False:
        return None
    for num in df.columns:
        if df[num].dtype == 'object' and len(df[num].unique()) > 10:
            pres[num] = len(df[num].unique())
    plt.bar(pres.keys(), pres.values())
    plt.xticks(rotation=45)
    # Save the plot to a BytesIO object
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    # Encode the image data as base64 string
    img_base64 = base64.b64encode(img_bytes.read()).decode('utf-8')
    plt.close()

    return img_base64
    
            