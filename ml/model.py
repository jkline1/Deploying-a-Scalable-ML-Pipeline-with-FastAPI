from os import path
import pickle
from sklearn.metrics import fbeta_score, precision_score, recall_score
from ml.data import process_data
#adding this since I'm using a RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier

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

    rand_forest = RandomForestClassifier()

    #fitting the model to training and labels as described above

    rand_forest.fit(X_train, y_train)
    return rand_forest


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
    #the wb parameter opens the file for writing in binary mode
    with open(path, 'wb') as file:
        pickle.dump(model, file)

def load_model(path):
    """ Loads pickle file from `path` and returns it."""
    #the rb parameter opens the file for reading in binary mode
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
    data_slice = data[data[column_name]==slice_value]
    X_slice, y_slice, _, _ = process_data(
        # your code here
        # for input data, use data in column given as "column_name", with the slice_value 
        # use training = False
        X = data_slice,
        categorical_features=categorical_features,
        label = label,
        training = False,
        encoder = encoder,
        lb = lb

    )
    preds = inference(model, X_slice)
    precision, recall, fbeta = compute_model_metrics(y_slice, preds)
    return precision, recall, fbeta
