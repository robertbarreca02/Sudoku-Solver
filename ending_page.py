from tkinter import *


# import landing_page


ending_page = Tk()
ending_page.title("Congratulations!")
ending_page.geometry("500x300")

# Add labels
congrats_label = Label(
    ending_page,
    text="Congratulations!",
    font=("Arial", 16),
)
results_label = Label(
    ending_page,
    text=f"You completed the board in 0 seconds and made 0 mistakes",
    font=("Arial", 14),
)
question_label = Label(
    ending_page,
    text=f"Would you like to play again?",
    font=("Arial", 14),
)
congrats_label.pack(pady=20)
results_label.pack(pady=20)
question_label.pack(pady=20)


# Function to restart the game
def play_again():
    print("yes pressed")

    # add buttons


buttons_frame = Frame(ending_page)
buttons_frame.pack()

no_button = Button(
    buttons_frame,
    text="No",
    font=("Arial", 12),
    command=ending_page.quit,
    width=10,
    height=5,
)
yes_button = Button(
    buttons_frame,
    text="Yes",
    font=("Arial", 12),
    command=play_again,
    width=10,
    height=5,
)

no_button.pack(side="left", pady=10, padx=20)
yes_button.pack(side="left", pady=10, padx=20)


ending_page.mainloop()
