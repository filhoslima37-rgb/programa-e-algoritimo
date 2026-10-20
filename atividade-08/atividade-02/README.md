# Atividade 02 — Soma de números até digitar zero

## Enunciado

Solicite números inteiros até que o usuário digite zero. Apresente a soma.

## Código (`main.py`)

```python
soma = 0
numero = int(input("Digite um número (0 para sair): "))

while numero != 0:
    soma += numero
    numero = int(input("Digite outro número: "))

print("Soma total:", soma)
```

## Explicação

O programa recebe números inteiros e acumula seus valores. O número zero funciona como sentinela: encerra a entrada e não é somado.

## Exemplo de saída

```text
Digite um número (0 para sair): 5
Digite outro número: 10
Digite outro número: 3
Digite outro número: 0
Soma total: 18
```
