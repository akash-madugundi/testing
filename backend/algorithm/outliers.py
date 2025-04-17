# @Date: 2023-03-06
# @Title: This program checks for outliers in the dataset.

import pandas as pd, numpy as np, io, base64, matplotlib.pyplot as plt, seaborn as sns

# To generate the boxplot for the outliers
def generate_boxplot(df):
    # sns.boxplot(data=df.select_dtypes(include=['float64', 'int64']))
    # check if there are columns with the right data type
    if df.select_dtypes(include=['float64', 'int64']).shape[1] > 0:
        sns.boxplot(data=df.select_dtypes(include=['float64', 'int64']))
    else:
        # sns.boxplot(data=df)
        return None
    plt.xticks(rotation=90)
    # Save the plot to a BytesIO object
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    # Encode the image data as base64 string
    img_base64 = base64.b64encode(img_bytes.read()).decode('utf-8')
    plt.close()
    return img_base64

# To check the outliers in the dataset
def Outliers(df):
    instr = ''
    # print("Outliers:")
    instr += str("Outliers:\n")
    present = False
    num_outliers = 0
    total_size = 0
    for col in df.columns:
        if df[col].dtype == np.float64 or df[col].dtype == np.int64:
            # # print(col)
            # instr += str(col + "\n")
            # # print("Mean:", df[col].mean())
            # instr += str("Mean: " + str(df[col].mean()) + "\n")
            # # print("Standard deviation:", df[col].std())
            # instr += str("Standard deviation: " + str(df[col].std()) + "\n")
            # # print("Minimum value:", df[col].min())
            # instr += str("Minimum value: " + str(df[col].min()) + "\n")
            # # print("Maximum value:", df[col].max())
            # instr += str("Maximum value: " + str(df[col].max()) + "\n")
            # # print("Number of outliers:", df[(df[col] < df[col].mean() - 3 * df[col].std()) | (df[col] > df[col].mean() + 3 * df[col].std())].shape[0])
            # instr += str("Number of outliers: " + str(df[(df[col] < df[col].mean() - 3 * df[col].std()) | (df[col] > df[col].mean() + 3 * df[col].std())].shape[0]) + "\n")
            num_outliers += df[(df[col] < df[col].mean() - 3 * df[col].std()) | (df[col] > df[col].mean() + 3 * df[col].std())].shape[0]
            # # print("Percentage of outliers:", round(df[(df[col] < df[col].mean() - 3 * df[col].std()) | (df[col] > df[col].mean() + 3 * df[col].std())].shape[0] / df.shape[0] * 100, 2), "%")
            total_size += df.shape[0]
            # instr += str("Percentage of outliers: " + str(round(df[(df[col] < df[col].mean() - 3 * df[col].std()) | (df[col] > df[col].mean() + 3 * df[col].std())].shape[0] / df.shape[0] * 100, 2)) + " %\n")
            # # print("Indices of outliers:", df[(df[col] < df[col].mean() - 3 * df[col].std()) | (df[col] > df[col].mean() + 3 * df[col].std())].index.tolist())
            # ol = df[(df[col] < df[col].mean() - 3 * df[col].std()) | (df[col] > df[col].mean() + 3 * df[col].std())].index.tolist()
            # instr += str("Indices of outliers(first 20): " + str(ol[:min(20, len(ol))]) + "\n")
            # # print()
            # instr += str("\n")
            if df[(df[col] < df[col].mean() - 3 * df[col].std()) | (df[col] > df[col].mean() + 3 * df[col].std())].shape[0] > 0:
                present = True
    # print("Number of outliers:", num_outliers)
    instr += str("Number of outliers: " + str(num_outliers) + "\n")
    # print("Percentage of outliers:", round(num_outliers / total_size * 100, 2), "%")
    if total_size == 0:
        instr += str("Percentage of outliers: 0 %\n")
    else:
        instr += str("Percentage of outliers: " + str(round(num_outliers / total_size * 100)) + " %\n")
    sugg = ''; code = ''
    if not present:
        # print("There are no outliers in the dataset.")
        sugg += str("There are no outliers in the dataset.\n")

    else:
        # print("There are outliers in the dataset.")
        sugg += str("There are outliers in the dataset.\n")
        # # statistics:
        # sugg += f'Number of outliers: {df[(df[col] < df[col].mean() - 3 * df[col].std()) | (df[col] > df[col].mean() + 3 * df[col].std())].shape[0]}\n'
        # sugg += f'Percentage of outliers: {round(df[(df[col] < df[col].mean() - 3 * df[col].std()) | (df[col] > df[col].mean() + 3 * df[col].std())].shape[0] / df.shape[0] * 100)}%\n'
        # # print("You can remove the outliers from the dataset using the following code:")
        sugg += str("You can remove the outliers from the dataset using the following code:\n")
        code += '''# Remove outliers
initial_shape = df.shape
for col in df.columns:
    if df[col].dtype == np.float64 or df[col].dtype == np.int64:
        df = df[(df[col] >= df[col].mean() - 3 * df[col].std()) 
        & (df[col] <= df[col].mean() + 3 * df[col].std())]
        # print("Number of outliers removed from", col + ":", initial_shape[0] - df.shape[0])
        # print("Percentage of outliers removed from", col + ":",
        # round((initial_shape[0] - df.shape[0]) / initial_shape[0] * 100, 2), "%")

            '''
        
    instr += sugg
    return instr, sugg, code



def refactor_outliers(df):
    try:
        # Loop through each column to detect and remove outliers for numerical columns
        for col in df.columns:
            if df[col].dtype == np.float64 or df[col].dtype == np.int64:
                # Calculate the mean and standard deviation for outlier detection
                mean = df[col].mean()
                std_dev = df[col].std()
                # Remove the outliers based on the 3-sigma rule
                df = df[(df[col] >= mean - 3 * std_dev) & (df[col] <= mean + 3 * std_dev)]
        return df
    except Exception as e:
        # In case of any exception, return the original dataframe
        return df
