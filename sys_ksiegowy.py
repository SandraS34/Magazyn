operacje = ["saldo", "sprzedaż", "zakup", "konto", "lista", "magazyn", "przeglad", "koniec"]
stan_konta = 0
operacja = input(f"Podaj operację jaką chcesz wykonać: {operacje[::]}\n")
match operacja:
    case "saldo":
        a = int(input("Podaj kwotę, którą mam dodać do stanu konta (użyj - jeśli chcesz tę kwotę odjąć): "))
        #if isinstance(a, int|float):
        stan_konta+=a
        print (f"Aktualny stan konta wynosi: {stan_konta} zł")
#     case "sprzedaż":
#     case "zakup":
#     case "konto":
#     case "lista":
#     case "magazyn":
#     case "zprzeglad":
#     case "koniec":

