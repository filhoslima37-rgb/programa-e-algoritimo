# Atividade 08 — Busca linear

## Enunciado

Busque um valor na lista de dez números e informe o índice encontrado.

## Código (`main.py`)

```python
numeros = [10, 25, 8, 40, 15, 30, 7, 50, 12, 20]
busca = int(input("Digite o número que deseja buscar: "))
encontrado = False

for i in range(len(numeros)):
    if numeros[i] == busca:
        print(f"Número encontrado no índice {i}")
        encontrado = True
        break

if not encontrado:
    print("Número não encontrado.")
```

## Explicação

A busca linear verifica os elementos da lista em sequência. Quando encontra o valor procurado, exibe seu índice e interrompe o laço com break. Se não encontrar, informa isso ao final.

## Exemplo de saída

```text
Digite o número que deseja buscar: 40
Número encontrado no índice 3
```
