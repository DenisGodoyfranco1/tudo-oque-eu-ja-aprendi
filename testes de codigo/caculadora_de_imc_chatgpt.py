import tkinter as tk

def calculate_imc():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    imc = weight / (height/100)**2
    imc_label.config(text="Seu IMC é: {:.2f}".format(imc))

root = tk.Tk()
root.title("Calculadora de IMC")

height_label = tk.Label(root, text="Altura (cm):")
height_label.pack()

height_entry = tk.Entry(root)
height_entry.pack()

weight_label = tk.Label(root, text="Peso (kg):")
weight_label.pack()

weight_entry = tk.Entry(root)
weight_entry.pack()

calculate_button = tk.Button(root, text="Calcular IMC", command=calculate_imc)
calculate_button.pack()

imc_label = tk.Label(root)
imc_label.pack()

root.mainloop()