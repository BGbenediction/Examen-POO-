class Employer:
    def __init__(self, nom, salaire):
        self.nom = nom
        self.salaire = salaire
        
    def display(self):
        print(f"Votre nom est:", self.nom)
        print(f"Votre salaire est de:", self.salaire)
        
class Manageur(Employer):
    def __init__(self, nom, salaire, bonus):
        super().__init__(nom, salaire)
        self.bonus = bonus
        
    def display(self):
        super().display()
        print("Bonus:", self.bonus)
        
class Intern(Employer):
    def __init__(self, nom, stipend):
        super().__init__(nom, stipend)
        
    def display(self):
        super().display()
        print("Stipend:", self.salaire)
