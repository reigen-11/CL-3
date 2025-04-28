import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import classification_report

# Data generation
X, y = make_classification(n_samples=100, n_features=10,
                            n_redundant=2, n_classes=2)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train = StandardScaler().fit_transform(X_train)
X_test = StandardScaler().fit(X_train).transform(X_test)

# AIRS-like training
def airs_train(X, y, detectors=20):
    idx = np.random.choice(len(X), detectors, replace=False)
    model = SVC(kernel='rbf', probability=True)
    model.fit(X[idx], y[idx])
    return model

svm = airs_train(X_train, y_train, detectors=30)

# Evaluation
y_pred = svm.predict(X_test)
print("Classification Report:\n", classification_report(y_test, y_pred))
print(f"Accuracy: {np.mean(y_pred == y_test) * 100:.2f}%")

# Plotting
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='coolwarm', edgecolor='k')
plt.title("Structural Damage Classification")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.grid(True)
plt.show()