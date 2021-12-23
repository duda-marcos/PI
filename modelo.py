from ast import Num
from config import *

# Classe pai para funcionário e cidadão
class Comentario(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(200))
    Email = db.Column(db.String(100))
    Telefone = db.Column(db.String(100))
    Descricao = db.Column(db.String(300))
    def __str__(self):
        return f'{self.Id}, {self.Nome}, {self.Email}, {self.Telefone}, {self.Descricao}'
    
    def json(self):
        return {
            "Id": self.Id,
            "Nome": self.Nome,
            "Email": self.Email,
            "Telefone": self.Telefone,
            "Descricao": self.Descricao
            }

class Roupa(db.Model):
    Id = db.Column(db.Integer, primary_key=True)
    Descricao = db.Column(db.String(200))
    Preco = db.Column(db.Float())
    Tipo = db.Column(db.String(100))
    Imagem = db.Column(db.String(20))
    def __str__(self):
        return f'{self.Id}, {self.Descricao}, {str(self.Preco)}, {self.Tipo}, {self.Imagem}'
    
    def json(self):
        return {
            "Id": self.Id,
            "Descricao": self.Descricao,
            "Preco": self.Preco,
            "Tipo": self.Tipo,
            "Imagem": self.Imagem
            }


# Bloqueia as seguintes funções quando importado
if __name__ == "__main__":
    
    # Apaga arquivos já existentes para que não tenha repetição de dados
    if os.path.exists(arquivobd):
        os.remove(arquivobd)
    
    db.create_all() # Cria as tabelas do banco de dados

    # Inputs de informações
    comentario1 = Comentario(Nome = "Raissa Gatinha", Email = "raissa@gmail.com", Telefone = "4002-8922", Descricao = "Site muito bonito")
    comentario2 = Comentario(Nome = "Duda", Email = "duda@gmail.com", Telefone = "4002-8922", Descricao = "Site bonito")
    comentario3 = Comentario(Nome = "Marcelo Vicente", Email = "marcelo@gmail.com", Telefone = "4002-8922", Descricao = "Site mediano")
    
    roupa1 = Roupa(Descricao = "Short verde", Preco = 50.30, Tipo = "Roupa de Verão", Imagem = "img/RoupasVenda/1.png")
    roupa2 = Roupa(Descricao = "Vestido Preto", Preco = 40.30, Tipo = "Roupa de Festa", Imagem = "img/RoupasVenda/2.png")
    roupa3 = Roupa(Descricao = "Biquíni", Preco = 10.30, Tipo = "Conjunto", Imagem = "img/RoupasVenda/3.png")

    db.session.add(comentario1)
    db.session.add(comentario2)
    db.session.add(comentario3)
    db.session.add(roupa1)
    db.session.add(roupa2)
    db.session.add(roupa3)
    db.session.commit() # Grava os dados no banco de dados

    TodosComentarios = db.session.query(Comentario).all() # Traz os dados do banco para uma lista 
    # Imprime as informações
    print("")
    for i in TodosComentarios:
        print(i)
        print(i.json())
        print("")

    TodasRoupas = db.session.query(Roupa).all() # Traz os dados do banco para uma lista 
    # Imprime as informações
    print("")
    for i in TodasRoupas:
        print(i)
        print(i.json())
        print("")