#Author:  Travis Whiteside
#Date written: 01/24/2024
#Assignment:   Gui Project
#Short Desc: This program will calculate the payment of a car you are looking to purchase. It will take into consideration the following variables: Price, Downpayment, Intrest rate, Length of loan, Trade in value, Amount you owe on the traded in car

import tkinter as tk
from tkinter import messagebox

def calculate_payment():
    try:
        # Get input values
        price = float(price_entry.get())
        interest_rate = float(interest_rate_entry.get()) / 100  # Convert percentage to decimal
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
        total_price = price + total_interest_paid

        # Update the result text widget
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)  # Clear previous content
        result_text.insert(tk.END, f"Monthly Payment: ${monthly_payment:.2f}\n")
        result_text.insert(tk.END, f"Total Interest Paid: ${total_interest_paid:.2f}\n")
        result_text.insert(tk.END, f"Total Price of the Car: ${total_price:.2f}")
        result_text.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

def reset_inputs():
    price_entry.delete(0, tk.END)
    interest_rate_entry.delete(0, tk.END)
    down_payment_entry.delete(0, tk.END)
    trade_in_value_entry.delete(0, tk.END)
    amount_owed_on_trade_in_entry.delete(0, tk.END)
    loan_length_entry.delete(0, tk.END)
    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.config(state=tk.DISABLED)

def close_window():
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Car Payment Calculator")

# Set the size of the window
root.geometry("550x350")

# Set the font
custom_font = ("Georgia", 12, "bold")

# Create input labels and entry widgets
price_label = tk.Label(root, text="Price of the car:", font=custom_font)
price_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
price_entry = tk.Entry(root, font=custom_font)
price_entry.grid(row=0, column=1, padx=5, pady=5)

interest_rate_label = tk.Label(root, text="Interest rate (%):", font=custom_font)
interest_rate_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
interest_rate_entry = tk.Entry(root, font=custom_font)
interest_rate_entry.grid(row=1, column=1, padx=5, pady=5)

down_payment_label = tk.Label(root, text="Down payment:", font=custom_font)
down_payment_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
down_payment_entry = tk.Entry(root, font=custom_font)
down_payment_entry.grid(row=2, column=1, padx=5, pady=5)

trade_in_value_label = tk.Label(root, text="Trade-in value:", font=custom_font)
trade_in_value_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
trade_in_value_entry = tk.Entry(root, font=custom_font)
trade_in_value_entry.grid(row=3, column=1, padx=5, pady=5)

amount_owed_on_trade_in_label = tk.Label(root, text="Amount owed on trade-in:", font=custom_font)
amount_owed_on_trade_in_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
amount_owed_on_trade_in_entry = tk.Entry(root, font=custom_font)
amount_owed_on_trade_in_entry.grid(row=4, column=1, padx=5, pady=5)

loan_length_label = tk.Label(root, text="Length of loan (months):", font=custom_font)
loan_length_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
loan_length_entry = tk.Entry(root, font=custom_font)
loan_length_entry.grid(row=5, column=1, padx=5, pady=5)

# Create buttons
calculate_button = tk.Button(root, text="Calculate", command=calculate_payment, font=custom_font)
calculate_button.grid(row=6, column=0, padx=5, pady=5, sticky="ew")

reset_button = tk.Button(root, text="Reset", command=reset_inputs, font=custom_font)
reset_button.grid(row=6, column=1, padx=5, pady=5, sticky="ew")

exit_button = tk.Button(root, text="Exit", command=close_window, font=custom_font)
exit_button.grid(row=6, column=2, padx=5, pady=5, sticky="ew")

# Create a text widget to display the result
result_text = tk.Text(root, height=5, width=50, font=custom_font)
result_text.grid(row=7, column=0, columnspan=3, padx=5, pady=10)
result_text.config(state=tk.DISABLED)  # Make the text widget read-only

# Run the Tkinter event loop
root.mainloop()
