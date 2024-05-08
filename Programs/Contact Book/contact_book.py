import tkinter as tk
from tkinter import messagebox

class AgendaContatos:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda de Contatos")

        self.contatos = {}

        self.label_nome = tk.Label(root, text="Nome:", font=('Arial', 14))
        self.label_nome.grid(row=0, column=0, padx=5, pady=5)
        self.entry_nome = tk.Entry(root, font=('Arial', 14))
        self.entry_nome.grid(row=0, column=1, padx=5, pady=5)

        self.label_telefone = tk.Label(root, text="Telefone:", font=('Arial', 14))
        self.label_telefone.grid(row=1, column=0, padx=5, pady=5)
        self.entry_telefone = tk.Entry(root, font=('Arial', 14))
        self.entry_telefone.grid(row=1, column=1, padx=5, pady=5)

        self.btn_adicionar = tk.Button(root, text="Adicionar Contato", command=self.adicionar_contato, font=('Arial', 14))
        self.btn_adicionar.grid(row=2, columnspan=2, padx=5, pady=5)

        self.lista_contatos = tk.Listbox(root, font=('Arial', 12), width=40, height=10)
        self.lista_contatos.grid(row=3, columnspan=2, padx=5, pady=5)

    def adicionar_contato(self):
        nome = self.entry_nome.get()
        telefone = self.entry_telefone.get()

        if nome and telefone:
            self.contatos[nome] = telefone
            self.atualizar_lista_contatos()
            self.limpar_campos()
        else:
            messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")

    def atualizar_lista_contatos(self):
        self.lista_contatos.delete(0, tk.END)
        for nome, telefone in self.contatos.items():
            self.lista_contatos.insert(tk.END, f"{nome}: {telefone}")

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_telefone.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = AgendaContatos(root)
    root.mainloop()

if __name__ == "__main__":
    main()
