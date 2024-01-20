N = int(input())

while N > 0:
    A, B = input().split()

    # Verifica se B corresponde aos últimos dígitos de A
    if A.endswith(B):
        print("encaixa")
    else:
        print("nao encaixa")

    N -= 1
