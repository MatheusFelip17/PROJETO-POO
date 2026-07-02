import tkinter as tk
from sistema import abrir


def abrir_sistema():
    janela.destroy()
    abrir()


janela = tk.Tk()

janela.title("Mecânica do Zé")
janela.geometry("980x680")
janela.minsize(820, 560)
janela.configure(bg="#1E293B")

titulo = tk.Label(
    janela,
    text="Mecânica do Zé",
    font=("Arial", 40, "bold"),
    bg="#1E293B",
    fg="#E2E8F0"
)
titulo.pack(pady=40)

botao = tk.Button(
    janela,
    text="Entrar",
    font=("Arial", 12, "bold"),
    fg="#1E293B",
    bg="#E2E8F0",
    activeforeground="#49628c",
    activebackground="#f0f6fc",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2",
    command=abrir_sistema
)
botao.pack(pady=20)

janela.mainloop()