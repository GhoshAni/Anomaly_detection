import os as os
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

def preprocessing_data():
    data_path = '/Users/apple/Downloads/data/'
    data = 'Electricity_Theft_Data.csv'
    #os.chdir(os.path.join(data_path))
    theft_df = pd.read_csv(os.path.join(data_path, data))
    theft_df = theft_df.dropna(thresh=180) # delete accounts where at least 6 months of energy data not available
    theft_df = theft_df.dropna(subset='CONS_NO') ## delete where account number is null
    # transform the data frame from column to rows
    transformed_df = pd.melt(frame= theft_df, id_vars=["CONS_NO", "CHK_STATE"], var_name= "date" , value_name= "consumption")

    # change the column data types and extract month, year and week
    transformed_df['CONS_NO'] = transformed_df["CONS_NO"].astype(int)
    transformed_df['CHK_STATE'] = transformed_df["CHK_STATE"].astype(int)
    transformed_df['date'] = pd.to_datetime(transformed_df['date'], infer_datetime_format= True, dayfirst= True)
    transformed_df['month'] = transformed_df['date'].dt.month
    transformed_df['year'] = transformed_df['date'].dt.year
    transformed_df['week'] = transformed_df['date'].dt.isocalendar().week

    # aggregate the median value of consumption by consumer and year impute NAN values with the imputed values
    transformed_df['Consumption_imputed_by_year'] = transformed_df.groupby(['CONS_NO', 'year'])['consumption'].transform(lambda x: x.fillna(x.median()))
    df_consumption_week = transformed_df[['CONS_NO', 'week', 'Consumption_imputed_by_year', 'CHK_STATE']]
    # the column week is modified 
    df_consumption_week.loc[:, 'week'] = df_consumption_week['week'].apply(lambda x: f'week_{str(x)}')
    # the data frame is pivoted back to its original shape
    df_consumption = pd.DataFrame(pd.pivot_table(data= df_consumption_week, index = ['CONS_NO', 'CHK_STATE'], columns= 'week',   values= 'Consumption_imputed_by_year').reset_index())
    
    return df_consumption
