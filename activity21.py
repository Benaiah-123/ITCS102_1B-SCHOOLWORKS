miles_ulaga = True

while miles_ulaga == True:
    answer = input("\n Si miles ay ulaga? (y / n) " ).lower()
    if answer == "y":
        print("\n magbago, magpakaulaga, or manlalake")
        duh = input("Ano gagawin nya? " ).lower()
        if duh == "magbago":
            print("\t go mo yan te")
        elif duh == "magpakaulaga":
            print("\t bala ka te sa buhay mo")
        elif duh == "manlalake":
            print("\t ayan ha puro nalang ka anuhan sa buhay")
        continue
    if answer == "n":
        print("\n  wow, okay po!")
        break