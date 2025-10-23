list_anime = []

while True:
    anim3 = str(input("Enter the name of an anime (or type 'exit' to finish): "))
    if anim3.lower() == 'exit':
        print(f"Your anime list includes: \n{list_anime}")
        break
    else:
        list_anime.append(anim3)
        print(f"{anim3} has been added to your list.")
        continue