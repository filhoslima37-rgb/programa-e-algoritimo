# Atividade 09 — Ordenação Bubble Sort

## Enunciado

Ordene uma lista em ordem crescente sem usar `sort()` nem `sorted()`.

## Código (`main.py`)

```python
numeros = [8, 3, 5, 1, 9, 2]
n = len(numeros)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if numeros[j] > numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print("Lista ordenada:", numeros)
```

## Explicação

O Bubble Sort compara elementos vizinhos e troca suas posições quando estão fora de ordem. As passagens se repetem até que a lista fique em ordem crescente. O algoritmo não usa sort() nem sorted().

## Exemplo de saída

```text
Lista ordenada: [1, 2, 3, 5, 8, 9]
```
