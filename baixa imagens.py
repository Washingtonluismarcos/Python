import os
import requests
from tkinter import Tk, Label, Button, Entry, filedialog, messagebox

class ImageDownloaderApp:
    def __init__(self, master):
        self.master = master
        master.title("Google Image Downloader")

        self.label = Label(master, text="URL da Imagem:")
        self.label.pack()

        self.url_entry = Entry(master, width=50)
        self.url_entry.pack()

        self.browse_button = Button(master, text="Escolher Diretório", command=self.choose_directory)
        self.browse_button.pack()

        self.download_button = Button(master, text="Baixar Imagem", command=self.download_image)
        self.download_button.pack()

        self.destination_folder = ""

    def choose_directory(self):
        self.destination_folder = filedialog.askdirectory()
        if self.destination_folder:
            messagebox.showinfo("Sucesso", f"Diretório escolhido: {self.destination_folder}")

    def download_image(self):
        url = self.url_entry.get()

        if url and self.destination_folder:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    file_name = os.path.join(self.destination_folder, os.path.basename(url))
                    with open(file_name, 'wb') as file:
                        file.write(response.content)
                    messagebox.showinfo("Sucesso", f"Imagem baixada com sucesso: {file_name}")
                else:
                    messagebox.showerror("Erro", f"Falha ao baixar a imagem. Código de status: {response.status_code}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro durante o download da imagem: {e}")
        else:
            messagebox.showwarning("Aviso", "Por favor, insira um URL válido e escolha um diretório de destino.")

if __name__ == "__main__":
    root = Tk()
    app = ImageDownloaderApp(root)
    root.mainloop()


