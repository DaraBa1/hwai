import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
iris = load_iris()
X, y = iris.data, iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"--- Загальна точність (Accuracy) ---")
print(f"Accuracy: {accuracy:.4f}\n")
cm = confusion_matrix(y_test, y_pred)
print("Матриця плутанини (Confusion Matrix):")
print(cm)
print("-" * 40)
n_classes = len(iris.target_names)

for i in range(n_classes):
    class_name = iris.target_names[i]
    tp = cm[i, i]
    fp = cm[:, i].sum() - tp
    fn = cm[i, :].sum() - tp
    tn = cm.sum() - (tp + fp + fn)
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

    print(f"Клас: {class_name} (ID: {i})")
    print(f"  TP (True Positive):  {tp}")
    print(f"  FP (False Positive): {fp}")
    print(f"  TN (True Negative):  {tn}")
    print(f"  FN (False Negative): {fn}")
    print(f"  Precision:           {precision:.4f}")
    print(f"  Recall:              {recall:.4f}")
    print(f"  F1-Score:            {f1:.4f}")
    print("-" * 40)