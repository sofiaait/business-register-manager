import mysql.connector
from mysql.connector import Error


class Model:
    def __init__(self):
        #Établir une connexion à la base de données registre_commerce 
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root", 
                password="", 
                database="registre_commerce" 
            )
            #Crée un objet curseur pour exécuter des requêtes SQL
            self.cursor = self.conn.cursor()
            print("Connexion réussie à la base de données.")
        # Capture les erreurs    
        except Error as e:
            print(f"Erreur de connexion à la base de données : {e}")
            raise


    #Méthode pour insérer une nouvelle entreprise dans la table entreprises
    def ajouter_entreprise(self, data):
        query = """
        INSERT INTO entreprises (Nom_Entreprise, Num_Registre, Adresse, Email, Telephone, Date_Inscription, Secteur_Activite)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        try:
            self.cursor.execute(query, data)
            self.conn.commit() # Applique les changements à la base de données
        except Error as e:
            print(f"Erreur lors de l'ajout de l'entreprise : {e}")
            raise


    # Méthode pour rechercher des entreprises en fonction d’un critère (Nom entreprise ou Num registre)
    def rechercher_entreprise(self, critere):
      # Déclarer une requête SQL qui recherche les entreprises dont le nom ou le numéro de registre contient la valeur donnée
      query = """
      SELECT * FROM entreprises
      WHERE Nom_Entreprise LIKE %s OR Num_Registre LIKE %s
      """
      try:
        self.cursor.execute(query, (f"%{critere}%", f"%{critere}%"))
        return self.cursor.fetchall() # Récupère et retourne toutes les lignes correspondantes
      except Error as e:
        print(f"Erreur lors de la recherche : {e}")
        return []


    # Méthode pour lire toutes les entreprises de la table
    def lire_entreprises(self):
      query = "SELECT * FROM entreprises"
      try:
        self.cursor.execute(query)
        return self.cursor.fetchall()
      except Error as e:
        print(f"Erreur lors de la lecture des entreprises : {e}")
        return []
