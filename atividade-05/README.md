# Atividade 05 — Média de cinco notas

## Enunciado

Leia cinco notas, calcule a média e informe aprovação para média maior ou igual a 7.

## Código (`main.py`)

```python
soma = 0

for i in range(1, 6):
    nota = float(input(f"Digite a {i}ª nota: "))
    soma += nota

media = soma / 5
print(f"Média do aluno: {media:.2f}")

if media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
```

## Explicação

O laço for solicita cinco notas e soma seus valores. Depois, a soma é dividida por cinco. A média igual ou superior a 7 indica aprovação.

## Exemplo de saída

```text
Digite a 1ª nota: 8
Digite a 2ª nota: 7
Digite a 3ª nota: 9
Digite a 4ª nota: 6
Digite a 5ª nota: 10
Média do aluno: 8.00
Aluno aprovado
```
