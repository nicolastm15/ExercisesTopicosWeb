#conectar com GDrive para usar os dados do twitter que serão usados na disciplina
#conectar a base de dados
#processar o arquivos json e acessar o campo de texto de cada tweet
#transformar todo texto para minúsculo
#remover pontuação e caracteres especiais
#tokenização
#remover stopwords (busque uma lista para o português brasileiro, importe da sua máquina para o colab)
#remover termos sem sentido (ex: rt, remover links inteiros, citacao - tem que ser feito antes da expressao regular).
#stemming
#lemmastization
#bag of words

#mais dicas: veja o nltk e o spaCy


#o import abaixo nao funciona fora do python notebook do google (Google Colab)
from google.colab import drive
import json
import re
import configparser

config = configparser.ConfigParser()
config.read("./config.ini")

#Vai pedir um token de autorização para acesso ao drive. Ao rodar o comando, ele fornecerá o link para geração do token. O proprietário da conta do GDrive que se deseja acessar deve autenticar e copiar o token gerado.
drive.mount("/content/gdrive")
dataset = config.get("URL", "covid_js")
arq = open(dataset)

#opcao para abrir e iterar arquivo
#with open('/content/gdrive/My Drive/Quarentena2020/TopicosWeb/covid.json','r') as arq:
#    print(arq.readline())

#exemplo de conteúdo
#print(arq.readline())
#arq.seek(0)

for linha in arq:
  tweet = json.loads(linha.encode("utf-8"))
  text = tweet["text"]
  print(text)
  text = text.lower()

  rex = re.compile("\w+")  # "http://www.google.com"
  tokens = rex.findall(text)

  #ou linha abaixo, mas os caracteres especiais permanecerao
  #tokens = text.split()
  print(tokens)
  break  # remova esse break

conteudo = "Testando as expressoes regulares com python. O desafio consiste em remover as stop words deste texto, fazendo um script python local na maquina de voces. Depois adaptem para funcionar para os textos do tweet, observando o codigo que esta dentro do for aqui no colab."

#lista de stopwords temporaria
stopwords = ['em', 'a', 'as', 'o', 'os', 'de', 'para', 'como', 'um', 'uma', 'algum',
             'que', 'alguma', 'onde', 'aonde', 'com', 'no', 'na', 'do', 'voces', 'esta']

conteudo = conteudo.lower()

conteudo = conteudo.replace(",", "")
conteudo = conteudo.replace(".", "")

tokens = conteudo.split()

tokens_sem_stopwords = []
for i in tokens:
  if not(i in stopwords):
    tokens_sem_stopwords.append(i)

print(tokens_sem_stopwords)
