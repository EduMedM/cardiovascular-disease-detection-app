import os
import pickle
import joblib
import sklearn

config = {
    'classifier': {
        'SVC': 'ml_models/svc_model.pkl',
        'LogisticRegression': 'ml_models/Logistic_regression_model.pkl',
        'NaiveBayes': 'ml_models/naive_bayes_model.pkl',
        'DecisionTree':'ml_models/decision_tree_model.pkl',
        'scaler_file': 'ml_models/standard_scaler_ts015_rs0.pkl',
        'deep_learning': 'ml_models/deep_learning_model.pkl',
        'KNN': 'ml_models/KNN_model.pkl',
    }}

dir = os.path.dirname(__file__)

def get_joblib_file(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return joblib.load(os.path.join(dir, filepath))
    return None

def get_pickle_file(filepath):
    if os.path.isfile(os.path.join(dir, filepath)):
        return joblib.load(os.path.join(dir, filepath))
    return None

def get_standard_scaler():
    return get_pickle_file(config['classifier']['scaler_file'])

def get_all_classifiers():
    return (get_svc_classifier(), 
            get_logistic_regression_classifier(), 
            get_naive_bayes_classifier(), 
            get_decision_tree_classifier(), 
            get_deep_learning_classifier(), 
            get_knn_classifier())

def get_svc_classifier():
    return get_joblib_file(config['classifier']['SVC'])

def get_logistic_regression_classifier():
    return get_joblib_file(config['classifier']['LogisticRegression'])

def get_naive_bayes_classifier():
    return get_joblib_file(config['classifier']['NaiveBayes'])

def get_decision_tree_classifier():
    return get_joblib_file(config['classifier']['DecisionTree'])

def get_deep_learning_classifier():
    return get_joblib_file(config['classifier']['deep_learning'])

def get_knn_classifier():
    return get_joblib_file(config['classifier']['KNN'])



