import tkinter as tk
from tkinter import ttk
from cadastro_produtos import abrir_cadastro_produto
from cadastro_fornecedores import abrir_fornecedores
import json
import os

def abrir_entrada():
    from entrada import abrir_entrada
    janela.destroy()
    abrir_entrada()

def abrir_produtos():
    janela.destroy()
    abrir_cadastro_produto()

def abrir_fornecedores_sistema():
    janela.destroy()
    abrir_fornecedores()

def abrir():
    global janela
    janela = tk.Tk()
    janela.title("Mecânica do Zé")
    janela.geometry("1600x1600")
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
    command=abrir_produtos
    
)
    
    botao_aba1.pack(pady=20)

    tabela1.heading("codigo", text="Código")
    tabela1.heading("nome", text="Descrição")
    tabela1.heading("quantidade", text="Quantidade")

    tabela1.column("codigo", width=80, anchor="center")
    tabela1.column("nome", width=300, anchor="center")
    tabela1.column("quantidade", width=120, anchor="center")



    arquivo = "cadastro_produtos.json"

    if os.path.exists(arquivo):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                produtos = json.load(f)

            for produto in produtos:
                tabela1.insert(
                    "",
                    tk.END,
                    values=(
                        produto.get("codigo",""),
                        produto.get("nome",""),
                        produto.get("quantidade","")
                    )
                )
        except:
            pass

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

    arquivo = "cadastro_produtos.json"

    if os.path.exists(arquivo):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                produtos = json.load(f)

            for produto in produtos:
                tabela2.insert(
                    "",
                    tk.END,
                    values=(
                        produto.get("codigo",""),
                        produto.get("nome",""),
                        produto.get("preco",""),
                        produto.get("localizacao","")
                    )
                )
        except:
            pass

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
    columns=("codigo", "empresa", "contato", "telefone", "email", "categoria"),
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
    command=abrir_fornecedores_sistema
)
    botao_aba3.pack(pady=20)

    tabela3.heading("codigo", text="Código")
    tabela3.heading("empresa", text="Empresa")
    tabela3.heading("contato", text="Contato")
    tabela3.heading("telefone", text="Telefone")
    tabela3.heading("email", text="E-mail")
    tabela3.heading("categoria", text="Categoria")

    tabela3.column("codigo", width=70, anchor="center")
    tabela3.column("empresa", width=220, anchor="center")
    tabela3.column("contato", width=150, anchor="center")
    tabela3.column("telefone", width=120, anchor="center")
    tabela3.column("email", width=220, anchor="center")
    tabela3.column("categoria", width=150, anchor="center")

    arquivo = "cadastro_fornecedores.json"

    if os.path.exists(arquivo):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                fornecedores = json.load(f)

            for fornecedor in fornecedores:
                tabela3.insert(
                    "",
                    tk.END,
                    values=(
                        fornecedor.get("codigo", ""),
                        fornecedor.get("empresa", ""),
                        fornecedor.get("contato", ""),
                        fornecedor.get("telefone", ""),
                        fornecedor.get("email", ""),
                        fornecedor.get("categoria", "")
                    )
                )
        except:
            pass

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
        columns=("codigo", "cliente", "data"),
        show="headings"
    )

    tabela4.heading("codigo", text="Código")
    tabela4.heading("cliente", text="Cliente")
    tabela4.heading("data", text="Data")

    tabela4.column("codigo", width=100, anchor="center")
    tabela4.column("cliente", width=250, anchor="center")
    tabela4.column("data", width=180, anchor="center")

    arquivo = "cadastro_vendas.json"

    if os.path.exists(arquivo):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                vendas = json.load(f)

            for venda in vendas:
                tabela4.insert(
                    "",
                    tk.END,
                    values=(
                        venda.get("codigo", ""),
                        venda.get("cliente", ""),
                        venda.get("data", "")
                    )
                )
        except:
            pass

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
        columns=("codigo", "cliente", "data", "valor"),
        show="headings"
    )

    tabela5.heading("codigo", text="Código")
    tabela5.heading("cliente", text="Cliente")
    tabela5.heading("data", text="Data")
    tabela5.heading("valor", text="Valor (R$)")

    tabela5.column("codigo", width=100, anchor="center")
    tabela5.column("cliente", width=250, anchor="center")
    tabela5.column("data", width=180, anchor="center")
    tabela5.column("valor", width=120, anchor="center")

    arquivo = "cadastro_vendas.json"

    if os.path.exists(arquivo):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                vendas = json.load(f)

            for venda in vendas:
                tabela5.insert(
                    "",
                    tk.END,
                    values=(
                        venda.get("codigo", ""),
                        venda.get("cliente", ""),
                        venda.get("data", ""),
                        venda.get("valor", "")
                    )
                )
        except:
            pass

    tabela5.pack(expand=True, fill="both", padx=20, pady=20)

    botao = tk.Button(
        janela,
        text="Voltar",
        font=("Arial", 12, "bold"),
        fg="#1E293B",
        bg="#E2E8F0",
        activeforeground="#49628c",
        activebackground="#f0f6fc",
        relief="flat",
        padx=20,
        pady=10,
        cursor="hand2",
        command=abrir_entrada
    )
    botao.pack(pady=20)

    janela.mainloop()
