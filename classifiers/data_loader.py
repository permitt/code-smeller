from imblearn.over_sampling import SMOTE, ADASYN
import pandas as pd

LONG_METHOD_SPLITTED_CSV = "../data/MLCQ_long_method_data_splitted.csv"
GOD_CLASS_SPLITTED_CSV = "../data/MLCQ_god_class_data_splitted.csv"

# method for loading data distribution from CSV
# and reading vectors from pickled objects
def load_data_long_method() -> ([], []):
    ds_distribution = pd.read_csv(LONG_METHOD_SPLITTED_CSV)
    print(ds_distribution['files'][0:10])
    ds_distribution['parts']

    return

def load_data_god_class() -> ([], []):
    return


def over_sample_SMOTE(X: [], Y: []) -> ([], []):
    sampler = SMOTE(random_state = 42)
    return sampler.fit_resample(X, Y)

def over_sample_ADASYN(X: [], Y:[]) -> ([], []):
    sampler = ADASYN()
    return sampler.fit_resample(X, Y)


if __name__ == '__main__':
    load_data_long_method()
