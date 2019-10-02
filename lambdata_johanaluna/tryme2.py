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
        null_counts = self.df.isnull().sum().sort_values(ascending=False)

        # return count of null values
        return null_counts

    """
    function to split the data into train, validation and test
    this function split the data in 80% 20%
    that means that the target corresponds to 20%
    of the complete data frame
    """


    def splitdata(self):

        print('shape of your data frame: ', self.df.shape)
        # Define X and y
        X = self.df.drop(columns=self.name_column_target)
        y = self.df[self.name_column_target]

        # we need to do 2 splits
        # 1.(Takes X and y into X_trainval, X_test, y_trainval, y_test)
        X_trainval, X_test, y_trainval, y_test = train_test_split(
            X, y, train_size=0.80, test_size=0.20, random_state=42)

        # 2.(Takes X_trainval, y_trainval and split data
        # into X_train, X_val, y_train, y_val)
        X_train, X_val, y_train, y_val = train_test_split(
            X_trainval, y_trainval, train_size=0.80,
            test_size=0.20, random_state=42)

        # Print the size the results
        print('X_train shape', X_train.shape)
        print('y_train shape', y_train.shape)
        print('X_val shape', X_val.shape)
        print('y_val shape', y_val.shape)
        print('X_test shape', X_test.shape)
        print('y_test shape', y_test.shape, '\n\n')

        # Return the results of the split
        return (X_train, y_train, X_val, y_val, X_test, y_test)
