from preprocess import preprocessing_data
import warnings
warnings.filterwarnings('ignore')

def main():
    df_consumption = preprocessing_data()

    print(df_consumption.shape)      
if __name__ == "__main__":
    main()
