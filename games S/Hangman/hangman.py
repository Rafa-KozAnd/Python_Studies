import tkinter as tk
from tkinter import messagebox
import random

class JogoDaForca:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")

        self.palavras = ['python', 'java', 'ruby', 'javascript', 'html', 'css']
        self.palavra_secreta = random.choice(self.palavras)
        self.letras_descobertas = ['_' for _ in self.palavra_secreta]

        self.tentativas_restantes = 6

        self.letras_label = tk.Label(root, text=' '.join(self.letras_descobertas), font=('Arial', 24))
        self.letras_label.pack(pady=10)

        self.letra_entry = tk.Entry(root, font=('Arial', 18))
        self.letra_entry.pack(pady=10)

        self.tentativas_label = tk.Label(root, text=f'Tentativas Restantes: {self.tentativas_restantes}', font=('Arial', 18))
        self.tentativas_label.pack(pady=10)

        self.submeter_btn = tk.Button(root, text='Submeter', command=self.verificar_letra, font=('Arial', 18))
        self.submeter_btn.pack(pady=10)

    def verificar_letra(self):
        letra = self.letra_entry.get().lower()
        self.letra_entry.delete(0, tk.END)

        if len(letra) != 1 or not letra.isalpha():
            messagebox.showwarning("Atenção", "Por favor, insira apenas uma letra válida.")
            return

        if letra in self.palavra_secreta:
            for i in range(len(self.palavra_secreta)):
                if self.palavra_secreta[i] == letra:
                    self.letras_descobertas[i] = letra
            self.letras_label.config(text=' '.join(self.letras_descobertas))
        else:
            self.tentativas_restantes -= 1
            self.tentativas_label.config(text=f'Tentativas Restantes: {self.tentativas_restantes}')
            if self.tentativas_restantes == 0:
                messagebox.showinfo("Fim de Jogo", f"Você perdeu! A palavra secreta era '{self.palavra_secreta}'.")
                self.root.quit()

        if '_' not in self.letras_descobertas:
            messagebox.showinfo("Parabéns", "Você ganhou! Você descobriu a palavra secreta.")
            self.root.quit()

def main():
    root = tk.Tk()
    jogo = JogoDaForca(root)
    root.mainloop()

if __name__ == "__main__":
    main()
