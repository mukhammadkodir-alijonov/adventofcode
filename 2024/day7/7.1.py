def calculate(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
    return result

def generate_operators(n):
    if n == 0:
        return [[]]
    smaller = generate_operators(n - 1)
    return [op + ['+'] for op in smaller] + [op + ['*'] for op in smaller]

def can_form_target(target, numbers):
    operator_combinations = generate_operators(len(numbers) - 1)
    for operators in operator_combinations:
        if calculate(numbers, operators) == target:
            return True
    return False

def total_calibration_result(file_path):
    total = 0
    with open(file_path, "r") as file:
        lines = file.readlines()
        for line in lines:
            target, numbers = line.split(":")
            target = int(target.strip())
            numbers = list(map(int, numbers.strip().split()))
            if can_form_target(target, numbers):
                total += target
    return total

file_path = "input.txt"

result = total_calibration_result(file_path)
print(f"Total Calibration Result: {result}")