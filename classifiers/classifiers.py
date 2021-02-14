from sklearn import svm, linear_model as lm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import numpy as np
from data_loader import load_data, over_sample_SMOTE, over_sample_ADASYN
from sklearn.model_selection import RandomizedSearchCV


def classify(over_sampling_method: str, smell_type: str) -> None:
    X_train, Y_train, X_test, Y_test = load_data(smell_type)

    if over_sampling_method == 'SMOTE':
        X_train, Y_train = over_sample_SMOTE(X_train, Y_train)
    elif over_sampling_method == 'ADASYN':
        X_train, Y_train = over_sample_ADASYN(X_train, Y_train)


    svm_clf = svm.SVC(C=100)
    svm_clf.set_params(kernel='linear').fit(X_train, Y_train)

    Y_pred = svm_clf.predict(X_test)
    print("RESULT ZA LINEAR SVM : \n" ,classification_report(Y_test, Y_pred))

    svm_clf.set_params(kernel='rbf').fit(X_train, Y_train)
    Y_pred = svm_clf.predict(X_test)
    print("RESULT ZA RBF SVM : \n", classification_report(Y_test, Y_pred))

    rf_clf = RandomForestClassifier(n_estimators=100)
    rf_clf.fit(X_train, Y_train)
    Y_pred = rf_clf.predict(X_test)
    print("RESULT ZA RANDOM FOREST : \n", classification_report(Y_test, Y_pred))

    lr = lm.LogisticRegression(max_iter=2000).fit(X_train, Y_train)
    Y_pred = lr.predict(X_test)
    print("RESULT ZA LOGISTIC REGRESSION : \n", classification_report(Y_test, Y_pred))


def param_search_rf(over_sampling_method: str, smell_type: str) -> None:
    X_train, Y_train, X_test, Y_test = load_data(smell_type)

    if over_sampling_method == 'SMOTE':
        X_train, Y_train = over_sample_SMOTE(X_train, Y_train)
    elif over_sampling_method == 'ADASYN':
        X_train, Y_train = over_sample_ADASYN(X_train, Y_train)

    n_estimators = [int(x) for x in np.linspace(start=200, stop=2000, num=10)]
    max_features = ['auto', 'sqrt']
    max_depth = [int(x) for x in np.linspace(10, 110, num=11)]
    max_depth.append(None)
    min_samples_split = [2, 5, 10]
    min_samples_leaf = [1, 2, 4]
    bootstrap = [True, False]

    random_grid = {'n_estimators': n_estimators,
                   'max_features': max_features,
                   'max_depth': max_depth,
                   'min_samples_split': min_samples_split,
                   'min_samples_leaf': min_samples_leaf,
                   'bootstrap': bootstrap}

    rf = RandomForestClassifier()

    rf_random = RandomizedSearchCV(estimator=rf, param_distributions=random_grid, n_iter=100, cv=3, verbose=2,
                                   random_state=42, n_jobs=-1)
    rf_random.fit(X_train, Y_train)

    print(rf_random.best_params_)


    rf_clf = RandomForestClassifier(n_estimators=100)
    rf_clf.fit(X_train, Y_train)
    Y_pred = rf_clf.predict(X_test)
    print("RESULT ZA RANDOM FOREST : \n", classification_report(Y_test, Y_pred))

if __name__ == '__main__':
    classify('SMOTE', 'LONG_METHOD')
    # classify('SMOTE', 'GOD_CLASS')


    #param_search_rf('SMOTE', 'LONG_METHOD')



