import tkinter as tk
from tkinter import messagebox

# Function to handle the submission
def submit_form():
    student_name = entry_name.get()
    student_id = entry_id.get()
    email_id = entry_email.get()
    phone_number = entry_phone.get()
    address = entry_address.get()

    if not student_name or not student_id or not email_id or not phone_number or not address:
        messagebox.showerror("Error", "Please fill in all fields!")
    else:
        # If all fields are filled, show a success message
        messagebox.showinfo("Success", "Form submitted successfully!")

# Create the main window
root = tk.Tk()
root.title("Student Login Form")
root.geometry("400x400")
root.config(bg="#90EE90")  # Light green background

# Create a frame to center the fields
frame = tk.Frame(root, bg="#90EE90")
frame.place(relx=0.5, rely=0.5, anchor="center")

# Create the labels and entry fields
label_name = tk.Label(frame, text="Student Name:", bg="#90EE90", font=("Arial", 12))
label_name.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(frame, font=("Arial", 12))
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_id = tk.Label(frame, text="Student ID:", bg="#90EE90", font=("Arial", 12))
label_id.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_id = tk.Entry(frame, font=("Arial", 12))
entry_id.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(frame, text="Email ID:", bg="#90EE90", font=("Arial", 12))
label_email.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_email = tk.Entry(frame, font=("Arial", 12))
entry_email.grid(row=2, column=1, padx=10, pady=5)

label_phone = tk.Label(frame, text="Phone Number:", bg="#90EE90", font=("Arial", 12))
label_phone.grid(row=3, column=0, padx=10, pady=5, sticky="w")
entry_phone = tk.Entry(frame, font=("Arial", 12))
entry_phone.grid(row=3, column=1, padx=10, pady=5)

label_address = tk.Label(frame, text="Address:", bg="#90EE90", font=("Arial", 12))
label_address.grid(row=4, column=0, padx=10, pady=5, sticky="w")
entry_address = tk.Entry(frame, font=("Arial", 12))
entry_address.grid(row=4, column=1, padx=10, pady=5)

# Submit button
submit_button = tk.Button(frame, text="Submit", command=submit_form, bg="#90EE90", font=("Arial", 12))
submit_button.grid(row=5, columnspan=2, pady=20)

# Start the Tkinter event loop
root.mainloop()
