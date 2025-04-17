def duplicated(df):
    duplicates = df.duplicated()
    instr = ''
    if any(duplicates):
        # Print information about duplicates
        instr += "Duplicate examples are present in the dataset.\n"
        instr += "Number of duplicate examples: " + str(duplicates.sum()) + "\n"
        instr += f"Percentage of duplicate examples: {round(duplicates.sum() / df.shape[0] * 100, 3)} %\n"
        dl = df.index[duplicates].tolist()
        instr += "Indices of duplicate examples: " + str(dl[: min(len(dl), 30)]) + "\n"
        if len(dl) > 30:
            instr += "(Only the first 30 duplicate examples are shown.)\n"
        
        # Removing duplicates
        df_cleaned = df.drop_duplicates()
        instr += "\nDuplicates have been removed from the dataset."
        
    else:
        instr += "There are no duplicate examples in the dataset.\n"
        df_cleaned = df

    return instr, df_cleaned
