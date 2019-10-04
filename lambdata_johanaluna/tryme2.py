# Import libraries
import pandas
import numpy
from sklearn.model_selection import train_test_split

class Check_Data():

    def __init__(self, df, name_column_target):
        self.df = df
        self.name_column_target = name_column_target

    # function to check the null in a data frame and report how many nulls it found
    def reportnulls(self):
        """
        Takes a data frame and check de nulls and sum
        the resutls and organizes them from highest to lowest
        """
        self.null_counts = self.df.isnull().sum().sort_values(ascending=False)

        # return count of null values
        return self.null_counts

    """
    function to split the data into train, validation and test
    this function split the data in 80% 20%
    that means that the target corresponds to 20%
    of the complete data frame
    """


    def splitdata(self):

        print('shape of your data frame: ', self.df.shape)
        # Define X and y
        self.X = self.df.drop(columns=self.name_column_target)
        self.y = self.df[self.name_column_target]

        # we need to do 2 splits
        # 1.(Takes X and y into X_trainval, X_test, y_trainval, y_test)
        self.X_trainval, self.X_test, self.y_trainval, self.y_test = train_test_split(
            self.X, self.y, train_size=0.80, test_size=0.20, random_state=42)

        # 2.(Takes X_trainval, y_trainval and split data
        # into X_train, X_val, y_train, y_val)
        self.X_train, self.X_val, self.y_train, self.y_val = train_test_split(
            self.X_trainval, self.y_trainval, train_size=0.80,
            test_size=0.20, random_state=42)

        # Return the results of the split
        return (self.X_train, self.y_train, self.X_val, self.y_val, self.X_test, self.y_test)
