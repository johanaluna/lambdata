import pandas
import numpy
from sklearn.model_selection import train_test_split


def reportnulls(b):
    null_counts = b.isnull().sum().sort_values(ascending=False)
    print(null_counts.reset_index())
    return null_counts

def splitdata(a,target):
    print('shape of your data frame: ',a.shape)

    X = a.drop(columns=target)
    y = a[target]
    X_trainval, X_test, y_trainval, y_test = train_test_split(
    X, y, train_size=0.80, test_size=0.20, random_state=42)

    X_train, X_val, y_train, y_val = train_test_split(
    X_trainval, y_trainval, train_size=0.80, test_size=0.20,
    random_state=42)

    print('X_train shape', X_train.shape)
    print('y_train shape', y_train.shape)
    print('X_val shape', X_val.shape)
    print('y_val shape', y_val.shape)
    print('X_test shape', X_test.shape)
    print('y_test shape', y_test.shape)
    return (X_train, y_train, X_val, y_val, X_test, y_test)
