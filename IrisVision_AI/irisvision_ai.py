# =====================================================
# IRISVISION AI
# Professional Iris Flower Classification System
# Developed by: Cheran
# Internship Project - DecodeLabs
# =====================================================

# ================= IMPORT LIBRARIES =================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from colorama import Fore, Style, init

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)

# Initialize colorama
init(autoreset=True)

# ================= HEADER =================

print(Fore.CYAN + "=" * 60)
print(Fore.GREEN + "        IRISVISION AI CLASSIFICATION SYSTEM")
print(Fore.CYAN + "=" * 60)

print(Fore.YELLOW + "Developer : Cheran")
print(Fore.YELLOW + "Organization : DecodeLabs")
print(Fore.YELLOW + "Domain : Artificial Intelligence & ML")

print(Fore.CYAN + "=" * 60 + "\n")

# ================= LOAD DATASET =================

print(Fore.BLUE + "[1] Loading Iris Dataset...\n")

iris = load_iris()

X = iris.data
y = iris.target

feature_names = iris.feature_names
target_names = iris.target_names

print(Fore.GREEN + "Dataset Loaded Successfully!\n")

print(Fore.WHITE + f"Total Samples : {len(X)}")
print(Fore.WHITE + f"Features : {feature_names}")
print(Fore.WHITE + f"Classes : {target_names}\n")

# ================= TRAIN TEST SPLIT =================

print(Fore.BLUE + "[2] Splitting Dataset...\n")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print(Fore.GREEN + "Data Split Completed!\n")

print(Fore.WHITE + f"Training Samples : {len(X_train)}")
print(Fore.WHITE + f"Testing Samples : {len(X_test)}\n")

# ================= FEATURE SCALING =================

print(Fore.BLUE + "[3] Applying Feature Scaling...\n")

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

print(Fore.GREEN + "Feature Scaling Applied!\n")

# ================= MODEL TRAINING =================

print(Fore.BLUE + "[4] Training KNN Model...\n")

model = KNeighborsClassifier(n_neighbors=5)

model.fit(X_train, y_train)

print(Fore.GREEN + "Model Training Successful!\n")

# ================= PREDICTIONS =================

print(Fore.BLUE + "[5] Predicting Test Data...\n")

predictions = model.predict(X_test)

print(Fore.GREEN + "Prediction Completed!\n")

# ================= ACCURACY =================

accuracy = accuracy_score(y_test, predictions)

print(Fore.CYAN + "=" * 60)
print(Fore.GREEN + "MODEL PERFORMANCE")
print(Fore.CYAN + "=" * 60)

print(Fore.YELLOW + f"\nAccuracy : {accuracy * 100:.2f}%\n")

# ================= CLASSIFICATION REPORT =================

print(Fore.MAGENTA + "Classification Report:\n")

print(classification_report(y_test, predictions))

# ================= CONFUSION MATRIX =================

print(Fore.MAGENTA + "Confusion Matrix:\n")

cm = confusion_matrix(y_test, predictions)

print(cm)

# ================= VISUALIZATION =================

print(Fore.BLUE + "\n[6] Generating Visualization...\n")

plt.figure(figsize=(6, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=target_names,
    yticklabels=target_names
)

plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.show()

# ================= CUSTOM PREDICTION =================

print(Fore.CYAN + "\n" + "=" * 60)
print(Fore.GREEN + "CUSTOM FLOWER PREDICTION")
print(Fore.CYAN + "=" * 60)

try:

    sepal_length = float(input("\nEnter Sepal Length : "))
    sepal_width = float(input("Enter Sepal Width : "))
    petal_length = float(input("Enter Petal Length : "))
    petal_width = float(input("Enter Petal Width : "))

    custom_data = [[
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]]

    custom_data = scaler.transform(custom_data)

    prediction = model.predict(custom_data)

    flower = target_names[prediction[0]]

    print(Fore.GREEN + f"\nPredicted Flower : {flower}")

except:

    print(Fore.RED + "\nInvalid Input! Please enter numeric values only.")

# ================= END =================

print(Fore.CYAN + "\n" + "=" * 60)
print(Fore.GREEN + "Thank You for Using IrisVision AI")
print(Fore.CYAN + "=" * 60)