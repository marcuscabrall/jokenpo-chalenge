# Desafio Numen - Jokenpô

## Escolha da linguagem:
A linguagem escolhida foi Python, devido à familiaridade que possuo
e pelo interesse recente em aprimorar conhecimentos em testes -
atualmente objeto de meus estudos,
utilizando a biblioteca pytest (também como um desafio pessoal).

## Projeto:
Para rodar o projeto, é necessário instalar algumas bibliotecas.
O projeto já conta com um arquivo requirements.txt, o que facilita
a instalação. Basta executar o seguinte comando:
`pip install -r requirements.txt
`

## Como rodar o programa?
Para executar o programa, localize o arquivo main.py, 
que está dentro do pacote application, e execute-o. 
O programa possui uma interface gráfica desenvolvida com a biblioteca Pygame.

## Como rodar os testes?
### Caso deseje refazer os testes:

1 - `python -m pytest --cov -q .\tests\test_functionality.py`

2 - `coverage html`

3 - `start tests/htmlcov/index.html`

### Caso deseje abrir o teste já executado no projeto, basta digitar no terminal:

1 - `start tests/htmlcov/index.html`

#### Obs: O `start` nos comandos só funciona no sistema operacional Windows. Caso você utilize algum outro, esse prefixo mudará.