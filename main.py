def add(a, b):
    int_a, int_b = int("0b"+a, 2), int("0b"+b, 2)

    return bin(int_a+int_b)[2:]

def round_bin(a, man_len):
    b = ""
    for _ in range(man_len):
        b += "0"
    b+="1"
    rounded = add(a,b)
    while len(rounded) < man_len+1:
        rounded = "0"+rounded
    return rounded

def dec_to_flp(a: float):
    x = input("Podaj kolejno po spacjach dlugosci wykladnika i mantysy:").split()
    man_len = int(x[1])
    exp_len = int(x[0])

    print(man_len)

    sign = 0
    if a < 0:
        a *= -1
        sign = 1

    print(f"Liczba: {a}") #Liczba do przekonwertowania

    print(f"Znak: {sign}") #znak liczby

    print("Obliczanie mantysy: ")

    i = int(a) #na poczatku przeliczymy czesc calkowita
    frac = a - i

    int_bin = bin(i)[2:]
    frac_bin="0."

    since_one = -1

    #teraz przeliczymy częsc ułamkową, ale tylko do okreslonego momentu, żeby nie wypisywac w nieskonczonosc
    #szuakmy kolejnych rozwiniec jezeli wypiszemy tyle bitow po pierwszej jedynce ile jest ma byc w mantysie

    while frac > 0 and since_one < man_len+1:
        print(f"{round(frac, 6)} * 2 = ", end="")
        frac *= 2
        print(f"{round(frac, 6)} ", end="")
        if int(frac) == 1:
            frac_bin += '1'
            if since_one < 0:
                since_one = 0
            else:
                since_one += 1

            print("| 1")

            frac -= 1
        else:
            frac_bin += '0'
            if since_one >= 0:
                since_one += 1

            print("| 0")
    frac_bin = frac_bin[2:]
    man_ = f"{int_bin}.{frac_bin}" #mantysa przed normalizacja
    print(f"Mantysa nieznormalizowana: {man_}")

    exp = 0

    if i > 0: #jezeli liczba ma czesc calkowita
        while len(int_bin) > 1:
            c = int_bin[-1]
            frac_bin = c+frac_bin
            int_bin = int_bin[:-1]
            exp+=1
        man_normalized = f"{int_bin}.{frac_bin}"
        print(man_normalized)
    else:
        c='0'
        while c == '0':
            c = frac_bin[0]
            frac_bin = frac_bin[1:]
            exp-=1
        man_normalized = f"1.{frac_bin}"

    print(f"Mantysa znormalizowana: {man_normalized} wykladnik przed dodaniem skuchy: {exp}")



    #teraz ukrywamy pierwszy bit, i odcinamy do odpowiedniej dlugosci
    for _ in range(man_len+1):
        man_normalized = man_normalized + '0'
    man_normalized = man_normalized[2:man_len+3]
    #print(man_normalized)  tutaj mamy mantyse z jednym dodatkowym bitem

    #zaokrąglamy
    man_rounded = round_bin(man_normalized, man_len)
    if len(man_rounded) > man_len + 1:
        print("Nastąpiło przeładowanie mantysy. należy przesunac wykladnik")
        print(f"Mantysa wynosi 1.{man_rounded[1:]}")
        print("Należy dodać 1 do wykładnika")
        exp += 1
        man_rounded = man_rounded[1:]
    else:
        print(f"Mantysa po zaokrągleniu wynosi 0.{man_rounded}, dodatkowy bit nie zmienił mantysy")

    man_rounded = man_rounded[:-1]

    #liczymy skuche
    skucha = (2**(exp_len-1)) - 1
    exp += skucha



    print(f"\nSkucha wynosi: {skucha} \nWykładnik po dodaniu skuchy: {exp}")

    exp_bin = bin(exp)[2:]
    while len(exp_bin) < exp_len:
        exp_bin = "0"+exp_bin

    print(f"Wykładnik zapisany binarnie: {exp_bin}")

    print(f"\nOdpowiedz: \n{sign} {exp_bin} {man_rounded} ")

a = float(input("Podaj liczbe do policzenia jebanego flp: "))
dec_to_flp(a)