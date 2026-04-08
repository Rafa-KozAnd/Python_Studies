import tkinter as tk
from tkinter import messagebox
import random

class JogoDeAdivinhacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Adivinhação")

        self.numero_secreto = random.randint(1, 100)
        self.tentativas_restantes = 10

        self.label_instrucao = tk.Label(root, text="Adivinhe um número entre 1 e 100:", font=('Arial', 14))
        self.label_instrucao.pack(pady=10)

        self.entry_numero = tk.Entry(root, font=('Arial', 14))
        self.entry_numero.pack(pady=5)

        self.btn_adivinhar = tk.Button(root, text="Adivinhar", command=self.verificar_palpite, font=('Arial', 14))
        self.btn_adivinhar.pack(pady=5)

    def verificar_palpite(self):
        palpite = self.entry_numero.get()

        try:
            palpite = int(palpite)
            if 1 <= palpite <= 100:
                self.tentativas_restantes -= 1
                if palpite == self.numero_secreto:
                    messagebox.showinfo("Parabéns!", f"Você acertou! O número secreto era {self.numero_secreto}.")
                    self.resetar_jogo()
                elif palpite < self.numero_secreto:
                    messagebox.showinfo("Tente Novamente", "Tente um número maior.")
                else:
                    messagebox.showinfo("Tente Novamente", "Tente um número menor.")
                if self.tentativas_restantes == 0:
                    messagebox.showinfo("Fim de Jogo", f"Você perdeu! O número secreto era {self.numero_secreto}.")
                    self.resetar_jogo()
            else:
                messagebox.showwarning("Atenção", "Por favor, insira um número entre 1 e 100.")
        except ValueError:
            messagebox.showwarning("Atenção", "Por favor, insira um número válido.")

    def resetar_jogo(self):
        self.numero_secreto = random.randint(1, 100)
        self.tentativas_restantes = 10
        self.entry_numero.delete(0, tk.END)

def main():
    root = tk.Tk()
    jogo = JogoDeAdivinhacao(root)
    root.mainloop()

if __name__ == "__main__":
    main()
