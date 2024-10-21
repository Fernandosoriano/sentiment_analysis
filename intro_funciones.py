def suma (numero_uno:int, numero_dos:int) -> int:
    res = numero_uno + numero_dos
    return res

print(suma(3,2))

suma_lam = lambda n_1, n_2: n_1 + n_2
print (suma_lam(3,2))