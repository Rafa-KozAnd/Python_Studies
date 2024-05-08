import tkinter as tk
import qrcode
from PIL import Image, ImageTk

class GeradorQRCode:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de QR Code")

        self.label_instrucao = tk.Label(root, text="Insira os dados para gerar o QR Code:", font=('Arial', 14))
        self.label_instrucao.pack(pady=10)

        self.entry_dados = tk.Entry(root, font=('Arial', 14), width=40)
        self.entry_dados.pack(pady=5)

        self.btn_gerar = tk.Button(root, text="Gerar QR Code", command=self.gerar_qr_code, font=('Arial', 14))
        self.btn_gerar.pack(pady=5)

        self.imagem_qr_code = tk.Label(root)
        self.imagem_qr_code.pack(pady=10)

    def gerar_qr_code(self):
        dados = self.entry_dados.get()
        if dados:
            qr_code = qrcode.make(dados)
            qr_code.save("qrcode.png")

            imagem = Image.open("qrcode.png")
            imagem = imagem.resize((200, 200), Image.ANTIALIAS)
            imagem_qr = ImageTk.PhotoImage(imagem)

            self.imagem_qr_code.config(image=imagem_qr)
            self.imagem_qr_code.image = imagem_qr
        else:
            tk.messagebox.showwarning("Atenção", "Por favor, insira os dados para gerar o QR Code.")

def main():
    root = tk.Tk()
    app = GeradorQRCode(root)
    root.mainloop()

if __name__ == "__main__":
    main()
