# Atividade 06 — Ignorando números com continue

## Enunciado

Percorra os números de 1 a 20 e mostre apenas os ímpares usando continue.

## Código (`main.py`)

```python
for numero in range(1, 21):
    if numero % 2 == 0:
        continue
    print(numero)
```

## Explicação

O operador % calcula o resto da divisão. Se o resto da divisão por 2 for zero, o número é par e continue pula para a próxima repetição. Assim, são exibidos apenas os ímpares.

## Exemplo de saída

```text
1
3
5
7
9
11
13
15
17
19
```
