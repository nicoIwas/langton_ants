# Começando com langton_ants

Este projeto foi desenvolvido por mim para uma disciplina do programa de mestrado. 

---

Para rodar o código, você precisa ter o Python instalado. Esta versão específica foi desenvolvida no [Python 3.13.7](https://www.python.org/downloads/release/python-3137/), mas honestamente deve rodar em versões inferiores (e, por enquanto, superiores) do Python.

## Primeiros passos

Para este passo a passo eu vou usar exemplos no Windows, já que é o sistema operacional no qual a aplicação foi desenvolvida. Para usuários de outros sistemas, sinta-se à vontade para me contatar em caso de qualquer problema (mesmo que eu não ache que eles devam acontecer). Para usuários do Windows, eu vou rodar comandos no terminal bash, mas deve funcionar normalmente no prompt de comando!

Primeiro, crie seu ambiente virtual. No Windows, deve funcionar digitando o seguinte comando no terminal bash:

```shell
py -m venv .venv
```

Para ativá-lo, caso sua IDE ainda não o tenha localizado como seu ambiente Python, rode no terminal bash:

```bash
source .venv/Scripts/activate 
```

Por fim, você precisa instalar as dependências necessárias. Rode no terminal bash:

```bash
pip install -r requirements.txt
```

Isso instalará as bibliotecas Python na versão correta.

## Rodando o código

O código é, por enquanto, muito simples, mesmo que deva receber algumas atualizações no futuro. Ele simula o autômato celular da formiga de Langton, rodando em uma matriz definida por você. Ele possui uma propriedade de "world wrapping" (se a malha termina, a formiga aparece diretamente no lado oposto) e simula a formiga básica proposta por Christopher Langton.

Após a simulação rodar por um tempo, você pode notar alguns comportamentos emergentes sendo exibidos pela formiga. Alterar o comportamento da formiga pode mostrar comportamentos inesperados.

Para rodar o código, basta digitar no terminal bash:

```shell
python src/main.py
```

E isso rodará a simulação usando as configurações padrão. O arquivo `main.py` contém as seguintes informações (importantes):

```py
if __name__ == "__main__":

    ant = Ant((125, 125))
    anthill = Map(ant, 250, 250)
    anthill.simulate(steps=500, debug=True)
```

Este é o código que simula a formiga. Se você quiser alterar a configuração inicial, entenda o seguinte:

```py
def __init__(self, starting_position: tuple[int, int] = (0, 0), starting_direction: Literal["r", "l", "u", "d"] = "r", current_square: int = 0):

    self.position = starting_position
    self.direction = starting_direction
    self.current_square = current_square
```

A formiga possui alguns atributos que influenciam seu comportamento. Para cada atributo, existem algumas condições.

* Atributos da Ant:

  1. `self.position`: Position é a posição inicial da formiga. É uma tupla de inteiros e determinará onde a formiga começa na simulação. Mesmo que pareça óbvio, é importante saber que a posição inicial deve estar dentro do intervalo de índices da malha (anthill). A tupla de posição inicial (eixo x e y) não deve ultrapassar as dimensões do anthill (lembre-se que isso funciona como uma lista Python, então o valor máximo para x e y é o valor de x e y do Map menos um).
  2. `self.direction`: É importante saber que o movimento da formiga depende da direção para a qual ela está olhando. Mover para "esquerda" ou "direita" depende da perspectiva da formiga. Este argumento altera a direção inicial da perspectiva da formiga em sua posição inicial. Para maior clareza, ele deve assumir um dos seguintes valores: `["r", "l", "u", "d"]`. Para cada um deles:

     * `"r"` significa **DIREITA**;
     * `"l"` significa **ESQUERDA**;
     * `"u"` significa **CIMA**;
     * `"d"` significa **BAIXO**.
  3. `self.current_square`: Este atributo é a leitura da formiga para o quadrado atual em que ela está. Se você escolher (por algum motivo) começar com uma malha que não é completamente preta, este argumento pode ter algum uso, mas não deve ser usado. Em futuras implementações, ele será removido como parâmetro do construtor.

A variável anthill é a grade onde o código roda. Se você quiser alterar a configuração inicial, entenda o seguinte:

```py
def __init__(self, ant: Ant, rows: int = 500, columns: int = 500):

    self.anthill = np.zeros((rows, columns))
    self.ant = ant
```

* Atributos do Anthill:

  1. Argumentos (rows, columns): definem o número de linhas e colunas presentes na malha. Eles definem o tamanho do "mundo". Como dito antes, o número de linhas deve ser maior que a posição inicial da formiga no eixo x; o número de colunas deve ser maior que a posição inicial no eixo y.
  2. `self.anthill`: Com base no número de linhas e colunas, uma matriz de zeros será inicializada, com dimensões baseadas nos argumentos anteriores.
  3. `self.ant`: Este argumento corresponde à formiga criada anteriormente.

Por fim, a função `anthill.simulate([...])` é responsável por rodar e renderizar a matriz. Ela usa a função `matshow` do matplotlib para renderizar o gráfico na tela. Ela recebe dois argumentos:

```py
def simulate(self, steps: int = 1, debug: bool = False) -> None:
```

* Argumentos do método simulate:

  1. `steps`: Basicamente, determina quantos passos serão "pulados" a cada iteração. Para uma visualização suave e relativamente rápida, eu sugiro usar o valor dado: 125 passos. Para visualização inicial e entendimento do que está acontecendo, sugiro começar com uma velocidade menor.
  2. `debug`: Isso existe para fins de depuração. É um booleano que determina se o passo atual será exibido. Existe apenas para debug e não é muito útil; sinta-se à vontade para deixá-lo desligado, já que pode travar a visualização.

Com isso em mente, você já consegue ver o código funcionando. Digite o comando mencionado anteriormente no terminal bash e você deve ver algo assim:

![](imgs/grid.png)

## Encerrando a simulação

Se (quando) você quiser encerrar o programa rodando, pode achar um pouco complicado. Primeiro, apenas feche a grade renderizada. No terminal bash, pressione `CTRL + C` e ele encerrará suavemente.

## Por fim

Obrigado por ler até aqui! Sinta-se à vontade para me contatar por qualquer uma das minhas redes (você pode vê-las na página inicial do meu perfil no GitHub) caso tenha interesse em algum aspecto do projeto ou qualquer tipo de sugestão. Divirta-se simulando formigas!
