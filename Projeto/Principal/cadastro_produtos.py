import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

arquivo = "cadastro_produtos.json"

def abrir_sistema():
    from sistema import abrir
    janela.destroy()
    abrir()

def salvar_produto():
    codigo = txt_codigo.get()
    nome = txt_nome.get()
    categoria = txt_categoria.get()
    quantidade = txt_quantidade.get()
    preco = txt_preco.get()
    localizacao = txt_localizacao.get()

    if codigo == "" or nome == "" or categoria == "" or quantidade == "" or preco == "" or localizacao == "":
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return

    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            produtos = json.load(f)
    else:
        produtos = []

    produto = {
        "codigo": codigo,
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "preco": preco,
        "localizacao": localizacao
    }

    produtos.append(produto)

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(produtos, f, indent=4, ensure_ascii=False)

    messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")

    txt_codigo.delete(0, tk.END)
    txt_nome.delete(0, tk.END)
    txt_categoria.current(0)
    txt_quantidade.delete(0, tk.END)
    txt_preco.delete(0, tk.END)
    txt_localizacao.current(0)


def abrir_cadastro_produto():
    global txt_codigo
    global txt_nome
    global txt_categoria
    global txt_quantidade
    global txt_preco
    global txt_localizacao
    global janela

    janela = tk.Tk()
    janela.title("Sistema - Cadastro de produto")
    janela.geometry("980x790")
    janela.configure(bg="#1E293B")

    titulo = tk.Label(
        janela,
        text="Cadastro de Produtos",
        font=("Arial", 18, "bold"),
        bg="#1E293B",
        fg="#E2E8F0"
    )
    titulo.pack(pady=15)

    tk.Label(
        janela,
        text="Código",
        bg="#1E293B",
        fg="#E2E8F0"
    ).pack()

    txt_codigo = tk.Entry(janela, width=40)
    txt_codigo.pack(pady=5)

    tk.Label(
        janela,
        text="Nome",
        bg="#1E293B",
        fg="#E2E8F0"
    ).pack()

    txt_nome = tk.Entry(janela, width=40)
    txt_nome.pack(pady=5)

    tk.Label(
        janela,
        text="Categoria",
        bg="#1E293B",
        fg="#E2E8F0"
    ).pack()

    categorias = [
        "Motor",
        "Freios",
        "Suspensão",
        "Elétrica",
        "Transmissão",
        "Lubrificantes",
        "Filtros",
        "Pneus",
        "Acessórios",
        "Parafusos",
        "Rolamentos",
        "Correias",
        "Mangueiras",
        "Baterias",
        "Outros"
    ]

    txt_categoria = ttk.Combobox(
        janela,
        values=categorias,
        width=37,
        state="readonly"
    )
    txt_categoria.pack(pady=5)
    txt_categoria.current(0)

    tk.Label(
        janela,
        text="Quantidade",
        bg="#1E293B",
        fg="#E2E8F0"
    ).pack()

    txt_quantidade = tk.Entry(janela, width=40)
    txt_quantidade.pack(pady=5)

    tk.Label(
        janela,
        text="Preço (R$)",
        bg="#1E293B",
        fg="#E2E8F0"
    ).pack()

    txt_preco = tk.Entry(janela, width=40)
    txt_preco.pack(pady=5)

    tk.Label(
        janela,
        text="Localização",
        bg="#1E293B",
        fg="#E2E8F0"
    ).pack()

    setores = [
        "Setor A1",
        "Setor A2",
        "Setor A3",
        "Setor A4",
        "Setor A5",
        "Setor B1",
        "Setor B2",
        "Setor B3",
        "Setor B4",
        "Setor B5",
        "Setor C1",
        "Setor C2",
        "Setor C3",
        "Setor C4",
        "Setor C5",
        "Setor D1",
        "Setor D2",
        "Setor D3",
        "Setor D4",
        "Setor D5",
        "Setor E1",
        "Setor E2",
        "Setor E3",
        "Setor E4",
        "Setor E5",
        "Prateleira 1",
        "Prateleira 2",
        "Prateleira 3",
        "Prateleira 4",
        "Prateleira 5",
        "Estoque Principal",
        "Almoxarifado",
        "Área de Peças Grandes",
        "Área de Peças Pequenas"
    ]

    txt_localizacao = ttk.Combobox(
        janela,
        values=setores,
        width=37,
        state="readonly"
    )
    txt_localizacao.pack(pady=5)
    txt_localizacao.current(0)

    botao = tk.Button(
        janela,
        text="Cadastrar Produto",
        command=salvar_produto,
        font=("Arial", 11, "bold"),
        fg="#1E293B",
        bg="#E2E8F0",
        activeforeground="#49628c",
        activebackground="#f0f6fc",
        relief="flat",
        padx=20,
        pady=10,
        cursor="hand2"
    )
    botao.pack(pady=20)

    titulo.pack(pady=40)

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
        command=abrir_sistema 
    )
    botao.pack(pady=20)


    janela.mainloop()