# Menu em Python

Este é um exemplo de código Python que implementa um menu interativo utilizando uma função `menu` e algumas visualizações.

## Funcionalidade

A função `menu` recebe uma lista de opções representadas por tuplas contendo uma string e uma função. O menu exibe as opções numeradas e aguarda a entrada do usuário. A entrada do usuário é validada e, se for uma opção válida, a função correspondente é executada. Caso contrário, uma mensagem de opção inválida é exibida e o menu é exibido novamente.

As visualizações `view_home` e `view_person` são exemplos de funções que podem ser utilizadas com o menu. Cada visualização exibe uma mensagem e chama a função `menu` para exibir suas próprias opções. A visualização `view_home` possui opções para listar pessoas e sair, enquanto a visualização `view_person` possui opções para voltar à tela inicial ou sair.

O programa principal é a função `main`, que chama a visualização inicial `view_home`.

## Como executar

Certifique-se de ter o Python instalado em seu ambiente. Salve o código em um arquivo com extensão `.py`, por exemplo, `menu_example.py`. Em seguida, abra um terminal ou prompt de comando e navegue até o diretório onde o arquivo foi salvo. Execute o programa usando o comando `python menu_example.py`. O menu será exibido e você poderá interagir com ele digitando as opções correspondentes.

## Exemplo de uso

```python
def view_home():
    print("Home")
    menu(("Listar Pessoas", view_person), ("Sair", exit))


def view_person():
    print("Pessoas")
    menu(("Voltar", view_home), ("Sair", exit))


def main():
    view_home()


if __name__ == "__main__":
    main()
```

## Contribuições

Contribuições são bem-vindas! Se você tiver sugestões de melhorias, correções de bugs ou outras implementações, sinta-se à vontade para enviar uma pull request.
