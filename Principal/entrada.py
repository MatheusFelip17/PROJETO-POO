import tkinter as tk
from sistema import abrir
from vendas import abrir_nova_venda


def abrir_sistema():
    janela.destroy()
    abrir()


def abrir_vendas():
    janela.destroy()
    abrir_nova_venda()

def abrir_entrada():
    global janela
    janela = tk.Tk()

    janela.title("Mecânica do Zé")
    janela.geometry("1600x1600")
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

    botao1 = tk.Button(
        janela,
        text="Nova Venda",
        font=("Arial", 12, "bold"),
        fg="#1E293B",
        bg="#E2E8F0",
        activeforeground="#F0F6FC",
        activebackground="#49628c",
        relief="flat",
        padx=20,
        pady=10,
        cursor="hand2",
        command=abrir_vendas 
    )
    botao1.pack(pady=20)

    janela.mainloop()
if __name__ == "__main__":
    abrir_entrada()