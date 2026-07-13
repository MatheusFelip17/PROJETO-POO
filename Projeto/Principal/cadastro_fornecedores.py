import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

arquivo = "cadastro_fornecedores.json"


def salvar_fornecedor():
    codigo = txt_codigo.get()
    empresa = txt_empresa.get()
    contato = txt_contato.get()
    telefone = txt_telefone.get()
    email = txt_email.get()
    categoria = txt_categoria.get()

    if codigo == "" or empresa == "" or contato == "" or telefone == "" or email == "" or categoria == "":
        messagebox.showerror("Erro", "Preencha todos os campos.")
        return

    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            fornecedores = json.load(f)
    else:
        fornecedores = []

    fornecedor = {
        "codigo": codigo,
        "empresa": empresa,
        "contato": contato,
        "telefone": telefone,
        "email": email,
        "categoria": categoria
    }

    fornecedores.append(fornecedor)

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(fornecedores, f, indent=4, ensure_ascii=False)

    messagebox.showinfo("Sucesso", "Fornecedor cadastrado com sucesso!")

    txt_codigo.delete(0, tk.END)
    txt_empresa.delete(0, tk.END)
    txt_contato.delete(0, tk.END)
    txt_telefone.delete(0, tk.END)
    txt_email.delete(0, tk.END)
    txt_categoria.current(0)


def abrir_fornecedores():
    global txt_codigo
    global txt_empresa
    global txt_contato
    global txt_telefone
    global txt_email
    global txt_categoria

    janela = tk.Tk()
    janela.title("Sistema - Cadastro de fornecedores")
    janela.geometry("980x790")
    janela.configure(bg="#1E293B")

    titulo = tk.Label(
        janela,
        text="Cadastro de Fornecedores",
        font=("Arial", 18, "bold"),
        bg="#1E293B",
        fg="#E2E8F0"
    )
    titulo.pack(pady=15)

    tk.Label(janela, text="Código", bg="#1E293B", fg="#E2E8F0").pack()
    txt_codigo = tk.Entry(janela, width=40)
    txt_codigo.pack(pady=5)

    tk.Label(janela, text="Empresa", bg="#1E293B", fg="#E2E8F0").pack()
    txt_empresa = tk.Entry(janela, width=40)
    txt_empresa.pack(pady=5)

    tk.Label(janela, text="Contato", bg="#1E293B", fg="#E2E8F0").pack()
    txt_contato = tk.Entry(janela, width=40)
    txt_contato.pack(pady=5)

    tk.Label(janela, text="Telefone", bg="#1E293B", fg="#E2E8F0").pack()
    txt_telefone = tk.Entry(janela, width=40)
    txt_telefone.pack(pady=5)

    tk.Label(janela, text="E-mail", bg="#1E293B", fg="#E2E8F0").pack()
    txt_email = tk.Entry(janela, width=40)
    txt_email.pack(pady=5)

    tk.Label(janela, text="Categoria", bg="#1E293B", fg="#E2E8F0").pack()

    categorias = [
        "Peças Automotivas",
        "Lubrificantes",
        "Pneus",
        "Ferramentas",
        "Elétrica",
        "Suspensão",
        "Freios",
        "Motor",
        "Acessórios",
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

    botao = tk.Button(
        janela,
        text="Cadastrar Fornecedor",
        command=salvar_fornecedor,
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