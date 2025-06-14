import tkinter as tk
from model import Model
from view import View
import re
from datetime import datetime


class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root, self)

        # Associe les boutons définis dans la vue à des méthodes du contrôleur (ajouter_entreprise, rechercher_entreprise, lire_entreprises)
        self.view.ajouter_bouton.config(command=self.ajouter_entreprise)
        self.view.rechercher_bouton.config(command=self.rechercher_entreprise)
        self.view.afficher_bouton.config(command=self.lire_entreprises)

        # Centrage de la fenêtre principale
        self.center_window(root, 1000, 400)


    # Méthode calcule la position idéale pour centrer la fenêtre sur l'écran
    def center_window(self, root, width, height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        position_top = int(screen_height / 2 - height / 2)
        position_right = int(screen_width / 2 - width / 2)
        root.geometry(f'{width}x{height}+{position_right}+{position_top}')


    #  Récupère les valeurs saisies dans les champs de texte de la vue (nom, registre, adresse... )
    def get_data_from_view(self):
        return (
            self.view.nom_entry.get(),
            self.view.registre_entry.get(),
            self.view.adresse_entry.get(),
            self.view.email_entry.get(),
            self.view.telephone_entry.get(),
            self.view.date_entry.get(),
            self.view.secteur_entry.get()
        )


    # Méthode pour ajouter une entreprise
    def ajouter_entreprise(self):
        data = self.get_data_from_view()

        if all(data): # Assure que tous les champs sont remplis
            # Vérifier le format de la date
            if not self.is_valid_date(data[5]):
                self.view.afficher_erreur("Petit rappel", "La date doit être au format YYYY-MM-DD. Merci de corriger !")
                return
            # Vérifie k le numéro contient exactement 10 chiffres
            if not self.is_valid_phone(data[4]):
                self.view.afficher_erreur("Petit rappel", "Un numéro de téléphone valide, c’est 10 chiffres ni plus, ni moins.")
                return

            try: # Ajoute les données
                self.model.ajouter_entreprise(data)
                self.view.afficher_message("Mission accomplie", "l’entreprise a été enregistrée avec succès.")
            except Exception as e:
                self.view.afficher_erreur("Erreur", str(e))
        else:
            self.view.afficher_erreur("Pas si vite !", "Chaque champ a son importance. Prenez un moment pour tout remplir.")


    # Méthode pour rechercher une entreprise
    def rechercher_entreprise(self):
     # Récupérer les valeurs saisies dans les champs de recherche (nom et registre)
     critere = self.view.recherche_entry.get()

     # Si le champ de recherche est vide, afficher un message d'erreur
     if not critere:
        self.view.afficher_erreur("Oups !", "Entrez un nom ou un numéro de registre pour procéder.")
        return

     # Appeler la méthode de recherche dans le modèle
     resultats = self.model.rechercher_entreprise(critere)

     # Afficher les résultats dans une fenêtre d'information
     if resultats:
        for entreprise in resultats:
            details = (
                f"ID : {entreprise[0]}\n"
                f"Nom : {entreprise[1]}\n"
                f"Numéro de Registre : {entreprise[2]}\n"
                f"Adresse : {entreprise[3]}\n"
                f"Email : {entreprise[4]}\n"
                f"Téléphone : {entreprise[5]}\n"
                f"Date d'inscription : {entreprise[6]}\n"
                f"Secteur : {entreprise[7]}"
            )
            self.view.afficher_message("À propos de l'entreprise", details)
     else:
        self.view.afficher_message("Pas de résultat !", "Aucune entreprise trouvée avec ces critères.")


    # Récupère toutes les entreprises et les affiche
    def lire_entreprises(self):
        entreprises = self.model.lire_entreprises()
        if entreprises:
            self.view.afficher_resultats(entreprises)
        else:
            self.view.afficher_message("Aucune entreprise", "Aucune entreprise enregistrée.")
    

    # Vérifie si une chaîne correspond au format de date YYYY-MM-DD
    def is_valid_date(self, date_str):
        try:
            datetime.strptime(date_str, '%Y-%m-%d')
            return True
        except ValueError:
            return False
    

    # Vérifie si un numéro de téléphone contient exactement 10 chiffres
    def is_valid_phone(self, phone):
        return re.match(r'^\d{10}$', phone) is not None



if __name__ == "__main__": 
    root = tk.Tk()
    app = Controller(root) # Initialise le contrôleur
    root.mainloop() # Afficher la fenêtre et interagir avec l'utilisateur
