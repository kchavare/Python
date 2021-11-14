def test():
    PeoplesBloodComposition=[]
    Virus=str(input("Name the virus:").lower())
    Number_of_people=int(input("Number of People:"))
    for people in range(Number_of_people):
        BloodComposition=str(input("Enter the Blood Composition:").lower())
        PeoplesBloodComposition.append(BloodComposition)
    for BloodComp in PeoplesBloodComposition:
        Result=CheckResult(BloodComp,Virus)
        print(Result)

def CheckResult(BloodComposition,VirusComposition):
    constanst=""
    for B in BloodComposition:
        if B in VirusComposition:
            if not B in constanst:
                constanst=constanst + B
    if constanst==BloodComposition:
        return "POSITIVE"
    else:    
        return "NEGATIVE" 

test()