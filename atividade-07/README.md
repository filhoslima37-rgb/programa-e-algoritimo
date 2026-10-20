# Atividade 07 — Contagem regressiva com while

## Enunciado

Leia um número inteiro positivo e faça uma contagem regressiva até zero.

## Código (`main.py`)

```python
numero = int(input("Digite um número positivo: "))

while numero >= 0:
    print(numero)
    numero -= 1

print("Contagem finalizada!")
```

## Explicação

Enquanto o valor for maior ou igual a zero, ele é exibido e decrementado em 1. Quando fica abaixo de zero, o laço termina.

## Exemplo de saída

```text
Digite um número positivo: 5
5
4
3
2
1
0
Contagem finalizada!
```
