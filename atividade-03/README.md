# Atividade 03 — Validação de senha com do-while simulado

## Enunciado

Solicite a senha até que seja digitado `python123`.

## Código (`main.py`)

```python
senha_correta = "python123"

while True:
    senha = input("Digite sua senha: ")
    if senha == senha_correta:
        print("Acesso permitido!")
        break
    else:
        print("Senha incorreta. Tente novamente.")
```

## Explicação

Python não possui uma estrutura do-while nativa. O while True executa a leitura ao menos uma vez, e break encerra o laço quando a senha estiver correta.

## Exemplo de saída

```text
Digite sua senha: python123
Acesso permitido!
```
