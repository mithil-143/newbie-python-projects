def main():
    weapon = input("Choose a weapon(sword,bow,spell): ").lower()
    distance = float(input("Enter distance from target(in metres): "))
    print(calculate_damage(weapon,distance)) 
def calculate_damage(weapon,distance):
    match weapon:
        case "bow":
            base_damage = 12
            if  5<= distance <=30:
                damage = base_damage*2
                return f"Total damage:{damage}"
            elif 31>=distance >=4:
               damage = base_damage
               return f"Total damage:{damage}"
            else: 
               return "Attack missed! Target out of range"
        case "sword":
            base_damage = 15
            if 0<= distance <=5:
                damage = base_damage*1.5
                return f"Total damage:{damage}"
            elif 0<=distance<=7:
                damage = base_damage    
                return f"Total damage:{damage}"       
            else:
                return "Attack missed! Target out of range"
        case "spell":
            base_damage = 20
            if  5<= distance <=30:
             damage = base_damage*2
             return f"Total damage:{damage}"
            elif 31>=distance >=4 :
             damage = base_damage
             return f"Total damage:{damage}"
            else:
              return "Attack missed! Target out of range"                
        case _:
            return "Invalid weapon selection"
       

main()
