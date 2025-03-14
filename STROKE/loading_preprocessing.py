#libraries importation
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


#There is a little bit of a problem in the gender column to fix ths we drop the row with other as the entry to avoid cases of bias
data=data.drop(data.loc[data['gender']=="Other"].index[0],axis=0)
data['gender'].value_counts()


class data_loading_EDA:
    def __init__(self):
        """This function is used to load the data and
        also to initialize the data"""
        #data loading
        self.data=pd.read_csv("c:\\Users\\ADMIN\\AppData\\Local\\Temp\\Rar$DRa9180.46242\\healthcare-dataset-stroke-data.csv")
        self.columns=data.columns
        self.data_types=data.dtypes
        self.size=data.size
        self.shape=data.shape
    
    def describe(self):
        """This function is used to describe the data"""
        return self.data.describe()

    def info(self):
        """This function is used to get the information about the data"""
        return self.data.info()

    def head(self):
        """This function is used to get the first five rows of the data"""
        return self.data.head()

    def value_counts(self):
        """This function is used to get the value counts of the data"""
        return self.data.value_counts()
    

    def convert_to_categorical(self):
        """This function is used to convert datatypes from 
        object to categorical both ordered and unordered"""\

        #local variables
        unordered_categories=['gender','ever_married','work_type','']
        ordered_categories={'Residence_type':['Rural','Urban'],
                    "smoking_status":['never smoked','Unknown','formerly smoked','smokes'],
                    'heart_disease':[0,1],
                    'hypertension':[0,1],
                    'stroke':[0,1]}    

        for i in self.data.columns:
            if i in ordered_categories.keys():
                self.data[i]=pd.Categorical(self.data[i],ordered=True,categories=ordered_categories[i])
            elif i in unordered_categories:
                self.data[i]=pd.Categorical(self.data[i],ordered=False)
        return self.data

    def remove_duplicates(self)->pd.DataFrame:
        """
          This function is used to check for duplicates based on the id column 
          which should be a unique identifier for each.
        """
        self.data=self.data.drop_duplicates() 
        return self.data


   

    def dealing_with_missing(self):     
        """This function is used to check for missingness in the
        pandas dataframe object from a given column
        """
        return self.data.isnull().sum()

    def quantile(self, column_name: str, number:float) -> str:
      """
      Calculate quantiles for a specified column.
    
      Parameters:
      -----------
      column_name : str
        The name of the column to calculate quantiles for"""
        
      if column_name not in self.data.columns:
        raise KeyError(f"Column '{column_name}' not found in DataFrame")
        
      # Ensure we're working with numeric data
      self.data[column_name] = pd.to_numeric(self.data[column_name])
      return f"{number}:{self.data[column_name].quantile(number)} "

    def removeAgeOutliers(self):
        """This function is used to remove outliers from the age column
           It does this by filtering the data from 3-100 years
        """
        self.data=self.data[(self.data['age']>=3) & (self.data['age']<=100)]
        return self.data
    def round(self, column_name: str, decimals: int) -> pd.DataFrame:
      """
      Round the values in a specified column to a given number of decimal places.   
      Raises:
      -------
      KeyError
        If column_name doesn't exist in the DataFrame
      ValueError
        If the column is not numeric
      """
      if column_name not in self.data.columns:
        raise KeyError(f"Column '{column_name}' not found in DataFrame")
        
      # if not np.issubdtype(self.data[column_name].dtype, np.number):
      #   raise ValueError(f"Column '{column_name}' must be numeric")
    
      self.data[column_name] = np.round(self.data[column_name], decimals=decimals)
      self.data[column_name] = self.data[column_name].astype(float)
      return self.data


#distributions kinda do remain same

data_obj=data_preprocessing1(data)        
data=data_obj.convert_to_categorical()
data.dtypes