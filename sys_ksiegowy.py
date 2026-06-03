operacje = ("saldo", "sprzedaż", "zakup", "konto", "lista", "magazyn", "przeglad", "koniec")
magazyn = {
    "rower":{
        #"wartość": 900.00,
        "ilość": 10
    },
    "hulajnoga":{
        #"wartość":150.00,
        "ilość":10
    },
    "kask":{
        #"wartość":100.00,
        "ilość":10
    },
    "rolki":{
        #"wartość":350.00,
        "ilość":10
    },
    "ochraniacze":{
        #"wartość":80.00,
        "ilość":10
    },
    "piłka":{
        #"wartość":10.00,
        "ilość":10
    },
    "sup":{
        #"wartość":1700.00,
        "ilość":10
    },
    "pedały":{
        #"wartość":50.00,
        "ilość":10
    },
    "bidon":{
        #"wartość":20.00,
        "ilość":10
    }
}
stan_konta = 0
operacja = input(f"Podaj operację jaką chcesz wykonać: {operacje}\n")
match operacja:
    case "saldo":
        a = float(input("Podaj kwotę, którą mam dodać do stanu konta (użyj - jeśli chcesz tę kwotę odjąć): "))
        stan_konta+=a
        print (f"Aktualny stan konta wynosi: {stan_konta} zł")
    case "sprzedaż":
        item = input("Który produkt chcesz sprzedać?\n")
        if item not in magazyn: #sprawdzam czy dany produkt jest w magazynie
            print("Brak produktu w magazynie.")
        else:
            quantity = int(input("Ile sztuk chcesz sprzedać?\n"))
            if quantity > magazyn[item]["ilość"]: #sprawdzam czy mam wystarczającą ilość w magazynie
                print(f"W magazynie znajduje się tylko {magazyn[item]["ilość"]} sztuk.")
            else:
                cost = float(input("Ile kosztuje ten produkt?\n"))
                stan_konta+=cost
                magazyn[item]["ilość"]-=quantity #odejmuje z magazynu sprzedane produkty
                print(f"Aktualny stan konta wynosi: {stan_konta} zł")
                print(f"Aktualny stan magazynowy:\n{magazyn}")

#    case "zakup":
#    case "konto":
#    case "lista":
#    case "magazyn":
#    case "zprzeglad":
#    case "koniec":

