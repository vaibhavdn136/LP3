def fibonacci_iterative_with_steps(n):
    if n <= 1:
        return n

    a, b, c = 0, 1, 0
    steps = 0

    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
        steps += 1

    return c, steps

# Specify the Fibonacci number you want to calculate
n = 10

# Calculate the Fibonacci number and count the steps
result, step_count = fibonacci_iterative_with_steps(n)

print(f"Fibonacci({n}) = {result}")
print(f"Total Steps (Iterative): {step_count}")










def fibonacci_recursive(n):
    # Base case
    if n <= 1:
        return n

    # Recursive call
    global recursion_steps
    recursion_steps += 1
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Initialize the step count
recursion_steps = 0

# Specify the Fibonacci number you want to calculate
n = 10

# Calculate the Fibonacci number
result = fibonacci_recursive(n)

print(f"Fibonacci({n}) = {result}")
print(f"Total Steps (Recursive): {recursion_steps}")











if __name__=="__main__":
    n=10
    for i in range(n):
        print(fibonacci_recursive(i))
    
 

