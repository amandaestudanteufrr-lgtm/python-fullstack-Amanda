#=============================================================================
# ITEAM | Projeto: Salão de Beleza & Barbearia
# Módulo : salao.modelos.pessoa
# Assunto: Classes, Atributos, Encapsulamento e @property  (Seção 5.2 e 5.3.1)
#=============================================================================

class Pessoa:
    """
    Classe BASE que representa qualquer pessoa do salão.
    Demonstra encapsulamento com atributos privados e @property.
    """

    def __init__(self, nome: str, cpf: str, telefone: str):
        # Correção do BUG 1: alterado para atributos privados (__nome e __cpf)
        self.__nome     = nome.strip().title()   
        self.__cpf      = cpf.strip()
        self.telefone = telefone.strip()

    # --- getters (leitura controlada) ---

    @property
    def nome(self):
        # Correção do BUG 2: retorna o atributo privado __nome em vez de self.nome (evita recursão)
        return self.__nome   

    @property
    def cpf(self):
        return self.__cpf

    # --- setter com validação ---

    @nome.setter
    def nome(self, valor: str):
        if not valor.strip():
            raise ValueError("O nome não pode ser vazio.")
        self.__nome = valor.strip().title()

    # --- representação ---

    def __str__(self):
        return f"Pessoa: {self.nome} | CPF: {self.cpf} | Tel: {self.telefone}"

    def __repr__(self):
        return f"Pessoa(nome='{self.nome}', cpf='{self.cpf}')"
    