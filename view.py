import tkinter as tk
from tkinter import ttk # Fournit des widgets (comme les arbres Treeview)
from tkinter import messagebox 


# Initialisation de la classe View
class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller 
        

        # Paramétrage de la fenêtre principale 
        self.root.title("Gestion des Entreprises")
        self.root.geometry("600x400")
        

        # Couleurs par défaut de l'interface 
        self.mode_clair = {
            "bg": "#ecf0f1",
            "fg": "#000000",
            "button_bg": "#a9cce3",
            "button_fg": "black"
        }


        # Couleurs de l'interface pour le mode nuit 
        self.mode_nuit = {
            "bg": "#1e1e1e",  
            "fg": "#e0e0e0",  
            "button_bg": "#3b3b3b", 
            "button_fg": "#f0f0f0"
        }
        # Initialisation du current mode a mode clair 
        self.current_mode = self.mode_clair


        # Style pour le tableau de resulats de l'affichage de ttes les entreprises 
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", background="#ffffff", foreground="black", rowheight=25, fieldbackground="fffffff")
        style.map("Treeview", background=[("selected", "#7b241c")])


        # Création du cadre principal et des sous-cadres
        self.main_frame = tk.Frame(root, bg=self.current_mode["bg"])
        self.main_frame.pack(expand=True) # Permet au cadre de se redimensionner pour occuper tt l'espace disponible dans la fenêtre principale
        

        # 3 sous-cadres sont créés pour organiser les différentes sections de l'interface ( Afficher une entreprise, Rechercher et Afficher ttes les entreprises )
        self.frame_ajout = tk.LabelFrame(self.main_frame, text="Ajouter une entreprise", bg=self.current_mode["bg"], fg=self.current_mode["fg"], font=("Roboto", 10, "bold"))
        self.frame_ajout.grid(row=0, column=0, padx=20, pady=10, sticky="ew")

        self.frame_recherche = tk.LabelFrame(self.main_frame, text="Rechercher une entreprise", bg=self.current_mode["bg"], fg=self.current_mode["fg"], font=("Roboto", 10, "bold"))
        self.frame_recherche.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.frame_affichage = tk.LabelFrame(self.main_frame, text="Afficher toutes les entreprises", bg=self.current_mode["bg"], fg=self.current_mode["fg"], font=("Roboto", 10, "bold"))
        self.frame_affichage.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        

        # Création des champs d'entrée pour l'ajout d'une entreprise (Nom, NumRegistre, Adresse... )
        tk.Label(self.frame_ajout, text="Nom", bg=self.current_mode["bg"], fg=self.current_mode["fg"]).grid(row=0, column=0, sticky="w")
        self.nom_entry = tk.Entry(self.frame_ajout, width=30)
        self.nom_entry.grid(row=0, column=1)

        tk.Label(self.frame_ajout, text="Numéro de Registre", bg=self.current_mode["bg"], fg=self.current_mode["fg"]).grid(row=1, column=0, sticky="w")
        self.registre_entry = tk.Entry(self.frame_ajout, width=30)
        self.registre_entry.grid(row=1, column=1)

        tk.Label(self.frame_ajout, text="Adresse", bg=self.current_mode["bg"], fg=self.current_mode["fg"]).grid(row=2, column=0, sticky="w")
        self.adresse_entry = tk.Entry(self.frame_ajout, width=30)
        self.adresse_entry.grid(row=2, column=1)

        tk.Label(self.frame_ajout, text="Email", bg=self.current_mode["bg"], fg=self.current_mode["fg"]).grid(row=3, column=0, sticky="w")
        self.email_entry = tk.Entry(self.frame_ajout, width=30)
        self.email_entry.grid(row=3, column=1)

        tk.Label(self.frame_ajout, text="Téléphone", bg=self.current_mode["bg"], fg=self.current_mode["fg"]).grid(row=4, column=0, sticky="w")
        self.telephone_entry = tk.Entry(self.frame_ajout, width=30)
        self.telephone_entry.grid(row=4, column=1)

        tk.Label(self.frame_ajout, text="Date d'inscription", bg=self.current_mode["bg"], fg=self.current_mode["fg"]).grid(row=5, column=0, sticky="w")
        self.date_entry = tk.Entry(self.frame_ajout, width=30)
        self.date_entry.grid(row=5, column=1)

        tk.Label(self.frame_ajout, text="Secteur", bg=self.current_mode["bg"], fg=self.current_mode["fg"]).grid(row=6, column=0, sticky="w")
        self.secteur_entry = tk.Entry(self.frame_ajout, width=30)
        self.secteur_entry.grid(row=6, column=1)
        

        # Bouton Ajouter une entreprise
        self.ajouter_bouton = tk.Button(self.frame_ajout, text="Ajouter", bg=self.current_mode["button_bg"], fg=self.current_mode["button_fg"], font=("Lora", 10, "bold"), relief="solid", bd=1)
        self.ajouter_bouton.grid(row=7, column=0, columnspan=2, pady=10)


        # Rechercher une entreprise par son nom ou numero de son registre 
        tk.Label(self.frame_recherche, text="Rechercher par nom/registre", bg=self.current_mode["bg"], fg=self.current_mode["fg"]).grid(row=0, column=0, sticky="w")
        self.recherche_entry = tk.Entry(self.frame_recherche, width=30)
        self.recherche_entry.grid(row=0, column=1)


        # Bouton Rechercher 
        self.rechercher_bouton = tk.Button(self.frame_recherche, text="Rechercher", bg=self.current_mode["button_bg"], fg=self.current_mode["button_fg"], font=("Lora", 10, "bold"), relief="solid", bd=1)
        self.rechercher_bouton.grid(row=1, column=0, columnspan=2, pady=10)


        # Bouton Afficher ttes les entreprises 
        self.afficher_bouton = tk.Button(self.frame_affichage, text="Afficher toutes les entreprises", bg=self.current_mode["button_bg"], fg=self.current_mode["button_fg"], font=("Lora", 10, "bold"), relief="solid", bd=1)
        self.afficher_bouton.grid(row=0, column=0, columnspan=2, pady=10)


        # Bouton de changement de mode
        self.bouton_mode_nuit = tk.Button(self.main_frame, text="Mode Nuit", command=self.toggle_mode, bg=self.current_mode["button_bg"], fg=self.current_mode["button_fg"], font=("Lora", 8, "bold"), relief="solid", bd=1)
        self.bouton_mode_nuit.grid(row=0, column=2, columnspan=2, sticky="ne", pady=10)


        # Applique les couleurs du mode choisi
        self.apply_mode()
  

        # Tableau (Treeview) pour afficher les entreprises
        self.tree = ttk.Treeview(self.frame_affichage, columns=("id", "nom", "registre", "adresse", "email", "telephone", "date", "secteur"), show="headings")


        # Les en-têtes du tableau
        self.tree.heading("id", text="ID")
        self.tree.heading("nom", text="Nom")
        self.tree.heading("registre", text="Registre")
        self.tree.heading("adresse", text="Adresse")
        self.tree.heading("email", text="Email")
        self.tree.heading("telephone", text="Téléphone")
        self.tree.heading("date", text="Date d'inscription")
        self.tree.heading("secteur", text="Secteur")
        self.tree.column("id", width=30, anchor="center")
        self.tree.column("nom", width=100)
        self.tree.column("registre", width=100)
        self.tree.column("adresse", width=150)
        self.tree.column("email", width=150)
        self.tree.column("telephone", width=100)
        self.tree.column("date", width=100)
        self.tree.column("secteur", width=100)
        self.tree.grid(row=1, column=0, columnspan=2, pady=10, sticky="nsew")

        scrollbar = ttk.Scrollbar(self.frame_affichage, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, column=2, sticky="ns")


    # Basculer entre le mode jour et le mode nuit
    def toggle_mode(self):
     if self.current_mode == self.mode_clair:
        self.current_mode = self.mode_nuit
        self.bouton_mode_nuit.config(text="Mode Jour")
     else:
        self.current_mode = self.mode_clair
        self.bouton_mode_nuit.config(text="Mode Nuit")
    
     # Applique les nouvelles couleurs après la bascule
     self.apply_mode()

        
    def apply_mode(self):
        # Applique les couleurs à tous les widgets
         self.root.configure(bg=self.current_mode["bg"])
         self.main_frame.configure(bg=self.current_mode["bg"])
         self.frame_ajout.configure(bg=self.current_mode["bg"], fg=self.current_mode["fg"])
         self.frame_recherche.configure(bg=self.current_mode["bg"], fg=self.current_mode["fg"])
         self.frame_affichage.configure(bg=self.current_mode["bg"], fg=self.current_mode["fg"])

        # Met à jour les couleurs des boutons
         self.ajouter_bouton.config(bg=self.current_mode["button_bg"], fg=self.current_mode["button_fg"])
         self.bouton_mode_nuit.config(bg=self.current_mode["button_bg"], fg=self.current_mode["button_fg"])
         self.rechercher_bouton.config(bg=self.current_mode["button_bg"], fg=self.current_mode["button_fg"])
         self.afficher_bouton.config(bg=self.current_mode["button_bg"], fg=self.current_mode["button_fg"])

        # Met à jour les couleurs des labels et des champs de texte
         for widget in self.main_frame.winfo_children():
            if isinstance(widget, tk.Label) or isinstance(widget, tk.Entry):
                widget.config(bg=self.current_mode["bg"], fg=self.current_mode["fg"])



    # Méthodes pour afficher les résultats ou des messages d'erreur

    # Efface les résultats précédemment affichés dans le tableau (Treeview)
    def afficher_resultats(self, resultats):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for ligne in resultats:
            self.tree.insert("", "end", values=ligne)



    # Affichent des fenêtres de message 
    def afficher_message(self, titre, message):
        messagebox.showinfo(titre, message)

    def afficher_erreur(self, titre, message):
        messagebox.showerror(titre, message)
