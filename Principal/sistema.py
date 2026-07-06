import tkinter as tk
from tkinter import ttk

def abrir():
    janela = tk.Tk()
    janela.title("Sistema")
    janela.geometry("980x680")
    janela.configure(bg="#1E293B")

    abas = ttk.Notebook(janela)
    abas.pack(expand=True, fill="both")

    aba1 = tk.Frame(abas)
    aba2 = tk.Frame(abas)

    abas.add(aba1, text="Depósito")
    abas.add(aba2, text="Tabela de preços")

    Tabela = ttk.Treeview(
    aba1,
    columns=("codigo", "nome", "quantidade"),
    show="headings"
)
    
    Tabela.heading("codigo", text="Código")
    Tabela.heading("nome", text="Descrição")
    Tabela.heading("quantidade", text="Quantidade")

    Tabela.column("codigo", width=60, anchor="center")
    Tabela.column("nome", width=200, anchor="center")
    Tabela.column("quantidade", width=80, anchor="center")

    Tabela.insert("", tk.END, values=("001", "Filtro de óleo", 50))
    Tabela.insert("", tk.END, values=("002", "Pastilha de freio dianteira", 50))
    Tabela.insert("", tk.END, values=("003", "Amortecedor dianteiro", 50))
    Tabela.insert("", tk.END, values=("004", "Vela de ignição", 50))

    Tabela.pack(expand=True, fill="both", padx=10, pady=10)

    tabela = ttk.Treeview(
    aba2,
    columns=("codigo", "nome", "preco", "localizacao"),
    show="headings"
)
    
    tabela.heading("codigo", text="Código")
    tabela.heading("nome", text="Descrição")
    tabela.heading("preco", text="Preço(R$)")
    tabela.heading("localizacao", text="Localização")

    tabela.column("codigo", width=60, anchor="center")
    tabela.column("nome", width=200, anchor="center")
    tabela.column("preco", width=80, anchor="center")
    tabela.column("localizacao", width=150, anchor="center")

    tabela.insert("", tk.END, values=("001", "Filtro de óleo", "32.50", "Setor A1"))
    tabela.insert("", tk.END, values=("002", "Pastilha de freio dianteira", "139.90", "Setor C2"))
    tabela.insert("", tk.END, values=("003", "Amortecedor dianteiro", "329.90", "Setor C1"))
    tabela.insert("", tk.END, values=("004", "Vela de ignição", "29.90", "Setor C1"))

    tabela.pack(expand=True, fill="both", padx=10, pady=10)

    janela.mainloop()