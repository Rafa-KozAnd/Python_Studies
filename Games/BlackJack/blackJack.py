import tkinter as tk
from tkinter import messagebox
import random

class Blackjack:
    def __init__(self, root):
        self.root = root
        self.root.title("Blackjack")

        self.baralho = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'] * 4
        random.shuffle(self.baralho)

        self.mao_jogador = []
        self.mao_dealer = []

        self.comecar_btn = tk.Button(root, text='Começar Jogo', command=self.comecar_jogo)
        self.comecar_btn.pack(pady=10)

    def comecar_jogo(self):
        self.comecar_btn.config(state=tk.DISABLED)

        self.mao_jogador = [self.pegar_carta(), self.pegar_carta()]
        self.mao_dealer = [self.pegar_carta(), self.pegar_carta()]

        self.mostrar_cartas()

        self.btn_outra_carta = tk.Button(self.root, text="Outra Carta", command=self.outra_carta)
        self.btn_outra_carta.pack(pady=10)

        self.btn_parar = tk.Button(self.root, text="Parar", command=self.parar)
        self.btn_parar.pack(pady=10)

    def pegar_carta(self):
        return self.baralho.pop()

    def mostrar_cartas(self):
        messagebox.showinfo("Mão do Dealer", f"A carta do dealer é: {self.mao_dealer[0]}\n\n"
                                             f"Sua mão é: {', '.join(self.mao_jogador)}")

    def calcular_valor(self, mao):
        valor = 0
        ases = 0
        for carta in mao:
            if carta.isdigit():
                valor += int(carta)
            elif carta in ['J', 'Q', 'K']:
                valor += 10
            elif carta == 'A':
                ases += 1
                valor += 11
        while valor > 21 and ases:
            valor -= 10
            ases -= 1
        return valor

    def outra_carta(self):
        self.mao_jogador.append(self.pegar_carta())
        valor_jogador = self.calcular_valor(self.mao_jogador)
        if valor_jogador > 21:
            messagebox.showinfo("Resultado", f"Você estourou! Sua mão: {', '.join(self.mao_jogador)}\n\n"
                                             f"Dealer's hand: {', '.join(self.mao_dealer)}")
            self.resetar_jogo()
        elif valor_jogador == 21:
            messagebox.showinfo("Resultado", f"Blackjack! Você venceu!\n\n"
                                             f"Sua mão: {', '.join(self.mao_jogador)}\n\n"
                                             f"Dealer's mão: {', '.join(self.mao_dealer)}")
            self.resetar_jogo()

    def parar(self):
        while self.calcular_valor(self.mao_dealer) < 17:
            self.mao_dealer.append(self.pegar_carta())

        valor_jogador = self.calcular_valor(self.mao_jogador)
        valor_dealer = self.calcular_valor(self.mao_dealer)

        if valor_dealer > 21 or valor_jogador > valor_dealer:
            messagebox.showinfo("Resultado", f"Você venceu!\n\n"
                                             f"Sua mão: {', '.join(self.mao_jogador)}\n\n"
                                             f"Dealer's mão: {', '.join(self.mao_dealer)}")
        elif valor_jogador == valor_dealer:
            messagebox.showinfo("Resultado", "Empate!")
        else:
            messagebox.showinfo("Resultado", f"Você perdeu!\n\n"
                                             f"Sua mão: {', '.join(self.mao_jogador)}\n\n"
                                             f"Dealer's mão: {', '.join(self.mao_dealer)}")
        self.resetar_jogo()

    def resetar_jogo(self):
        self.comecar_btn.config(state=tk.NORMAL)
        self.btn_outra_carta.pack_forget()
        self.btn_parar.pack_forget()
        self.mao_jogador = []
        self.mao_dealer = []

def main():
    root = tk.Tk()
    jogo = Blackjack(root)
    root.mainloop()

if __name__ == "__main__":
    main()
