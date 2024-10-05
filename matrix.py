import numpy as np

def parse_matrix_input():
    rows = []
    print("Enter matrix rows one by one. Type 'end' to finish:")
    while True:
        row = input()
        if row.lower() == 'end':
            break
        rows.append([float(num) for num in row.split()])
    return np.array(rows)

def matrix_calculator():
    while True:
        print("\nMatrix Calculator - Supported operations: add, sub, mul, div, exit")
        operation = input("Enter operation: ").strip().lower()

        if operation == 'exit':
            break

        print("Enter the first matrix:")
        matrix1 = parse_matrix_input()

        print("Enter the second matrix:")
        matrix2 = parse_matrix_input()

        if operation == 'add':
            try:
                result = np.add(matrix1, matrix2)
                print("Result:\n", result)
            except ValueError as e:
                print("Error:", e)
        elif operation == 'sub':
            try:
                result = np.subtract(matrix1, matrix2)
                print("Result:\n", result)
            except ValueError as e:
                print("Error:", e)
        elif operation == 'mul':
            try:
                result = np.matmul(matrix1, matrix2)
                print("Result:\n", result)
            except ValueError as e:
                print("Error:", e)
        elif operation == 'div':
            try:
                result = np.divide(matrix1, matrix2)
                print("Result:\n", result)
            except ValueError as e:
                print("Error:", e)
        else:
            print("Invalid operation")

if __name__ == "__main__":
    matrix_calculator()