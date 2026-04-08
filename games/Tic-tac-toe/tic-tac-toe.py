import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")

        self.turno = 'X'
        self.tabuleiro = [['' for _ in range(3)] for _ in range(3)]

        self.botoes = [[None for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.botoes[i][j] = tk.Button(root, text='', font=('Arial', 24), width=5, height=2,
                                              command=lambda row=i, col=j: self.clicar(row, col))
                self.botoes[i][j].grid(row=i, column=j)

    def clicar(self, row, col):
        if self.tabuleiro[row][col] == '':
            self.tabuleiro[row][col] = self.turno
            self.botoes[row][col].config(text=self.turno)
            
            if self.verificar_vitoria(self.turno):
                messagebox.showinfo("Parabéns!", f"O jogador {self.turno} venceu!")
                self.resetar_jogo()
            elif self.verificar_empate():
                messagebox.showinfo("Empate!", "O jogo terminou em empate!")
                self.resetar_jogo()
            else:
                self.turno = 'O' if self.turno == 'X' else 'X'

    def verificar_vitoria(self, jogador):
        for i in range(3):
            if self.tabuleiro[i][0] == self.tabuleiro[i][1] == self.tabuleiro[i][2] == jogador:
                return True
            if self.tabuleiro[0][i] == self.tabuleiro[1][i] == self.tabuleiro[2][i] == jogador:
                return True
        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == jogador:
            return True
        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] == jogador:
            return True
        return False

    def verificar_empate(self):
        for i in range(3):
            for j in range(3):
                if self.tabuleiro[i][j] == '':
                    return False
        return True

    def resetar_jogo(self):
        for i in range(3):
            for j in range(3):
                self.tabuleiro[i][j] = ''
                self.botoes[i][j].config(text='')
        self.turno = 'X'

def main():
    root = tk.Tk()
    jogo = JogoDaVelha(root)
    root.mainloop()

if __name__ == "__main__":
    main()
