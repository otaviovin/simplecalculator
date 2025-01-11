from tkinter import *  # Import the tkinter library for GUI development

# Initialize the expression as an empty string
expression = ""

# Function to update the expression when a button is pressed
def press(num):
    global expression
    # Append the pressed button's value to the current expression
    expression = expression + str(num)  # Concatenate the number to the expression
    equation.set(expression)  # Update the displayed equation on the GUI

# Function to evaluate the final expression and display the result
def equalpress():
    try:
        global expression
        # Evaluate the mathematical expression using eval() and convert the result to a string
        total = str(eval(expression))
        equation.set(total)  # Display the result in the GUI
        expression = ""  # Reset the expression for further use
    except:
        # If an error occurs during evaluation, display an error message
        equation.set('error generated')
        expression = ""  # Reset the expression

# Function to clear the current input and reset the expression
def clear():
    global expression
    expression = ""  # Reset the expression to an empty string
    equation.set("")  # Clear the displayed equation on the GUI

# Main function to set up the GUI
if __name__ == "__main__":
    # Create the main application window
    root = Tk()
    root.configure(background="grey")  # Set the background color of the window
    root.title("Calculator Application")  # Set the title of the application window
    root.geometry("270x150")  # Define the size of the window

    # Variable to store and display the current equation
    equation = StringVar()

    # Create an input field to display the current equation
    expression_field = Entry(root, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)  # Span the input field across 4 columns

    # Set the initial text in the input field
    equation.set("Enter your expression")

    # Create buttons for numbers 0-9 and mathematical operators
    button1 = Button(root, text=' 1 ', fg='white', bg='black',
                     command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(root, text=' 2 ', fg='white', bg='black',
                     command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(root, text=' 3 ', fg='white', bg='black',
                     command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(root, text=' 4 ', fg='white', bg='black',
                     command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(root, text=' 5 ', fg='white', bg='black',
                     command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(root, text=' 6 ', fg='white', bg='black',
                     command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(root, text=' 7 ', fg='white', bg='black',
                     command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(root, text=' 8 ', fg='white', bg='black',
                     command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(root, text=' 9 ', fg='white', bg='black',
                     command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(root, text=' 0 ', fg='white', bg='black',
                     command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    # Create buttons for operators and functionalities
    plus = Button(root, text=' + ', fg='white', bg='black',
                  command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(root, text=' - ', fg='white', bg='black',
                   command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(root, text=' * ', fg='white', bg='black',
                      command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(root, text=' / ', fg='white', bg='black',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    # Button to calculate and display the result
    equal = Button(root, text=' = ', fg='white', bg='black',
                   command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    # Button to clear the current equation
    clear_button = Button(root, text=' Clear ', fg='white', bg='black',
                          command=clear, height=1, width=7)
    clear_button.grid(row=5, column=1)

    # Button for the decimal point
    decimal = Button(root, text=".", fg='white', bg='black',
                     command=lambda: press('.'), height=1, width=7)
    decimal.grid(row=6, column=0)

    # Start the main event loop of the application
    root.mainloop()
