# Python sets
# Each event uses de function to have their own space
# Use class to organize events and swimmers podium

class Olympics_Finals():
    @staticmethod
    def Men_50m_Freestyle():
        swimmers = {"1": "Cameron McEvoy", "2": "Benjamin Proud", "3": "Florent Manaudou"}
        return swimmers
    def Men_100m_Freestyle():
        swimmers = {"1": "Zhanle Pan", "2": "Kyle Chalmers", "3": "David Popovici"}
        return swimmers
    def Men_200m_Freestyle():
        swimmers= {"1": "David Popovici", "2": "Mathew Richards", "3": "Luke Hobson"}
        return swimmers
    def Men_400m_Freestyle():
        swimmers = {"1": "Lucas Maertens", "2": "Elijah Winnington", "3": " Woomin Kim"}
        return swimmers
    def Men_800m_Freestyle():
        swimmers = {"1": "Daniel Wiffen", "2": "Bobby Finke", "3": "Gregorio Paltrinieri"}
        return swimmers
    def Men_1500m_Freestyle():
        swimmers = {"1": "Bobby Finke", "2": "Gregorio Paltrinieri", "3": "Daniel Wiffen"}
        return swimmers
    
if __name__ == "__main__":

    event = Olympics_Finals.Men_1500m_Freestyle()

    for swimmer in event:
        print(f"{swimmer}: {event[swimmer]}")