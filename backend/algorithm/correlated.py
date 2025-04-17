import matplotlib
matplotlib.use('Agg')  

import pandas as pd
import numpy as np
import io
import base64
import matplotlib.pyplot as plt
import seaborn as sns

def generate_heatmap(df):
    # Select only numeric columns
    df_numeric = df.select_dtypes(include=[np.number])
    # Compute the correlation matrix
    corr = df_numeric.corr()

    if corr.empty:
        return None
    
    plt.imshow(corr, cmap='coolwarm', interpolation='none')
    plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
    plt.yticks(range(len(corr.columns)), corr.columns)
    plt.colorbar()

    # Save the plot to a BytesIO object
    img_bytes = io.BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)

    # Encode the image data as base64 string
    img_base64 = base64.b64encode(img_bytes.read()).decode('utf-8')
    plt.close()
    
    return img_base64


def correlated(df):
    # Select only numeric columns
    df_numeric = df.select_dtypes(include=[np.number])
    # Compute the correlation matrix
    corr_matrix = df_numeric.corr()
    
    instr = []
    if corr_matrix.empty:
        instr.append("There are no highly correlated features in the dataset.\n")
        return instr

    # Identify highly correlated features
    high_corr_features = set()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > 0.7:  # Change threshold value as needed
                colname = corr_matrix.columns[i]
                high_corr_features.add(colname)

    # Maximum correlation value among any two values
    max_corr = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(np.bool_)).stack().max()
    instr.append("Maximum correlation value among any two distinct values: " + str(max_corr) + "\n")

    if len(high_corr_features) > 0:
        instr.extend([
            "There are highly correlated features in the dataset.\n",
            "Number of highly correlated features: " + str(len(high_corr_features)) + "\n",
            "Highly correlated features: " + str(high_corr_features) + "\n"
        ])
    else:
        instr.append("There are no highly correlated features in the dataset.\n")

    return instr
