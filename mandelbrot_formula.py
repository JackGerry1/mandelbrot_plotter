import re

def parse_complex_number(input_string):
    # Regular expression pattern to match the complex number format
    pattern = r'([+-]?\d+(?:\.\d+)?)i?'

    # Matching the input string against the pattern
    match = re.match(pattern, input_string)

    if match:
        real_part = 0
        imaginary_part = 0
        number = match.group(1)

        if number:
            if number == '-':
                imaginary_part = -1
            elif number == '+':
                imaginary_part = 1
            else:
                imaginary_part = float(number)

        # Constructing the complex number using the real and imaginary parts
        return complex(real_part, imaginary_part)

    # Raising an exception if the input string does not match the expected format
    raise ValueError("Invalid complex number format")


def f(x, c):
    """
    Recursive function to calculate the result of f(x) = x**2 + c for a given complex number c. 

    Arguments:
        x: The current iteration.
        c: The complex number.

    Returns:
        The result of f(x).
    """
    if x == 0:
        # Base case: When x is 0, the result is the input complex number c itself.
        return c
    else:
        # Recursive case: Calculate f(x-1) recursively and apply the function equation.
        return f(x - 1, c) ** 2 + c


def get_user_choice():
    """
    Prompt the user for a choice to enter a complex number or not.

    Returns:
        The user's choice as a lowercase string ('y' for yes, 'n' for no).
    """
    while True:
        enter_complex = input("Do you want to enter a complex number? (y/n): ")
        if enter_complex.lower() in ['y', 'n']:
            # Valid input: Return the user's choice in lowercase.
            return enter_complex.lower()
        else:
            # Invalid input: Prompt the user again.
            print("Invalid input. Please enter 'y' or 'n'.")

def get_complex_number():
    """
    Prompt the user to enter a complex number.

    Returns:
        The complex number as a sum of the real and imaginary parts.
    """
    valid_input = False

    while not valid_input:
        try:
            real_part = float(input("Enter the real part of C: "))
            valid_input = True
        except ValueError:
            # Invalid input for real part: Prompt for a valid real number.
            print("Invalid input. Please enter a valid real number.")

    valid_input = False

    while not valid_input:
        complex_input = input("Enter the imaginary part of C (e.g., 1i, -1i, 0.38i): ")
        try:
            imaginary_part = parse_complex_number(complex_input)
            valid_input = True
        except ValueError as e:
            # Invalid input for imaginary part: Print the error message and prompt again.
            print(e)

    return real_part + imaginary_part


def get_iteration_count():
    """
    Prompt the user to enter the number of iterations for the function.

    Returns:
        The number of iterations.
    """
    valid_input = False

    while not valid_input:
        try:
            user_iteration = int(input("Enter the number of iterations for the function (up to 100): "))
            if 1 <= user_iteration <= 100:
                valid_input = True
            else:
                # Invalid input: Number is not within the valid range.
                print("Invalid input. Please enter a number between 1 and 100.")
        except ValueError:
            # Invalid input: Not a valid number.
            print("Invalid input. Please enter a valid number.")

    return user_iteration


def process_complex_number():
    """
    Process the complex number chosen by the user and perform iterations of the Mandelbrot function.

    Prints the results and determines if the complex number is in the Mandelbrot set.
    """
    c = get_complex_number()
    user_iteration = get_iteration_count()

    for n in range(user_iteration):
        # Calculate the result of the Mandelbrot function for each iteration
        result = round(f(n, c).real, 3) + round(f(n, c).imag, 3) * 1j
        real_part = round(result.real, 3)
        imag_part = round(result.imag, 3)
        result = f"{real_part} + {imag_part}i"
        print(f"f({n + 1}) = {result}")

    # Calculate the final result for the last iteration
    final_result = f(user_iteration, c)
    original_complex = f"{round(c.real, 3)} + {round(c.imag, 3)}i"

    # Check if the final result is in the Mandelbrot set
    if abs(final_result) > 2:
        print(f"The values {original_complex} are NOT in the Mandelbrot set.")
    else:
        print(f"The values {original_complex} ARE in the Mandelbrot set.")


def process_real_number():
    """
    Process the real number chosen by the user and perform iterations of the Mandelbrot function.

    Prints the results and determines if the real number is in the Mandelbrot set.
    """
    real_number = float(input("Enter the real part of C: "))
    user_iteration = get_iteration_count()

    for n in range(user_iteration):
        # Calculate the result of the Mandelbrot function for each iteration
        result = round(f(n, real_number), 3)
        print(f"f({n + 1}) = {result:.3f}")

    # Calculate the final result for the last iteration
    final_result = f(user_iteration, real_number)

    # Check if the final result is in the Mandelbrot set
    if abs(final_result) > 2:
        print(f"The value {real_number} is NOT in the Mandelbrot set.")
    else:
        print(f"The value {real_number} is IN the Mandelbrot set.")



def main():
    """
    Main program loop to interact with the user and control the flow of the program.
    """
    while True:
        # Prompt the user to choose whether to enter a complex number
        enter_complex = get_user_choice()

        if enter_complex == 'y':
            # Process a complex number chosen by the user
            process_complex_number()
        else:
            # Process a real number chosen by the user
            process_real_number()

        while True:
            # Prompt the user to restart or exit the program
            restart = input("Do you want to restart the program? (y/n): ")
            if restart.lower() == 'y':
                break
            elif restart.lower() == 'n':
                print("Thanks for using this program! I hope it was helpful :)")
                exit()
            else:
                print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
    main()

