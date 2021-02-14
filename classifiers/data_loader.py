from imblearn.over_sampling import SMOTE, ADASYN
import pandas as pd
import pickle
import numpy as np
from sklearn import svm
from sklearn.metrics import classification_report

DATASET_PREFIX_PATH = "../data/INPUT/"
LONG_METHOD_SPLITTED_CSV = "../data/MLCQ_long_method_data_splitted.csv"
GOD_CLASS_SPLITTED_CSV = "../data/MLCQ_god_class_data_splitted.csv"


# method for loading data distribution from CSV
# and reading vectors from pickled objects
def load_data_long_method() -> ([], []):
    ds_distribution = pd.read_csv(LONG_METHOD_SPLITTED_CSV)
    ds_distribution['parts']

    cls = {'none': 0, 'major': 0, 'critical': 0, 'minor': 0}
    X, Y = {'train': [], 'test': []}, {'train': [], 'test': []}

    for index, file in enumerate(ds_distribution['files']):
        label = file.split('/')[0]
        try:
            pickling_open = open(DATASET_PREFIX_PATH + file[:-3] + "pickle", "rb")
            obj = pickle.load(pickling_open)
            if (np.isnan(obj.vector[0][0])):
                cls[label] += 1
                continue
            else:
                X[ds_distribution['parts'][index]].append(obj.vector[0])
                label = 'none' if label == 'none' else 'code_smell'
                Y[ds_distribution['parts'][index]].append(label)
        except Exception as error:
            print("Ne postoji fajl :( ", error)

    print("NE PARSIRANIH METODA: ", cls)
    return np.array(X['train']), np.array(Y['train']), np.array(X['test']), np.array(Y['test'])


def load_data_god_class() -> ([], []):
    return


def over_sample_SMOTE(X: [], Y: []) -> ([], []):
    sampler = SMOTE(random_state=42)
    return sampler.fit_resample(X, Y)


def over_sample_ADASYN(X: [], Y: []) -> ([], []):
    sampler = ADASYN()
    return sampler.fit_resample(X, Y)


if __name__ == '__main__':
    X_train, Y_train, X_test, Y_test = load_data_long_method()

    X_train, Y_train = over_sample_SMOTE(X_train, Y_train)

    svm_clf = svm.SVC(C=100)
    svm_clf.set_params(kernel='linear').fit(X_train, Y_train)

    Y_pred = svm_clf.predict(X_test)
    print(classification_report(Y_test, Y_pred))

