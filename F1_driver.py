# Formula 1 ABU DHABI GP 

import __main__

def f1_driver():

 total = 0 
 while True:
   
    print("\nFORMULA 1 ABU DHABI GRAND PRIX 2025")
    print("Race Details")
    print("Date: Sun, Dec 7, 2025, 9:00PM")
    print("Track: Yas Marina Circuit")
    print("@Formula 1")

    driver = int(input("\nF1 Driver number: "))

    match driver:
        case 1:
            print("\nM. Verstappen #1 - Redbull Racing")
            print("Position - 1 Time: 1:26:07.469 Pts - 25")
        case 81:
            print("\nO. Piastri #81 - McLaren")
            print("Position - 2 Time: +12.594s Pts - 18")
        case 4:
            print("\nL. Norris #4 - McLaren")
            print("Position - 3 Time: +16.572s Pts - 15")
        case 16:
            print("\nC. Leclerc #16 - Ferrari")
            print("Position - 4 Time: +23.279s Pts - 12")
        case 63:
            print("\nG. Rusell #63 - Mercedes")
            print("Position - 5 Time: +48.563s Pts - 10")
        case 14:
            print("\nF. Alonso #14 - Aston Martin")
            print("Position - 6 Time: +67.562s Pts - 8")
        case 31:
            print("\nE. Ocon #31 - Haas F1 Team")
            print("Position - 7 Time: +69.876s Pts - 6")
        case 44:
            print("\nL. Hamilton #44 - Ferrari")
            print("Position - 8 Time: +72.67s Pts - 4")
        case 27:
            print("\nN. Hülkenberg # 27 - Kick Sauber")
            print("Position - 9  Time: +79.014s Pts - 2")
        case 18:
            print("\nL. Stroll #18 - Aston Martin")
            print("Position - 10 Time: +79.523s Pts - 1")
        case 5:
            print("\nG. Bortoleto #5 - Kick Sauber")
            print("Position - 11 Time: +81.043s Pts - 0")
        case 87:
            print("\nO. Bearman #87 - Haas F1 Team")
            print("Position - 12 Time: +81.166s Pts - 0")
        case 55:
            print("\nC. Sainz Jr. #55 - Williams")
            print("Position - 13 Time: +82.158s Pts - 0")
        case 22:
            print("\nY. Tsunoda #22 - Redbull Racing")
            print("Position - 14 Time: +83.794s Pts - 0")
        case 12:
            print("\nA.K. Antonelli #12 - Mercedes")
            print("Position - 15 Time: +84.399s Pts - 0")
        case 23:
            print("\nA. Albon #23 - Williams")
            print("Position - 16 Time: +90.327s Pts - 0")
        case 6:
            print("\nI. Hadjar #6 - RB")
            print("Position - 17 Time: +1 Lap Pts - 0")
        case 30:
            print("\n L. Lawson #30 - RB")
            print("Position - 18 Time: +1 Lap Pts - 0")
        case 10:
            print("\nP. Gasly #10 - Alpine")
            print("Position - 19 Time: +1 Lap Pts - 0")
        case 43:
            print("\nF. Colapinto #43 - Alpine")
            print("Position - 20 Time: +1 Lap Pts - 0")
        
        case _:
            print("Driver not found, please try again.")
            break

if __name__ == "__main__":
    f1_driver()
