import pytest
from ml.model import train_model, compute_model_metrics #needed for first and second test
from sklearn.ensemble import RandomForestClassifier #needed for first test
import pandas as pd  # needed for third test

def test_for_rfc():
    """
    testing that we are using a RandomForestClassifier algorithm
    """
    #creating two lists of lists to simulate X and y inputs
    x = [[1, 2, 3], [1, 2, 3]]
    y = [[1, 2, 3], [1, 2, 3]]

#running the model training function on our lists
    model = train_model(x, y)
#and the actual test, making sure we return a RandomForestClassifier model
    assert isinstance(model, RandomForestClassifier)," Not a RandomForestClassifier model"


def test_compute_model_metrics():
    """
    Test that the compute_model_metrics function returns floatvalues within a reasonable range.
    """
    # creating two lists as sample data
    y_true = [1, 1, 1, 1, 0, 1, 0, 0]
    y_pred = [1, 0, 1, 0, 0, 0, 1, 0]

    # Calculate metrics. Default average is 'binary', which we don't want here. Seeing if "weighted" works better for multi-class
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)

    # 
    # checking for floats 
    assert isinstance(precision, float), "Precision is not a float"
    assert isinstance(recall, float), "Recall is not a float"
    assert isinstance(fbeta, float), "Fbeta is not a float"
    # checking range
    assert 0 <= precision <= 1, "Precision is out of range"
    assert 0 <= recall <= 1, "Recall is out of range"
    assert 0 <= fbeta <= 1, "Fbeta is out of range"


# TODO: implement the third test. Change the function name and input as needed
def test_column_names():
    """
    # This test will ensure the column names are as expected in the source data.
    """
    # what I think the column names should be
    expected_columns = [
        'age',
        'workclass',
        'fnlgt',
        'education',
        'education-num',
        'marital-status',
        'occupation',
        'relationship',
        'race',
        'sex',
        'capital-gain',
        'capital-loss',
        'hours-per-week',
        'native-country',
        'salary'
    ]
    # loading the data so we can see what they actually are
    path = "data/census.csv"
    data = pd.read_csv(path)

    # comparing the two lists. https://stackoverflow.com/questions/62267584/comparing-two-lists-using-zip-function-in-python
    # got me started
    for index, (first, second) in enumerate(zip(data.columns, expected_columns)):
        assert first == second, f"Column name mismatch at index {index}: expected '{second}', got '{first}'"

    
