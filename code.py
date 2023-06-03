import random
import tkinter as tk
from tkinter import messagebox

# Função para verificar a tentativa do jogador
def verificar_tentativa():
    tentativa = int(entry.get())

    if tentativa == numero_secreto:
        messagebox.showinfo("Resultado", "Parabéns! Você acertou!")
        janela.quit()
    elif tentativa < numero_secreto:
        messagebox.showinfo("Resultado", "Tente um número maior.")
    else:
        messagebox.showinfo("Resultado", "Tente um número menor.")

# Gera um número aleatório entre 1 e 100
numero_secreto = random.randint(1, 100)

# Cria a janela principal
janela = tk.Tk()
janela.title("Jogo de Adivinhação")

# Cria os componentes da interface
label = tk.Label(janela, text="Tente adivinhar o número:")
label.pack()

entry = tk.Entry(janela)
entry.pack()

button = tk.Button(janela, text="Verificar", command=verificar_tentativa)
button.pack()

# Inicia a execução da interface gráfica
janela.mainloop()
