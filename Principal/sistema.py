import tkinter as tk

def abrir():
    janela = tk.Tk()

    janela.title("Sistema")
    janela.geometry("980x680")
    janela.minsize(820, 560)
    janela.configure(bg="#1E293B")

    texto = tk.Label(
        janela,
        text="Bem-vindo ao Sistema da Mecânica do Zé!",
        font=("Arial", 14),
        bg="#1E293B",
        fg="#E2E8F0"
    )
    texto.pack(expand=True)

    janela.mainloop()