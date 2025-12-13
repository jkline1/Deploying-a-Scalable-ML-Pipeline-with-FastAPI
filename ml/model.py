from os import path
import pickle
from sklearn.metrics import fbeta_score, precision_score, recall_score
from ml.data import process_data
#adding this since I'm using a RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
#this is used in performance_on_categorical_slice
import numpy as np 
import pandas as pd

# TODO: add necessary import

# Optional: implement hyperparameter tuning.
def train_model(X_train, y_train):
    """
    Trains a machine learning model and returns it.

    Inputs
    ------
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.
    Returns
    -------
    model
        Trained machine learning model.
    """
    # TODO: implement the function
    # Let's try a RandomForestClassifier! They're good for classification tasks.
    #initializing the model

    rfc_model = RandomForestClassifier()

    #fitting the model to training and labels as described above

    rfc_model.fit(X_train, y_train)
    return rfc_model


def compute_model_metrics(y, preds):
    #If I understand the assignment correctly, I can just leave this alone
    """
    Validates the trained machine learning model using precision, recall, and F1.

    Inputs
    ------
    y : np.array
        Known labels, binarized.
    preds : np.array
        Predicted labels, binarized.
    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """
    fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
    precision = precision_score(y, preds, zero_division=1)
    recall = recall_score(y, preds, zero_division=1)
    return precision, recall, fbeta


def inference(model, X):
    """ Run model inferences and return the predictions.

    Inputs
    ------
    model : ???
        Trained machine learning model.
    X : np.array
        Data used for prediction.
    Returns
    -------
    preds : np.array
        Predictions from the model.
    """
    # The below should be how you return predictions from our model, X being our new input data.
    preds = model.predict(X)
    return preds

def save_model(model, path):
    """ Serializes model to a file.

    Inputs
    ------
    model
        Trained machine learning model or OneHotEncoder.
    path : str
        Path to save pickle file.
    """
    # TODO: figure out how to generate "path"
    with open(path, 'wb') as file:
        pickle.dump(model, file)

def load_model(path):
    """ Loads pickle file from `path` and returns it."""
    # TODO: implement the function
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model



def performance_on_categorical_slice(
    data, column_name, slice_value, categorical_features, label, encoder, lb, model
):
    """ Computes the model metrics on a slice of the data specified by a column name and

    Processes the data using one hot encoding for the categorical features and a
    label binarizer for the labels. This can be used in either training or
    inference/validation.

    Inputs
    ------
    data : pd.DataFrame
        Dataframe containing the features and label. Columns in `categorical_features`
    column_name : str
        Column containing the sliced feature.
    slice_value : str, int, float
        Value of the slice feature.
    categorical_features: list
        List containing the names of the categorical features (default=[])
    label : str
        Name of the label column in `X`. If None, then an empty array will be returned
        for y (default=None)
    encoder : sklearn.preprocessing._encoders.OneHotEncoder
        Trained sklearn OneHotEncoder, only used if training=False.
    lb : sklearn.preprocessing._label.LabelBinarizer
        Trained sklearn LabelBinarizer, only used if training=False.
    model : ???
        Model used for the task.

    Returns
    -------
    precision : float
    recall : float
    fbeta : float

    """
    """
    Calculates precision, recall, and fbeta score for a specific data slice.

    Parameters
    ----------
    data : pandas.DataFrame
        The dataset to evaluate.
    column_name : str
        The name of the categorical column to slice on.
    slice_value : str
        The specific value within the column to filter by.
    categorical_features : list
        A list of all categorical feature names in the data.
    label : str
        The name of the target/label column.
    encoder : dict
        A dictionary where keys are column names and values are fitted LabelEncoders.
    lb : sklearn.preprocessing.LabelBinarizer
        The fitted LabelBinarizer for the target variable.
    model : fitted sklearn model
        The trained machine learning model.

    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """

    # Filter the data to create the slice
    slice_data = data[data[column_name] == slice_value]

    # 2. Prepare the data for prediction
    X_slice = slice_data[categorical_features].copy()
    y_true_labels = slice_data[label]

    # Apply the pre-fitted encoders to the slice features
    for feature in categorical_features:
        # Handle potential unseen values if necessary
        try:
            X_slice[feature] = encoder[feature].transform(X_slice[feature])
        except ValueError:
            X_slice[feature] = X_slice[feature].astype('category').cat.codes.fillna(-1).astype(int)

    # Convert to numpy array 
    X_slice_np = np.array(X_slice.values)

    # 3. Make predictions
    y_pred_labels = model.predict(X_slice_np)

    # 4. Transform true labels to match model output format (assuming model predicts binarized/encoded labels)

    y_true = lb.transform(y_true_labels)
    y_pred = lb.transform(pd.Series(y_pred_labels))

    # In binary classification, lb.transform returns a 2D array, so we flatten it
    if y_true.shape[1] == 1:
        y_true = y_true.flatten()
        y_pred = y_pred.flatten()


    # 5. Calculate metrics (using beta=1 for default fbeta, i.e., f1 score)
    # make sure I don't need to fix this
    precision = precision_score(y_true, y_pred, average='binary', pos_label=1, zero_division=0)
    recall = recall_score(y_true, y_pred, average='binary', pos_label=1, zero_division=0)
    fbeta = fbeta_score(y_true, y_pred, beta=1, average='binary', pos_label=1, zero_division=0) # Using beta=1 for F1 score

    return precision, recall, fbeta

    X_slice, y_slice, _, _ = process_data(
        # your code here
        # for input data, use data in column given as "column_name", with the slice_value 
        # use training = False
    )
    preds = None # your code here to get prediction on X_slice using the inference function
    precision, recall, fbeta = compute_model_metrics(y_slice, preds)
    return precision, recall, fbeta
