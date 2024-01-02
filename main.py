import tkinter as tk
from tkinter import ttk
from api import getSigns, getHoroscope
from PIL import Image, ImageTk

class HoroscopeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Horoscope App")

        self.signs = getSigns()

        # Sign selection
        self.sign_label = ttk.Label(root, text="Choose your zodiac sign:")
        self.sign_combobox = ttk.Combobox(root, values=self.signs, state="readonly")
        self.sign_label.pack(pady=10)
        self.sign_combobox.pack(pady=10)

        # Timeframe selection
        self.timeframe_label = ttk.Label(root, text="Choose the timeframe:")
        self.timeframe_combobox = ttk.Combobox(
            root, values=["today", "yesterday", "tomorrow"], state="readonly"
        )
        self.timeframe_label.pack(pady=10)
        self.timeframe_combobox.pack(pady=10)

        # Button to get horoscope
        self.get_horoscope_button = ttk.Button(
            root, text="Get Horoscope", command=self.get_horoscope
        )
        self.get_horoscope_button.pack(pady=20)

        # Display result
        self.result_label = ttk.Label(root, text="", wraplength=400)
        self.result_label.pack(pady=10)

        # Image label
        self.image_label = ttk.Label(root, image=None)
        self.image_label.pack(pady=10)

    def get_horoscope(self):
        sign_to_fetch = self.sign_combobox.get()
        timeframe = self.timeframe_combobox.get()

        if not sign_to_fetch or not timeframe:
            self.result_label.config(text="Please select both sign and timeframe.")
            return

        horoscope = getHoroscope(sign_to_fetch, timeframe)
        self.result_label.config(text=f"\n\n{horoscope['horoscope']}\n\n")

        self.show_sign_image(sign_to_fetch.lower())

    def show_sign_image(self, sign):
        try:
            # Load image
            image_path = f"images/{sign}.png"
            img = Image.open(image_path)
            img = img.resize((200, 200))
            photo = ImageTk.PhotoImage(img)

            # Set image to label
            self.image_label.config(image=photo)
            self.image_label.image = photo
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HoroscopeApp(root)
    root.geometry("500x650")  # Set window size
    root.mainloop()
