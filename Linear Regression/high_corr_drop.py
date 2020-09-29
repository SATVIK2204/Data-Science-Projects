import pandas as pd
import numpy as np 

def drop_high_corr_columns(df,correlation_matrix):

    # Selecting the upper triangle of the matrix
    upper = correlation_matrix.where(np.triu(np.ones(correlation_matrix.shape), k=1).astype(np.bool))
    # Columns to drop
    to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]

    return df.drop(df[to_drop], axis=1)