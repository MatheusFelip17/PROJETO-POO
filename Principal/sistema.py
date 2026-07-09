import tkinter as tk
from tkinter import ttk
from cadastro_produtos import abrir_cadastro_produto
from cadastro_tabela import abrir_tabela
from cadastro_fornecedores import abrir_fornecedores
from cadastro_clientes import abrir_cliente
from cadastro_de_nova_venda import abrir_nova_venda

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

    botao_aba1 = tk.Button(
    aba1,
    text="Cadastrar Produto",
    font=("Arial", 12),
    fg="#1E293B",
    bg="#E2E8F0",
    activeforeground="#49628c",
    activebackground="#f0f6fc",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2",
    command=abrir_cadastro_produto
)
    
    botao_aba1.pack(pady=20)

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

    botao_aba2 = tk.Button(
    aba2,
    text="Cadastrar Produto",
    font=("Arial", 12),
    fg="#1E293B",
    bg="#E2E8F0",
    activeforeground="#49628c",
    activebackground="#f0f6fc",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2",
    command=abrir_tabela
)
    botao_aba2.pack(pady=20)

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

    titulo3 = tk.Label(
        aba3,
        text="Fornecedores",
        font=("Arial", 18, "bold"),
        bg="#1E293B",
        fg="#E2E8F0"
    )
    titulo3.pack(pady=15)

    tabela3 = ttk.Treeview(
        aba3,
        columns=("codigo", "fornecedores", "telefone"),
        show="headings"
    )

    botao_aba3 = tk.Button(
    aba3,
    text="Cadastrar Fornecedor",
    font=("Arial", 12),
    fg="#1E293B",
    bg="#E2E8F0",
    activeforeground="#49628c",
    activebackground="#f0f6fc",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2",
    command=abrir_fornecedores
)
    botao_aba3.pack(pady=20)

    tabela3.heading("codigo", text="Código")
    tabela3.heading("fornecedores", text="Fornecedores")
    tabela3.heading("telefone", text="telefone")

    tabela3.column("codigo", width=80, anchor="center")
    tabela3.column("fornecedores", width=300, anchor="center")
    tabela3.column("telefone", width=120, anchor="center")

    tabela3.insert("", tk.END, values=("F001", "Auto Peças Brasil", "(11)99999-1111"))
    tabela3.insert("", tk.END, values=("F002", "Pastilha de freio dianteira", "(21)98888-1111"))

    tabela3.pack(expand=True, fill="both", padx=20, pady=20)

    titulo4 = tk.Label(
        aba4,
        text="Clientes",
        font=("Arial", 18, "bold"),
        bg="#1E293B",
        fg="#E2E8F0"
    )
    titulo4.pack(pady=15)

    tabela4 = ttk.Treeview(
        aba4,
        columns=("codigo", "cliente", "cpf"),
        show="headings"
    )

    botao_aba4 = tk.Button(
    aba4,
    text="Cadastrar Cliente",
    font=("Arial", 12),
    fg="#1E293B",
    bg="#E2E8F0",
    activeforeground="#49628c",
    activebackground="#f0f6fc",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2",
    command=abrir_cliente
)
    botao_aba4.pack(pady=20)

    tabela4.heading("codigo", text="Código")
    tabela4.heading("cliente", text="Clientes")
    tabela4.heading("cpf", text="CPF")

    tabela4.column("codigo", width=80, anchor="center")
    tabela4.column("cliente", width=300, anchor="center")
    tabela4.column("cpf", width=120, anchor="center")

    tabela4.insert("", tk.END, values=("C001", "João Silva", "327.564.908-11"))
    tabela4.insert("", tk.END, values=("C002", "Maria Souza", "123.667.432-69"))

    tabela4.pack(expand=True, fill="both", padx=20, pady=20)

    titulo5 = tk.Label(
        aba5,
        text="Vendas",
        font=("Arial", 18, "bold"),
        bg="#1E293B",
        fg="#E2E8F0"
    )
    titulo5.pack(pady=15)

    tabela5 = ttk.Treeview(
        aba5,
        columns=("venda", "cliente", "valor"),
        show="headings"
    )

    botao_aba5 = tk.Button(
    aba5,
    text="Cadastrar Nova Venda",
    font=("Arial", 12),
    fg="#1E293B",
    bg="#E2E8F0",
    activeforeground="#49628c",
    activebackground="#f0f6fc",
    relief="flat",
    padx=20,
    pady=10,
    cursor="hand2",
    command=abrir_nova_venda
)
    botao_aba5.pack(pady=20)

    tabela5.heading("venda", text="Vendas")
    tabela5.heading("cliente", text="Clientes")
    tabela5.heading("valor", text="Valor(R$)")

    tabela5.column("venda", width=80, anchor="center")
    tabela5.column("cliente", width=300, anchor="center")
    tabela5.column("valor", width=120, anchor="center")

    tabela5.insert("", tk.END, values=("V001", "João Silva", "199.90"))
    tabela5.insert("", tk.END, values=("V002", "Maria Souza", "359.80"))

    tabela5.pack(expand=True, fill="both", padx=20, pady=20)

    janela.mainloop()
