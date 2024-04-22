class Animal: ##superclasse
    def __init__(self, nome):
        self.nome = nome

    def fazer_som(self):
        pass  # Método a ser implementado pelas subclasses

class Cachorro(Animal): ##subclasse
    def fazer_som(self):
        return "Au Au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

# Criando objetos das subclasses
rex = Cachorro("Rex")
garfield = Gato("Garfield")

# Chamando o método fazer_som() em cada objeto
print(rex.nome + ": " + rex.fazer_som())  # Saída: Rex: Au Au!
print(garfield.nome + ": " + garfield.fazer_som())  # Saída: Garfield: Miau!

## Exemplo do ChatGPT