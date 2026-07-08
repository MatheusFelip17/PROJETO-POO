import tkinter as tk
from tkinter import ttk

def abrir():
    janela = tk.Tk()
    janela.title("Mecânica do Zé")
    janela.geometry("980x680")
    janela.minsize(820, 560)
    janela.configure(bg="#1E293B")

    style = ttk.Style()

    style.theme_use("default")

    style.configure(
        "TNotebook",
        background="#1E293B",
        borderwidth=0
    )

    style.configure(
        "TNotebook.Tab",
        background="#CBD5E1",
        foreground="#1E293B",
        padding=(12, 6),
        font=("Arial", 10, "bold")
    )

    style.map(
        "TNotebook.Tab",
        background=[("selected", "#E2E8F0")],
        foreground=[("selected", "#1E293B")]
    )

    style.configure(
        "Treeview",
        font=("Arial", 10),
        rowheight=28,
        background="#FFFFFF",
        fieldbackground="#FFFFFF",
        foreground="#1E293B"
    )

    style.configure(
        "Treeview.Heading",
        font=("Arial", 10, "bold"),
        background="#CBD5E1",
        foreground="#1E293B"
    )

    style.map(
        "Treeview.Heading",
        background=[("active", "#E2E8F0")]
    )

    abas = ttk.Notebook(janela)
    abas.pack(expand=True, fill="both")

    aba1 = tk.Frame(abas, bg="#1E293B")
    aba2 = tk.Frame(abas, bg="#1E293B")
    aba3 = tk.Frame(abas, bg="#1E293B")
    aba4 = tk.Frame(abas, bg="#1E293B")
    aba5 = tk.Frame(abas, bg="#1E293B")

    abas.add(aba1, text="Depósito")
    abas.add(aba2, text="Tabela de preços")
    abas.add(aba3, text="Fornecedores")
    abas.add(aba4, text="Clientes")
    abas.add(aba5, text="Vendas")

    titulo1 = tk.Label(
        aba1,
        text="Depósito",
        font=("Arial", 18, "bold"),
        bg="#1E293B",
        fg="#E2E8F0"
    )
    titulo1.pack(pady=15)

    tabela1 = ttk.Treeview(
        aba1,
        columns=("codigo", "nome", "quantidade"),
        show="headings"
    )

    tabela1.heading("codigo", text="Código")
    tabela1.heading("nome", text="Descrição")
    tabela1.heading("quantidade", text="Quantidade")

    tabela1.column("codigo", width=80, anchor="center")
    tabela1.column("nome", width=300, anchor="center")
    tabela1.column("quantidade", width=120, anchor="center")

    tabela1.insert("", tk.END, values=("001", "Filtro de óleo", 50))
    tabela1.insert("", tk.END, values=("002", "Pastilha de freio dianteira", 50))
    tabela1.insert("", tk.END, values=("003", "Amortecedor dianteiro", 50))
    tabela1.insert("", tk.END, values=("004", "Vela de ignição", 50))

    tabela1.pack(expand=True, fill="both", padx=20, pady=20)

    titulo2 = tk.Label(
        aba2,
        text="Tabela de preços",
        font=("Arial", 18, "bold"),
        bg="#1E293B",
        fg="#E2E8F0"
    )
    titulo2.pack(pady=15)

    tabela2 = ttk.Treeview(
        aba2,
        columns=("codigo", "nome", "preco", "localizacao"),
        show="headings"
    )

    tabela2.heading("codigo", text="Código")
    tabela2.heading("nome", text="Descrição")
    tabela2.heading("preco", text="Preço(R$)")
    tabela2.heading("localizacao", text="Localização")

    tabela2.column("codigo", width=80, anchor="center")
    tabela2.column("nome", width=300, anchor="center")
    tabela2.column("preco", width=120, anchor="center")
    tabela2.column("localizacao", width=150, anchor="center")

    tabela2.insert("", tk.END, values=("001", "Filtro de óleo", "32.50", "Setor A1"))
    tabela2.insert("", tk.END, values=("002", "Pastilha de freio dianteira", "139.90", "Setor C2"))
    tabela2.insert("", tk.END, values=("003", "Amortecedor dianteiro", "329.90", "Setor C1"))
    tabela2.insert("", tk.END, values=("004", "Vela de ignição", "29.90", "Setor C1"))

    tabela2.pack(expand=True, fill="both", padx=20, pady=20)

    abas_info = [
        (aba3, "Fornecedores", ("Código", "Fornecedor", "Telefone"),
         [("F001", "Auto Peças Brasil", "(11) 99999-1111"),
          ("F002", "Peças Premium", "(21) 98888-2222")]),

        (aba4, "Clientes", ("Código", "Cliente", "Cidade"),
         [("C001", "João Silva", "Natal"),
          ("C002", "Maria Souza", "Parnamirim")]),

        (aba5, "Vendas", ("Venda", "Cliente", "Valor(R$)"),
         [("0001", "João Silva", "199.90"),
          ("0002", "Maria Souza", "359.80")])
    ]

    for aba, titulo, colunas, dados in abas_info:
        label = tk.Label(
            aba,
            text=titulo,
            font=("Arial", 18, "bold"),
            bg="#1E293B",
            fg="#E2E8F0"
        )
        label.pack(pady=15)

        tabela = ttk.Treeview(
            aba,
            columns=colunas,
            show="headings"
        )

        for coluna in colunas:
            tabela.heading(coluna, text=coluna)
            tabela.column(coluna, width=200, anchor="center")

        for item in dados:
            tabela.insert("", tk.END, values=item)

        tabela.pack(expand=True, fill="both", padx=20, pady=20)

    janela.mainloop()
