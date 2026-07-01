import tkinter as tk
from tkinter import ttk
from Estilo.estilo import configurar_estilos, COR_FUNDO


def main():
    nome = "Mecânica do Zé"

    janela = tk.Tk()
    janela.title(f"{nome} - Sistema")
    janela.geometry("980x680")
    janela.minsize(820, 560)
    janela.configure(bg=COR_FUNDO)

    configurar_estilos()

    texto = ttk.Label(
        janela,
        text=f"Seja bem-vindo(a)!\nEste é o sistema de estoque da {nome}.",
        style="Titulo.TLabel",
        anchor="center",
        justify="center"
    )
    texto.pack(pady=40)

    janela.mainloop()


if __name__ == "__main__":
    main()