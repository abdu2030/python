from tkinter import *
from tkinter import font
import requests


def get_quote():
    try:
        response = requests.get(
            "https://api.kanye.rest",
            timeout=10
        )
        response.raise_for_status()

        quote = response.json()["quote"]

        # Start with a large font.
        quote_font.config(size=30)

        # Put the new quote on the canvas.
        canvas.itemconfig(quote_text, text=quote)

        # Check the area occupied by the quote.
        text_box = canvas.bbox(quote_text)

        # Reduce the font until the text fits inside the background.
        while text_box and (
            text_box[2] - text_box[0] > 260
            or text_box[3] - text_box[1] > 330
        ):
            current_size = quote_font.cget("size")

            # Do not make the text smaller than 14.
            if current_size <= 14:
                break

            quote_font.config(size=current_size - 1)
            text_box = canvas.bbox(quote_text)

    except requests.RequestException:
        canvas.itemconfig(
            quote_text,
            text="Unable to get a quote. Check your internet connection."
        )


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(
    width=300,
    height=414,
    highlightthickness=0
)

background_img = PhotoImage(file="background.png")
canvas.create_image(
    150,
    207,
    image=background_img
)

# Create a font that can be resized later.
quote_font = font.Font(
    family="Arial",
    size=30,
    weight="bold"
)

quote_text = canvas.create_text(
    150,
    207,
    text="Click Kanye for a quote",
    width=250,
    font=quote_font,
    fill="white",
    justify="center"
)

canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")

kanye_button = Button(
    image=kanye_img,
    highlightthickness=0,
    command=get_quote
)

kanye_button.grid(row=1, column=0)

window.mainloop()