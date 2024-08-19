import pickle
from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train_and_save_model():
    # Load the Iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the SVM model
    svm = SVC(C=1.0, kernel='rbf', degree=3, gamma='scale', coef0=0.0, shrinking=True, probability=False, tol=0.001, cache_size=200, class_weight=None, verbose=False, max_iter=-1, decision_function_shape='ovr', random_state=42)
    svm.fit(X_train, y_train)

    # Make predictions and calculate accuracy
    predictions = svm.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    # Save the trained model with a timestamped filename
    model_filename = 'iris_model.pkl'
    with open(model_filename, 'wb') as f:
        pickle.dump(svm, f)

    print(f'Model trained successfully with accuracy: {accuracy}')
    print(f'Model saved as: {model_filename}')

if __name__ == "__main__":
    train_and_save_model()
