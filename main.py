from Estilo.estilo import configurar_estilos


def main():
    import tkinter as tk
    nome = "Mecânica do Zé"
    janela = tk.Tk()
    janela.title(f"{nome} - Sistema")
    janela.geometry("980x680")
    janela.minsize(820, 560)

    configurar_estilos()
    texto = tk.Label(janela, text=f"Seja bem-vindo(a)!\nEste é o sistema de estoque da {nome}.", font=("Courier New", 20))
    texto.pack(pady=40)

    janela.mainloop()


if __name__ == "__main__":
    main()
