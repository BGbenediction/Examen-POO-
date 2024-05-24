class Employer:
    def __init__(self, nom, salaire):
        self.nom = nom
        self.salaire = salaire
        
    def display(self):
        print(f"Votre nom est:", self.nom)
        print(f"Votre salaire est de:", self.salaire)
        
