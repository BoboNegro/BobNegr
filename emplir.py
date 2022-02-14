from Nancy import Categorie, Livre, db
from datetime import datetime
import time
import random
for i in range(1,24):
    for j in range(2):
        titre = input(f"Veuillez entrer le titre de la categorie {i} :")
        auteur= input("Veuillez entrer le auteur de ce titre:")
        editeur = input("Veuillez entrer l'editeur de ce titre' :")
        date= input("veuillez entrer la date:")
        isbn=input("veuillez saisir le code isbn")
        livre=Livre(isbn,titre,date,auteur,editeur,i)
        db.session.add(livre)
        db.session.commit()
        
    
print("toute les insertions ont été faites")