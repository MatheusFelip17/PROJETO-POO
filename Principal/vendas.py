import tkinter as tk
from tkinter import messagebox
import json
import os

arquivo_vendas = "cadastro_vendas.json"
arquivo_produtos = "cadastro_produtos.json"

produtos = []
itens_venda = []


def atualizar_lista_venda():
    lista_venda.delete(0, tk.END)

    total = 0

    for item in itens_venda:
        lista_venda.insert(
            tk.END,
            f"{item['nome']} | Qtd: {item['quantidade']} | R$ {item['subtotal']:.2f}"
        )
        total += item["subtotal"]

    txt_valor.config(state="normal")
    txt_valor.delete(0, tk.END)
    txt_valor.insert(0, f"{total:.2f}")
    txt_valor.config(state="readonly")


def adicionar_produto():
    selecao = lista_produtos.curselection()

    if not selecao:
        messagebox.showerror("Erro", "Selecione um produto.")
        return

    try:
        quantidade = int(txt_quantidade.get())

        if quantidade <= 0:
            raise ValueError

    except:
        messagebox.showerror("Erro", "Digite uma quantidade válida.")
        return

    indice = selecao[0]
    produto = produtos[indice]

    preco = float(produto.get("preco", 0))
    subtotal = preco * quantidade

    item = {
        "nome": produto.get("nome", "Sem nome"),
        "preco": preco,
        "quantidade": quantidade,
        "subtotal": subtotal
    }

    itens_venda.append(item)

    atualizar_lista_venda()

    txt_quantidade.delete(0, tk.END)
    txt_quantidade.insert(0, "1")


def remover_produto():
    selecao = lista_venda.curselection()

    if not selecao:
        messagebox.showerror(
            "Erro",
            "Selecione um item para remover."
        )
        return

    indice = selecao[0]

    del itens_venda[indice]

    atualizar_lista_venda()


def salvar_venda():
    cliente = txt_cliente.get().strip()
    cpf = txt_cpf.get().strip()

    txt_valor.config(state="normal")
    valor = txt_valor.get()
    txt_valor.config(state="readonly")

    if cliente == "" or cpf == "":
        messagebox.showerror(
            "Erro",
            "Preencha cliente e CPF."
        )
        return

    if len(itens_venda) == 0:
        messagebox.showerror(
            "Erro",
            "Adicione pelo menos um produto."
        )
        return

    if os.path.exists(arquivo_vendas):
        try:
            with open(
                arquivo_vendas,
                "r",
                encoding="utf-8"
            ) as f:
                vendas = json.load(f)
        except:
            vendas = []
    else:
        vendas = []

    codigo = len(vendas) + 1

    venda = {
        "codigo": f"V{codigo:03}",
        "cliente": cliente,
        "cpf": cpf,
        "produtos": itens_venda.copy(),
        "valor": valor
    }

    vendas.append(venda)

    with open(
        arquivo_vendas,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            vendas,
            f,
            indent=4,
            ensure_ascii=False
        )

    messagebox.showinfo(
        "Sucesso",
        "Venda cadastrada com sucesso!"
    )

    txt_cliente.delete(0, tk.END)
    txt_cpf.delete(0, tk.END)

    itens_venda.clear()

    lista_venda.delete(0, tk.END)

    txt_valor.config(state="normal")
    txt_valor.delete(0, tk.END)
    txt_valor.insert(0, "0.00")
    txt_valor.config(state="readonly")

    lbl_codigo.config(
        text=f"Código da Venda: V{codigo + 1:03}"
    )


def abrir_nova_venda():
    global txt_cliente
    global txt_cpf
    global txt_quantidade
    global txt_valor
    global lbl_codigo
    global lista_produtos
    global lista_venda
    global produtos

    if os.path.exists(arquivo_vendas):
        try:
            with open(
                arquivo_vendas,
                "r",
                encoding="utf-8"
            ) as f:
                vendas = json.load(f)

            proximo = len(vendas) + 1

        except:
            proximo = 1
    else:
        proximo = 1

    try:
        with open(
            arquivo_produtos,
            "r",
            encoding="utf-8"
        ) as f:
            produtos = json.load(f)

    except:
        produtos = []

    janela = tk.Tk()

    janela.title("Cadastro de Venda")
    janela.geometry("650x700")
    janela.configure(bg="#1E293B")

    titulo = tk.Label(
        janela,
        text="Cadastro de Venda",
        font=("Arial", 18, "bold"),
        bg="#1E293B",
        fg="#E2E8F0"
    )
    titulo.pack(pady=10)

    lbl_codigo = tk.Label(
        janela,
        text=f"Código da Venda: V{proximo:03}",
        font=("Arial", 12, "bold"),
        bg="#1E293B",
        fg="#E2E8F0"
    )
    lbl_codigo.pack(pady=5)

    tk.Label(
        janela,
        text="Cliente",
        bg="#1E293B",
        fg="#E2E8F0"
    ).pack()

    txt_cliente = tk.Entry(
        janela,
        width=40
    )
    txt_cliente.pack(pady=5)

    tk.Label(
        janela,
        text="CPF",
        bg="#1E293B",
        fg="#E2E8F0"
    ).pack()

    txt_cpf = tk.Entry(
        janela,
        width=40
    )
    txt_cpf.pack(pady=5)

    tk.Label(
        janela,
        text="Produtos Disponíveis",
        bg="#1E293B",
        fg="#E2E8F0"
    ).pack(pady=(10, 0))

    lista_produtos = tk.Listbox(
        janela,
        width=50,
        height=8
    )
    lista_produtos.pack(pady=5)

    for produto in produtos:
        nome = produto.get("nome", "Sem nome")
        preco = float(produto.get("preco", 0))

        lista_produtos.insert(
            tk.END,
            f"{nome} - R$ {preco:.2f}"
        )

    tk.Label(
        janela,
        text="Quantidade",
        bg="#1E293B",
        fg="#E2E8F0"
    ).pack()

    txt_quantidade = tk.Entry(
        janela,
        width=10
    )
    txt_quantidade.insert(0, "1")
    txt_quantidade.pack(pady=5)

    tk.Button(
        janela,
        text="Adicionar Produto",
        command=adicionar_produto,
        font=("Arial", 10, "bold")
    ).pack(pady=5)

    tk.Label(
        janela,
        text="Itens da Venda",
        bg="#1E293B",
        fg="#E2E8F0"
    ).pack(pady=(10, 0))

    lista_venda = tk.Listbox(
        janela,
        width=60,
        height=10
    )
    lista_venda.pack(pady=5)

    tk.Button(
        janela,
        text="Remover Produto",
        command=remover_produto,
        font=("Arial", 10, "bold")
    ).pack(pady=5)

    tk.Label(
        janela,
        text="Valor Total (R$)",
        bg="#1E293B",
        fg="#E2E8F0"
    ).pack(pady=(10, 0))

    txt_valor = tk.Entry(
        janela,
        width=40
    )
    txt_valor.pack(pady=5)

    txt_valor.insert(0, "0.00")
    txt_valor.config(state="readonly")

    botao = tk.Button(
        janela,
        text="Cadastrar Venda",
        command=salvar_venda,
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

    janela.mainloop()


abrir_nova_venda()