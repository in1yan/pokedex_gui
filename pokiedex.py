import tkinter as tk
from io import BytesIO

import PIL.Image
import PIL.ImageTk
import pypokedex
import urllib3

window = tk.Tk()
window.geometry("600x600")
window.title("Pokedex")
window.config(padx=20, pady=20)

title_lable = tk.Label(window, text="Pokedex")

title_lable.config(font=("Arial", 32))
title_lable.pack(padx=10, pady=10)


pokiemon_image = tk.Label(window)

pokiemon_image.pack(padx=10, pady=10)

pokiemon_information = tk.Label(window)
pokiemon_information.config(font=("Arial", 32))
pokiemon_information.pack(padx=10, pady=10)

pokiemon_types = tk.Label(window)
pokiemon_types.config(font=("Arial", 32))
pokiemon_types.pack(padx=10, pady=10)


def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
    http = urllib3.PoolManager()
    response = http.request("GET", pokemon.sprites.front.get("default"))
    image = PIL.Image.open(BytesIO(response.data))
    img = PIL.ImageTk.PhotoImage(image)
    pokiemon_image.config(image=img)
    pokiemon_image.image = img

    pokiemon_information.config(text=f"{pokemon.dex} - {pokemon.name}")
    pokiemon_types.config(text="-".join([t for t in pokemon.types]))


# function

label_id_name = tk.Label(window, text="ID or name")
label_id_name.config(font=("Arial", 20))

label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(window, text="load pokemon", command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)


window.mainloop()
