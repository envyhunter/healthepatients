def SaveTheDying(num, starting_health, heal_pow, threshold):
    heal = False
    patients = []
    current = 0
    if starting_health>num and heal_pow>num and ((threshold-starting_health)/heal_pow) > 1:
        for i in range(0, num):
            patients.append(starting_health)
        while(heal == False):
            print(patients)
            heal_near_death = False
            cHeal = 0
            if patients[current] >= threshold:
                    #print("first if")
                    current = (current + 1)% num
            for p in range(len(patients)):
                if patients[p] <= heal_pow:
                    #print("second if")
                    patients[p] = patients[p] + heal_pow
                    cHeal = p
                    heal_near_death = True
                    break
            if not heal_near_death:
                #print("third if")
                patients[current] = patients[current] + heal_pow
                cHeal = current
                
            for p in range(len(patients)):
                if(patients[p] <= 0):
                    print("failed")
                    exit()
                if(patients[p] < threshold and p != cHeal):
                    patients[p] = patients[p] - 1
                
            for p in range(len(patients)):
                if patients[p] < threshold:
                    heal = False
                    break
                else:
                    #print("success")
                    heal = True
        print(patients)
        #print("out")
        #print(heal)
    else:
        print("Inputs break rules")
    


SaveTheDying(10, 11, 15, 27)
