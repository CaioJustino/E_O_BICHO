import datetime as dt 
import random as rd

class BancoDeDados():
  def __init__(self):
    self.__bd_animais={}
    self.__bd_pessoas={}

  def add_pessoa(self, pessoa):
    if pessoa.cpf in self.__bd_pessoas:
      return None
    self.__bd_pessoas[pessoa.cpf]=pessoa

  def listar_pessoas(self, cpf=None):
    if cpf != None:
      return self.__bd_pessoas[cpf]
    return self.__bd_pessoas

  def add_animal(self, animal):
    if animal._animal_id in self.__bd_animais:
      return None
    self.__bd_animais[animal._animal_id]=animal

  def listar_animais(self, id=None):
    if id != None:
      return self.__bd_animais[id]
    return self.__bd_animais

class ValidarCPF():
  def __init__(self, cpf):
    self.__cpf=cpf

  lista = [i for i in range(10)]

  def validarCpf(self):
    cpf = [int(char) for char in self.__cpf if char.isdigit()]

    if len(cpf) != 11:
        return ''

    if cpf == cpf[::-1]:
        return ''

    for i in range(9, 11):
        value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
        digit = ((value * 10) % 11) % 10
        if digit != cpf[i]:
            return ''
    return self.__cpf  

class Pessoa():
  def __init__(self, nome, sexo, idade, cpf, numero_telefone, email):
    self._nome=nome
    self._sexo=sexo
    self._idade=idade
    self.__cpf=ValidarCPF(cpf).validarCpf() 
    self._voluntario=False
    self._numero_telefone=numero_telefone
    self._email=email
    self.__endereco=[]

  @property
  def cpf(self):
    return self.__cpf

  @cpf.setter
  def cpf(self, v):
    self.__cpf=v
    
  def cadastrar_end(self, rua, numero, bairro, cidade):
    self.__endereco.append(Endereco(rua, numero, bairro, cidade))

  def editarEnd(self, new_rua, new_numero, new_bairro, new_cidade):
    self.__endereco.pop()
    self.__endereco.append(Endereco(new_rua, new_numero, new_bairro, new_cidade))

  def evoluntario(self):
    if not self._voluntario:
      self._voluntario=True
      return 
    self._voluntario=False
    return
  
  def info_Pessoa(self):
    return vars(self)

class Adotante(Pessoa):
  def __init__(self, nome, sexo, idade, cpf, numero_telefone, email):
    Pessoa.__init__(self, nome, sexo, idade, cpf, numero_telefone, email)
    self.__animais_adotados=[]

  def adotar(self, id, adocao):
    self.__animais_adotados.append(adocao.buscarAnimais(id))
    animal = adocao.buscarAnimais(id)
    animal.adotado=True
    adocao.removerAnimal(id)
    
  def buscar(self, id):
    for c in self.__animais_adotados:
      if c._animal_id == id:
        return c
    return None

class Endereco():
  def __init__(self, rua, numero, bairro, cidade):
    self.rua=rua
    self.numero=numero
    self.bairro=bairro
    self.cidade=cidade

  def info_Endereco(self):
    return vars(self)

class ONG():
  def __init__(self, nome, telefone, email):
    self._nome = nome
    self._telefone = telefone
    self._email = email
    self.__enderecos = []
  
  def editarONG(self, nome_edit=None, telefone_edit=None, email_edit=None):
    if nome_edit != None:
      self._nome = nome_edit
    if telefone_edit != None:
      self._telefone = telefone_edit
    if email_edit != None:
      self._email = email_edit

  def cadastrar_end(self, rua, numero, bairro, cidade):
    self.__enderecos.append(Endereco(rua, numero, bairro, cidade))

  def editarEnd(self, new_rua, new_numero, new_bairro, new_cidade):
    self.__enderecos.pop()
    self.__enderecos.append(Endereco(new_rua, new_numero, new_bairro, new_cidade))

  def infONG(self):
    return vars(self)

class Adocao():
  def __init__(self):
    self._animaisEmAdocao=[]

  def cadastrarAnimal(self, animal):
    self._animaisEmAdocao.append(animal)

  def listarAnimais(self):
    if len(self._animaisEmAdocao) != 0:
      return self._animaisEmAdocao
    else:
      return None

  def buscarAnimais(self, id):
    for c in self._animaisEmAdocao:
      if c._animal_id == id:
        return c
    return None

  def removerAnimal(self, id):
    for c in self._animaisEmAdocao:
      i = self._animaisEmAdocao.index(c)
      if c._animal_id == id:
        self._animaisEmAdocao.pop(i)
    return None

class Vacinar():
  def __init__(self, animal):
    self._data_de_vacinacao=dt.date.today()
    self._animal=animal

  def aplicarVacinasMultiplas(self):
    if self._animal._carteira_de_vacina.vacinas_multiplas == True:
      return None
    else:
      self._animal._carteira_de_vacina.vacinas_multiplas = True
      return
  
  def aplicarAntirrabica(self):
    if self._animal._carteira_de_vacina.antirrabica == True:
      return None
    else:
      self._animal._carteira_de_vacina.antirrabica = True
      return

class Animal():
  def __init__(self, nome, sexo, idade, peso, especie, raca):
    self._nome = nome
    self._sexo = sexo
    self._idade = idade
    self._peso = peso
    self._especie = especie
    self._raca = raca
    self._dia_que_chegou = dt.date.today()
    self._deficiencia = Deficiencia()
    self._carteira_de_vacina = CarteiraDeVacina()
    self.adotado = False
    self._animal_id = float('{:.4f}'.format(rd.uniform(1.0, 9.0)))

  def editar_animal(self, nome_edit=None, sexo_edit=None, idade_edit=None, peso_edit=None, especie_edit=None, raca_edit=None):
    if nome_edit != None:
      self._nome = nome_edit
    if sexo_edit != None:
      self._sexo = sexo_edit
    if idade_edit != None:
      self._idade = idade_edit
    if peso_edit != None:
      self._peso = peso_edit
    if especie_edit != None:
      self._especie = especie_edit
    if raca_edit != None:
      self._raca = raca_edit
    return
    
  def info_animal(self):
    return vars(self)

class Deficiencia():
  def __init__(self):
    self.__fisica=False
    self.__visual=False
    self.__auditiva=False
    self.__cognitiva=False
    self._deficiencias={'Física': '', 'Visual': '', 'Auditiva': '', 'Cognitiva': ''}

  def infoDef(self):
    return vars(self)

  def definir_deficiencia(self, tipo_def):
    if tipo_def.upper() == "F":
      new_def = input("Digite o nome da deficiência física: ")
      if new_def in self._deficiencias.values():
        return None
      else:
        self._deficiencias.update({'Física': new_def})
        self.__fisica = True
        return
    if tipo_def.upper() == "V":
      new_def = input("Digite o nome da deficiência visual: ")
      if new_def in self._deficiencias.values():
        return None
      else:
        self._deficiencias.update({'Visual': new_def})
        self.__visual = True
        return
    if tipo_def.upper() == "A":
      new_def = input("Digite o nome da deficiência auditiva: ")
      if new_def in self._deficiencias.values():
        return None
      else:
        self._deficiencias.update({'Auditiva': new_def})
        self.__auditiva = True
        return
    if tipo_def.upper() == "C":
      new_def = input("Digite o nome da deficiência cognitiva: ")
      if new_def in self._deficiencias.values():
        return None
      else:
        self._deficiencias.update({'Cognitiva': new_def})
        self.__cognitiva = True
        return
    return None

  def buscar_deficiencia(self, sdef):
    if sdef in self._deficiencias.values():
      return sdef
    else:
      return None

class CarteiraDeVacina():
  def __init__(self):
    self.__vacinas_multiplas=False
    self.__antirrabica=False 

  @property
  def vacinas_multiplas(self):
    return self.__vacinas_multiplas

  @vacinas_multiplas.setter
  def vacinas_multiplas(self, v):
    self.__vacinas_multiplas = v

  @property
  def antirrabica(self):
    return self.__antirrabica

  @antirrabica.setter
  def antirrabica(self, v):
    self.__antirrabica = v
