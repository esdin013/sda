class Fiets:
    def __init__(self, type, versnellingen):
        
        self.type = type
        self.versnellingen = versnellingen
        self.huidige_versnelling = 1

    def schakel_omhoog(self, versnellingen_omhoog):
        self.huidige_versnelling += versnellingen_omhoog
        print(f'ik schakel de versnelling {versnellingen_omhoog} omhoog')
    
racefiets = Fiets('racefiets', 21)
stadsfiets = Fiets('stadsfiets', 6)
racefiets.schakel_omhoog(2)
#reacefiets.huidige_versnellingen = 2

print(racefiets.type)
print(racefiets.versnellingen)
print(racefiets.huidige_versnelling)

print(stadsfiets.type)
print(stadsfiets.versnellingen)
print(stadsfiets.huidige_versnelling)