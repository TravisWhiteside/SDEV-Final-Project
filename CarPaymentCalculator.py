#Author:  Travis Whiteside
#Date written: 01/24/2024
#Assignment:   Gui Project
#Short Desc: This program will calculate the payment of a car you are looking to purchase. It will take into consideration the following variables: Price, Downpayment, Intrest rate, Length of loan, Trade in value, Amount you owe on the traded in car

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def calculate_payment():
    try:
        # Get input values
        price = float(price_entry.get())
        interest_rate_str = interest_rate_entry.get()
        if not interest_rate_str:
            raise ValueError("Interest rate is required")
        interest_rate = float(interest_rate_str) / 100  # Convert percentage to decimal
        if interest_rate <= 0:
            raise ValueError("Interest rate must be greater than zero")
        down_payment = float(down_payment_entry.get())
        trade_in_value = float(trade_in_value_entry.get())
        amount_owed_on_trade_in = float(amount_owed_on_trade_in_entry.get())
        loan_length_months = int(loan_length_entry.get())

        # Calculate the loan amount
        loan_amount = price - down_payment - (trade_in_value - amount_owed_on_trade_in)

        # Calculate the monthly payment
        monthly_interest_rate = interest_rate / 12
        monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -loan_length_months)

        # Calculate total interest paid
        total_interest_paid = monthly_payment * loan_length_months - loan_amount

        # Calculate total price of the car
        total_price = monthly_payment * loan_length_months

        # Create a new window for displaying output
        global output_window
        output_window = tk.Toplevel(root)
        output_window.title("Output")
        
        # Set the size of the output window to match the main window
        output_window.geometry("450x250")
        
        # Set the font for the output window
        custom_font_output = ("Georgia", 12, "bold")

        # Create a text widget to display the result in the output window
        result_text_output = tk.Text(output_window, height=5, width=50, font=custom_font_output)
        result_text_output.pack(padx=10, pady=10)
        result_text_output.insert(tk.END, f"Monthly Payment: ${monthly_payment:.2f}\n")
        result_text_output.insert(tk.END, f"Total Interest Paid: ${total_interest_paid:.2f}\n")
        result_text_output.insert(tk.END, f"Total Price of the Car: ${total_price:.2f}")
        result_text_output.config(state=tk.DISABLED)  # Make the text widget read-only

        # Load image for the reset button
        reset_image = Image.open("reset_button_image.png")  # Replace with the path to your image
        reset_photo = ImageTk.PhotoImage(reset_image)

        # Create a button to close the output window and reset/clear the main window
        reset_button_output = tk.Button(output_window, text="Reset", command=reset_inputs_and_close_output, image=reset_photo, compound=tk.LEFT, font=custom_font_output, width=200, height=40)
        reset_button_output.image = reset_photo  # Keep a reference to the image to prevent garbage collection
        reset_button_output.pack(side=tk.LEFT, padx=5, pady=5)

        # Load image for the exit button
        exit_image = Image.open("exit_button_image.png")  # Replace with the path to your image
        exit_photo = ImageTk.PhotoImage(exit_image)

        # Create a button to close both windows
        exit_button_output = tk.Button(output_window, text="Exit", command=close_windows, image=exit_photo, compound=tk.LEFT, font=custom_font_output, width=200, height=40)
        exit_button_output.image = exit_photo  # Keep a reference to the image to prevent garbage collection
        exit_button_output.pack(side=tk.LEFT, padx=5, pady=5)

    except ValueError as ve:
        if ve.args[0] == "Interest rate is required":
            messagebox.showerror("Error", "Interest rate is required")
        elif ve.args[0] == "Interest rate must be greater than zero":
            messagebox.showerror("Error", "Interest rate must be greater than zero")
        else:
            messagebox.showerror("Error", "Please enter valid numeric values.")




def reset_inputs_and_close_output():
    # Clear input fields in the main window
    price_entry.delete(0, tk.END)
    interest_rate_entry.delete(0, tk.END)
    down_payment_entry.delete(0, tk.END)
    trade_in_value_entry.delete(0, tk.END)
    amount_owed_on_trade_in_entry.delete(0, tk.END)
    loan_length_entry.delete(0, tk.END)

    # Destroy the output window
    output_window.destroy()

def close_windows():
    # Close both the main window and the output window
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Car Payment Calculator")

# Set the size of the window
root.geometry("500x300")

# Set the font for the main window
custom_font_main = ("Georgia", 12, "bold")

# Load the image for the calculate button
calculate_image = Image.open("Calc_Button_Image.png")  # Replace with the path to your image
calculate_photo = ImageTk.PhotoImage(calculate_image)

# Load the image for the exit button
exit_image = Image.open("Exit_Button_Image.png")  # Replace with the path to your image
exit_photo = ImageTk.PhotoImage(exit_image)

# Create input labels and entry widgets
price_label = tk.Label(root, text="Price of the car:", font=custom_font_main)
price_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
price_entry = tk.Entry(root, font=custom_font_main)
price_entry.grid(row=0, column=1, padx=5, pady=5)

interest_rate_label = tk.Label(root, text="Interest rate (%):", font=custom_font_main)
interest_rate_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
interest_rate_entry = tk.Entry(root, font=custom_font_main)
interest_rate_entry.grid(row=1, column=1, padx=5, pady=5)

down_payment_label = tk.Label(root, text="Down payment:", font=custom_font_main)
down_payment_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
down_payment_entry = tk.Entry(root, font=custom_font_main)
down_payment_entry.grid(row=2, column=1, padx=5, pady=5)

trade_in_value_label = tk.Label(root, text="Trade-in value:", font=custom_font_main)
trade_in_value_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
trade_in_value_entry = tk.Entry(root, font=custom_font_main)
trade_in_value_entry.grid(row=3, column=1, padx=5, pady=5)

amount_owed_on_trade_in_label = tk.Label(root, text="Amount owed on trade-in:", font=custom_font_main)
amount_owed_on_trade_in_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
amount_owed_on_trade_in_entry = tk.Entry(root, font=custom_font_main)
amount_owed_on_trade_in_entry.grid(row=4, column=1, padx=5, pady=5)

loan_length_label = tk.Label(root, text="Length of loan (months):", font=custom_font_main)
loan_length_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
loan_length_entry = tk.Entry(root, font=custom_font_main)
loan_length_entry.grid(row=5, column=1, padx=5, pady=5)

# Create the "Calculate" button with image and text
calculate_button = tk.Button(root, text="Calculate", image=calculate_photo, compound=tk.LEFT, command=calculate_payment, font=custom_font_main, width=120, height=40)
calculate_button.grid(row=6, column=0, padx=5, pady=5, sticky="ew")

# Create the "Exit" button
exit_button = tk.Button(root, text="Exit", image=exit_photo, compound=tk.LEFT, command=root.destroy, font=custom_font_main, width=120, height=40)
exit_button.grid(row=6, column=1, padx=5, pady=5, sticky="ew")

# Run the Tkinter event loop
root.mainloop()
