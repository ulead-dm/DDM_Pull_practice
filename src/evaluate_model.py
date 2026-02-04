# Model testing script
# evaluate_model.py
# Symbolic evaluation script

def accuracy(y_true, y_pred):
    correct = sum(1 for yt, yp in zip(y_true, y_pred) if yt == yp)
    return correct / len(y_true)


if __name__ == "__main__":
    y_true = [0, 1, 1, 0]
    y_pred = [0, 1, 0, 0]

    acc = accuracy(y_true, y_pred)
    print(f"Accuracy: {acc}")

def print_report(metric_value):
    print(f"Evaluation result: {metric_value}")
