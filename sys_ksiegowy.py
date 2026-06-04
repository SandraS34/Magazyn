from idlelib import history

operacje = ["saldo", "sprzedaż", "zakup", "konto", "lista", "magazyn", "przeglad", "koniec"]
magazyn = { #tworzę słownik słowników
    "rower":{
        "wartość": 900.00,
        "ilość": 10
    },
    "hulajnoga":{
        "wartość":150.00,
        "ilość":10
    },
    "kask":{
        "wartość":100.00,
        "ilość":10
    },
    "rolki":{
        "wartość":350.00,
        "ilość":10
    },
    "ochraniacze":{
        "wartość":80.00,
        "ilość":10
    },
    "piłka":{
        "wartość":10.00,
        "ilość":10
    },
    "sup":{
        "wartość":1700.00,
        "ilość":10
    },
    "pedały":{
        "wartość":50.00,
        "ilość":10
    },
    "bidon":{
        "wartość":20.00,
        "ilość":10
    }
}
historia_op = []
stan_konta = 0
while True:
    operacja = input(f"Podaj operację jaką chcesz wykonać: {operacje}\n")
    match operacja:
        case "saldo":
            historia_op.append("saldo")
            zmiana = input("Chcesz dodać kwotę do stanu konta, czy odjąć?\n")
            match zmiana:
                case "dodać":
                    a = float(input("Podaj kwotę, którą mam dodać do stanu konta: "))
                    if a < 0:
                        print("Podałeś ujemną kwotę.")
                    else:
                        stan_konta+=a
                        print(f"Do stanu Twojego konta dodano {a} zł")
                        #historia_op.append({"typ": "saldo", "kwota dodana": a})
                case "odjąć":
                    a = float(input("Podaj kwotę, którą mam odjąć z konta: "))
                    if a > stan_konta:
                        print("Nie mogę wykonać tej operacji. Na koncie jest za mało pieniędzy!")
                    elif a <0:
                        print("Podałeś ujemną kwotę.")
                    else:
                        stan_konta-=a
                        print(f"Z Twojego konta ubyło {a} zł")
                        #historia_op.append({"typ": "saldo", "kwota odjęta":a})
                case _:
                    print("Nie znaleziono takiej operacji.")
            #print (f"Aktualny stan konta wynosi: {stan_konta} zł")
        case "sprzedaż":
            historia_op.append("sprzedaż")
            item = input(f"Który produkt chcesz sprzedać? {magazyn.keys()}\n")
            if item not in magazyn: #sprawdzam czy dany produkt jest w magazynie
                print("Brak produktu w magazynie.")
            else:
                quantity = int(input("Ile sztuk chcesz sprzedać?\n"))
                if not isinstance(quantity, int) or quantity <= 0:
                    print("Podałeś nieprawidłową wartość!")
                elif quantity > magazyn[item]["ilość"]: #sprawdzam czy mam wystarczającą ilość w magazynie
                    print(f"W magazynie znajduje się tylko {magazyn[item]["ilość"]} sztuk.")
                else:
                    cost = float(input("Ile kosztuje ten produkt?\n"))
                    if not isinstance(cost, float) or cost <= 0:
                        print("Podałeś nieprawidłową wartość!")
                    else:
                        stan_konta+=cost*quantity
                        magazyn[item]["ilość"]-=quantity #odejmuje z magazynu sprzedane produkty
            #historia_op.append({"typ":"sprzedaż","Produkt":item,""})
        case "zakup":
            historia_op.append("zakup")
            item = input("Jaki produkt chcesz kupić?\n")
            cost = float(input("Ile kosztuje ten produkt?\n"))
            if not isinstance(cost, float) or cost <= 0:
                print("Podałeś nieprawidłową wartość!")
            else:
                quantity = int(input("Ile sztuk chcesz kupić?\n"))
                if not isinstance(quantity, int) or quantity <= 0:
                    print("Podałeś nieprawidłową wartość!")
                else:
                    exp=cost*quantity
                    if exp > stan_konta: #sprawdzam czy mnie stać na takie zakupy
                        print("Nie stać Cię na takie zakupy!")
                    elif item not in magazyn: #jeśli mnie stać to sprawdzam czy mam ten produkt w magazynie
                        magazyn[item]={"wartość":cost,"ilość":quantity} #dodaję nowy produkt do magazynu
                        stan_konta-=exp
                    else:
                        magazyn[item]["ilość"]+=quantity #zwiększam ilość już posiadanego produktu
                        stan_konta-=exp
        case "konto":
            print(f"Aktualny stan konta wynosi: {stan_konta} zł")
        case "lista":
            print(f"Aktualny stan magazynowy:\n{magazyn}")
        case "magazyn":
            item = input(f"Informacje o którym produkcie mam wyświetlić: {magazyn.keys()}?\n")
            if item not in magazyn:
                print("Brak produktu w magazynie.")
            else:
                print(magazyn[item])
        case "przeglad":
            print("Podaj zakres wyświetlenia historii.")
            od = input("Początek: ")
            do = input("Koniec: ")
            if od == "":
                od = 0
            else:
                od = int(od)
            if do == "":
                do = len(historia_op)
            else:
                do = int(do)
            if od >=0 and do <= len(historia_op) and od<=do:
                for operacja in historia_op[od:do]:
                    print(operacja)
            else:
                print(f"Niepoprawny zakres. Ilość wykonanych operacji wynosi: {len(historia_op)}")
        case "koniec":
            break #koniec pętli while true
        case _:
            print("Nie znaleziono takiej operacji.")

