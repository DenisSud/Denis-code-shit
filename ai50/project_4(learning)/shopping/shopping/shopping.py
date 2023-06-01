import csv
from pickle import TRUE
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    data = open(filename)
    file = tuple()
    evidence = []
    columns = ['Administrative', 'Administrative_Duration', 'Informational', 
               'Informational_Duration', 'ProductRelated', 'ProductRelated_Duration', 
               'BounceRates', 'ExitRates', 'PageValues', 'SpecialDay', 'Month', 
               'OperatingSystems', 'Browser', 'Region', 'TrafficType', 'VisitorType', 'Weekend'
               ]
    for i in columns:
        column = [row[i] for row in data]
        evidence.append(column)
    labels = []
    for i in [row["Revenue"] for row in data]:
        if i == 'TRUE':
            labels.append(1)
        else:
            labels.append(0)
    file.add(evidence)
    file.add(labels)
    print(file)
        
    
    

def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    X_train, X_test = [evidence, labels]
    model = KNeighborsClassifier
    model.fit(X_train, X_test)
    return(model)


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    #done but not tested
    rev_true = 0
    rev_false = 0
    rev_true_guess = 0
    rev_false_guess = 0
    for x in labels:
        if x == 1:
            rev_true += 1
        else:
            rev_false += 1
    for index in len(labels):
        if predictions[index] == labels[index] and labels[index] == 1:
            rev_true_guess += 1
        elif predictions[index] == labels[index] and labels[index] == 0:
            rev_false_guess += 1
        sensitivity = rev_true/rev_true_guess
        specificity = rev_false/rev_false_guess
        return(sensitivity, specificity)

if __name__ == "__main__":
    main()
print(load_data("shopping.csv"))