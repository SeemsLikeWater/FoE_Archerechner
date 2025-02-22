from itertools import accumulate

from mpmath.matrices.eigen import Eigen

if __name__ == "__main__":
    print("Archerechner")

    z = 0.0005   # tolerance floating point imprecission

    # Arche Bonus der Mäzen
    bonus = 1.93

    # Basis Stats der Stufe
    totalFP = 11308
    base_P1 = 1965

    # FPs die bereits eingezahlt wurden
    EigenFP = 4216
    Extern = [0, 0, 0, 0, 0]

    total = totalFP
    temp = base_P1
    values_bases =[base_P1]
    for i in range(2, 6):
        values_bases.append(round(temp/5./i +z)*5)
        temp = values_bases[i-1]
    print(values_bases)


    values_19 = [round(value * bonus + z) for value in values_bases]
    print(values_19)

    Exp_Eigen = total - sum(values_19)

    total = total - EigenFP
    print(total)
    print()

    all_costs = []
    all_to_save = []
    curr_Ex = 0
    for value in values_19:
        print(f"curr value = {value}, curr Ex = {Extern[curr_Ex]}")
        to_save = 0
        if Extern[curr_Ex] >= value and Extern[curr_Ex] != 0 or Extern[curr_Ex]>=total/2:
            all_costs.append("*" + str(Extern[curr_Ex]))
            to_save = round(total - 2*Extern[curr_Ex])
            if(to_save <= 0):
                print(f"  Ex sicher")
                to_save = 0
            else:
                print(f"  save Ex {Extern[curr_Ex]} with {to_save}")
            total = total - to_save - Extern[curr_Ex]
            curr_Ex = curr_Ex +1
        else:
            all_costs.append(value)
            to_save = round((total - 2*value))
            if(to_save <= 0):
                to_save = 0
                print(f"  sicher")
            else:
                print(f"  save {value} with {to_save}")
            total = total - to_save - value
        all_to_save.append(to_save)
    print(f"{all_to_save}")

    players = ["P1", "P2", "P3", "P4", "P5"]
    values_bases
    all_costs
    all_to_save
    all_Eigen = list(accumulate(all_to_save))

    width = 6
    print()
    print()
    print(f"bereits eingezahlt: {EigenFP}    mit Externen: {Extern}")
    print(f"{"Platz":^{width}} {"Basis":^{width}} {"Kosten":^{width}} {"Sichern":^{width}} {"Eigen":^{width}}")
    for p,base,cost,save,own in zip(players,values_bases,all_costs,all_to_save,all_Eigen):
        print(f"{p:^{width}} {base:^{width}} {cost:^{width}} {save:^{width}} {own:^{width}}")

    EigenFP = EigenFP + sum(all_to_save) + total
    if curr_Ex <= 4:
        for i in range(curr_Ex, 5):
            EigenFP = EigenFP - Extern[i]

    print(f"            Eigen-FP:{EigenFP}")
    if EigenFP == Exp_Eigen:
        print("1.9 success")
    elif EigenFP < Exp_Eigen:
        print(f"saved {Exp_Eigen - EigenFP}")
    else:
        print(f"sniped by {EigenFP - Exp_Eigen}")

    print(EigenFP)
    print(Exp_Eigen)