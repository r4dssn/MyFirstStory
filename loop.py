food = input("Vad blir det för mat idag?")

choice = input("Kan du äta maten?")
if choice == "nej" :
    print("Gå till hemköp")


tal = int(input("Hur många äpplen vill du köpa"))

counter = 0
while tal < 40 :
    counter = counter + 1
    print(counter, "Du är hungrig!")
    tal = counter

print("Hej då.")