import tkinter as tk
from tkinter import PhotoImage

# Create the main window
window = tk.Tk()
window.title("IRADS")

# making the window full screen
window.attributes("-fullscreen", True)

# maximing the size of the window
window.state("zoomed")


splash_screen = tk.Frame(window, bg="orange")
home = tk.Frame(window, bg="cyan")

# Load the image using PhotoImage
image = PhotoImage(file="image.gif")

# Create a label and set the image and text as the label's image and text
label = tk.Label(splash_screen, text="IRADS", image=image)
label.pack()

splash_screen.pack()

def closeSplashScreen():
    window.attributes("-fullscreen", False)
    splash_screen.pack_forget()
    home.pack()


# closing the splash and exiting fullscreen
window.after(3000, closeSplashScreen)

# Add a label with a message
label = tk.Label(home, text="Welcome to my program!", font=("Helvetica", 16))
label.pack()

# Add a button to close the splash screen and start the main program
button = tk.Button(home, text="Start", command=window.destroy)
button.pack()

# Run the main loop to display the splash screen
window.mainloop()
