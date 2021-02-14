from imblearn.over_sampling import SMOTE, ADASYN
import pandas as pd
import pickle
import numpy as np


DATASET_LM_PREFIX_PATH = "../data/long_method/"
DATASET_GC_PREFIX_PATH = "../data/god_class/"
LONG_METHOD_SPLITTED_CSV = "../data/MLCQ_long_method_data_splitted.csv"
GOD_CLASS_SPLITTED_CSV = "../data/MLCQ_god_class_data_splitted.csv"


# method for loading data distribution from CSV
# and reading vectors from pickled objects
# returning X, Y for training and testing
def load_data(smell_type: str) -> ([], []):
    if smell_type == "LONG_METHOD":
        ds_distribution = pd.read_csv(LONG_METHOD_SPLITTED_CSV)
        ds_prefix = DATASET_LM_PREFIX_PATH
    else:
        ds_distribution = pd.read_csv(GOD_CLASS_SPLITTED_CSV)
        ds_prefix = DATASET_GC_PREFIX_PATH

    ds_distribution['parts']
    X, Y = {'train': [], 'test': []}, {'train': [], 'test': []}

    for index, file in enumerate(ds_distribution['files']):
        try:
            pickling_open = open(ds_prefix + file[:-3] + "pickle", "rb")
            obj = pickle.load(pickling_open)
            if not np.isnan(obj.vector[0][0]):
                X[ds_distribution['parts'][index]].append(obj.vector[0])
                label = 'none' if obj.label == 'none' else 'code_smell'
                Y[ds_distribution['parts'][index]].append(label)

        except Exception as error:
            print("Ne postoji fajl :( ", error)

    return np.array(X['train']), np.array(Y['train']), np.array(X['test']), np.array(Y['test'])



def over_sample_SMOTE(X: [], Y: []) -> ([], []):
    sampler = SMOTE(random_state=42)
    return sampler.fit_resample(X, Y)


def over_sample_ADASYN(X: [], Y: []) -> ([], []):
    sampler = ADASYN()
    return sampler.fit_resample(X, Y)

