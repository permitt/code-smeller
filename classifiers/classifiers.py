from sklearn import svm, linear_model as lm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

from data_loader import load_data, over_sample_SMOTE, over_sample_ADASYN


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


if __name__ == '__main__':
    #classify('SMOTE', 'LONG_METHOD')

    classify('SMOTE', 'GOD_CLASS')
