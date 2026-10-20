# Atividade 04 — Tabuada utilizando for

## Enunciado

Solicite um número inteiro e exiba sua tabuada de 1 a 10.

## Código (`main.py`)

```python
numero = int(input("Digite um número: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
```

## Explicação

A função range(1, 11) gera os números de 1 a 10. O laço calcula e apresenta o produto do número informado por cada multiplicador.

## Exemplo de saída

```text
Digite um número: 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```
