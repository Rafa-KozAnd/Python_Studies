import tkinter as tk
from tkinter import messagebox

class ListaTarefas:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")

        self.tarefas = []

        self.label_tarefa = tk.Label(root, text="Tarefa:", font=('Arial', 14))
        self.label_tarefa.grid(row=0, column=0, padx=5, pady=5)
        self.entry_tarefa = tk.Entry(root, font=('Arial', 14))
        self.entry_tarefa.grid(row=0, column=1, padx=5, pady=5)

        self.btn_adicionar = tk.Button(root, text="Adicionar Tarefa", command=self.adicionar_tarefa, font=('Arial', 14))
        self.btn_adicionar.grid(row=0, column=2, padx=5, pady=5)

        self.lista_tarefas = tk.Listbox(root, font=('Arial', 12), width=40, height=10)
        self.lista_tarefas.grid(row=1, columnspan=3, padx=5, pady=5)

        self.btn_remover = tk.Button(root, text="Remover Tarefa", command=self.remover_tarefa, font=('Arial', 14))
        self.btn_remover.grid(row=2, columnspan=3, padx=5, pady=5)

    def adicionar_tarefa(self):
        tarefa = self.entry_tarefa.get()
        if tarefa:
            self.tarefas.append(tarefa)
            self.atualizar_lista_tarefas()
            self.entry_tarefa.delete(0, tk.END)
        else:
            messagebox.showwarning("Atenção", "Por favor, insira uma tarefa.")

    def remover_tarefa(self):
        indice = self.lista_tarefas.curselection()
        if indice:
            self.tarefas.pop(indice[0])
            self.atualizar_lista_tarefas()
        else:
            messagebox.showwarning("Atenção", "Por favor, selecione uma tarefa para remover.")

    def atualizar_lista_tarefas(self):
        self.lista_tarefas.delete(0, tk.END)
        for tarefa in self.tarefas:
            self.lista_tarefas.insert(tk.END, tarefa)

def main():
    root = tk.Tk()
    app = ListaTarefas(root)
    root.mainloop()

if __name__ == "__main__":
    main()
