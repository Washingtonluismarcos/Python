import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import pickle

class CadastroVeiculosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cadastro de Veículos")

        self.veiculos = self.carregar_veiculos()

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.botao_cadastrar = tk.Button(self.frame, text="Cadastrar Veículo", command=self.cadastrar_veiculo)
        self.botao_cadastrar.grid(row=0, column=0, padx=5, pady=5)

        self.botao_exibir = tk.Button(self.frame, text="Exibir Veículos", command=self.exibir_veiculos)
        self.botao_exibir.grid(row=0, column=1, padx=5, pady=5)

        self.botao_excluir = tk.Button(self.frame, text="Excluir Veículo", command=self.excluir_veiculo)
        self.botao_excluir.grid(row=0, column=2, padx=5, pady=5)

        self.botao_pesquisar = tk.Button(self.frame, text="Pesquisar Proprietário", command=self.pesquisar_veiculos)
        self.botao_pesquisar.grid(row=0, column=3, padx=5, pady=5)

        self.botao_sair = tk.Button(self.frame, text="Sair", command=self.sair)
        self.botao_sair.grid(row=0, column=4, padx=5, pady=5)

    def carregar_veiculos(self):
        try:
            with open('dados_veiculos.pkl', 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    def salvar_veiculos(self):
        with open('dados_veiculos.pkl', 'wb') as f:
            pickle.dump(self.veiculos, f)

    def cadastrar_veiculo(self):
        novo_veiculo = {}
        novo_veiculo['proprietario'] = self.obter_input("Nome do Proprietário:")
        novo_veiculo['modelo'] = self.obter_input("Modelo do Veículo:")
        novo_veiculo['chassi'] = self.obter_input("Número do Chassi:")
        novo_veiculo['ano_fabricacao'] = self.obter_input("Ano de Fabricação:")
        novo_veiculo['placa'] = self.obter_input("Placa do Veículo:")

        self.veiculos.append(novo_veiculo)
        self.salvar_veiculos()
        messagebox.showinfo("Cadastro", "Veículo cadastrado com sucesso!")

    def exibir_veiculos(self):
        if self.veiculos:
            lista_veiculos = "\n".join([str(veiculo) for veiculo in self.veiculos])
            messagebox.showinfo("Veículos Cadastrados", lista_veiculos)
        else:
            messagebox.showinfo("Veículos Cadastrados", "Não há veículos cadastrados.")

    def excluir_veiculo(self):
        if not self.veiculos:
            messagebox.showinfo("Excluir Veículo", "Não há veículos para excluir.")
            return

        escolha = self.obter_input("Digite o índice do veículo a ser excluído:")
        try:
            indice = int(escolha) - 1
            if 0 <= indice < len(self.veiculos):
                veiculo_excluido = self.veiculos.pop(indice)
                self.salvar_veiculos()
                messagebox.showinfo("Excluir Veículo", f"Veículo excluído: {veiculo_excluido}")
            else:
                messagebox.showinfo("Excluir Veículo", "Índice inválido.")
        except ValueError:
            messagebox.showinfo("Excluir Veículo", "Entrada inválida. Digite um número.")

    def pesquisar_veiculos(self):
        termo_pesquisa = self.obter_input("Digite parte do nome do proprietário para pesquisar:")
        resultados = [veiculo for veiculo in self.veiculos if termo_pesquisa.lower() in veiculo['proprietario'].lower()]

        if resultados:
            lista_resultados = "\n".join([str(veiculo) for veiculo in resultados])
            messagebox.showinfo("Resultados da Pesquisa", lista_resultados)
        else:
            messagebox.showinfo("Resultados da Pesquisa", "Nenhum resultado encontrado.")

    def obter_input(self, mensagem):
        return simpledialog.askstring("Input", mensagem)

    def sair(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroVeiculosApp(root)
    root.mainloop()
