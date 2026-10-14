run = True


name = input("Hej, vad heter du?: ")

while run:
    try:
        age = int(input("Hur gammal är du?: "))
        run = False
    except:
        print("Skriv i heltal.")

print(f"Hej {name}, du är {age} år gammal, Vad vill du göra?")
print("Alternativ: Mattetest, Nummertest, Avsluta")

choice = input()

if choice in {"Mattetest", "mattetest"}:
    point = 0
    run = True
    while run:
        try:
            print("Vad är 1+1?")
            svar = int(input())
            if svar == 2:
                print("Rätt!")
                point += 1
                run = False
            else:
                print("Fel!")
                run = False
        except:
            print("Försök igen")

    run = True
    while run:
        try:
            print("Vad är 2*2?")
            svar = int(input())
            if svar == 4:
                print("Rätt!")
                point += 1
                run = False
            else:
                print("Fel!")
                run = False
        except:
            print("Försök igen.")


    run = True
    while run:
        try:
            print("Vad är 5/2?")
            svar = float(input())
            if svar == 2.5:
                print("Rätt!")
                point += 1
                run = False
            else:
                print("Fel!")
                run = False
        except:
            print("Försök igen.")


    run = True
    while run:
        try:
            print("Vad är 3--5?")
            svar = int(input())
            if svar == 8:
                print("Rätt!")
                point += 1
                run = False
            else:
                print("Fel!")
                run = False
        except:
            print("Försök igen.")


    print(f"Du fick {point}/4 rätt.")
    if point == 4:
        print("Betyg: A")
    elif point == 3:
        print("Betyg: C")
    elif point == 2:
        print("Betyg: E")
    else:
        print("Betyg: F")

elif choice in {"Nummertest", "nummertest"}:
    score = 0
    print("Skriv 512 på svenska.")
    if input() in {"Femhundratolv", "femhundratolv"}:
        print("Rätt!")
        score += 1
    else:
        print("Fel!")
    print("Skriv 346 på svenska.")
    if input() in {"Trehundrafyrtiosex", "trehundrafyrtiosex"}:
        print("Rätt!")
        score += 1
    else:
        print("Fel!")
    print("Skriv 2003 på svenska.")
    if input() in {"Tvåtusentre", "tvåtusentre"}:
        print("Rätt!")
        score += 1
    else:
        print("Fel!")
    print("Skriv 42367 på svenska.")
    if input() in {"Fyrtiotvåtusentrehundrasextiosju", "fyrtiotvåtusentrehundrasextiosju"}:
        print("Rätt!")
        score += 1
    else:
        print("Fel!")
    print(f"Du fick {score}/4 rätt.")
    if score == 4:
        print("Betyg: A")
    elif score == 3:
        print("Betyg: C")
    elif score == 2:
        print("Betyg: E")
    else:
        print("Betyg: F")
    


elif choice in {"Avsluta", "avsluta"}:
    print("Avslutar...")
    exit()

