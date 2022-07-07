import numpy as np
import pandas as pd


def reduce_mem_usage(df: pd.DataFrame):
    start_mem = df.memory_usage().sum() / 1024**2
    for col in df.columns:
        col_type = df[col].dtypes
        if str(col_type)[:5] == 'float':
            c_min = df[col].min()
            c_max = df[col].max()
            if c_min > np.finfo('f2').min and c_max < np.finfo('f2').max:
                df[col] = df[col].astype(np.float16)
            elif c_min > np.finfo('f4').min and c_max < np.finfo('f4').max:
                df[col] = df[col].astype(np.float32)
            else:
                df[col] = df[col].astype(np.float64)
        elif str(col_type)[:3] == 'int':
            c_min = df[col].min()
            c_max = df[col].max()
            if c_min > np.iinfo("i1").min and c_max < np.iinfo("i1").max:
                df[col] = df[col].astype(np.int8)
            elif c_min > np.iinfo("i2").min and c_max < np.iinfo("i2").max:
                df[col] = df[col].astype(np.int16)
            elif c_min > np.iinfo("i4").min and c_max < np.iinfo("i4").max:
                df[col] = df[col].astype(np.int32)
            elif c_min > np.iinfo("i8").min and c_max < np.iinfo("i8").max:
                df[col] = df[col].astype(np.int64)
        elif col == 'timestamp':
            df[col] = pd.to_datetime(df[col])
        elif str(col_type)[:8] != 'datetime':
            df[col] = df[col].astype('category')
    
    end_mem = df.memory_usage().sum() / 1024**2
    print(
        'Потребление памяти меньше на ',
        round(start_mem - end_mem, 2),
        ' Мб (-',
        round(100 * (start_mem - end_mem) / start_mem, 1),
        '%)',
        sep=''
    )
    return df


def show_inf_and_na(df: pd.DataFrame):
    pd.set_option('use_inf_as_na', True)
    for col in df.columns:
        print(col, 'Inf+NaN:', df[col].isnull().sum())
        

def inf_and_na_columns(df: pd.DataFrame):
    result = list()
    pd.set_option('use_inf_as_na', True)
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            result.append(col)
    return result
