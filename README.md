Biblioteques API 
Installation des Dépendances
Python 3.10.0
pip 21.3.1 from C:\Users\hp\AppData\Local\Programs\Python\Python310\lib\site-packages\pip (python 3.10)
Suivez les instructions suivantes pour installer l'ancienne version de python sur la plateforme python docs

Dépendances de PIP

pip install -r requirements.txt
or
pip3 install -r requirements.txt
Nous passons donc à l'installation de tous les packages se trouvant dans le fichier requirements.txt.

SQLAlchemy est un toolkit open source SQL et un mapping objet-relationnel écrit en Python et publié sous licence MIT. SQLAlchemy a opté pour l'utilisation du pattern Data Mapper plutôt que l'active record utilisés par de nombreux autres ORM

Démarrer le serveur
Pour démarrer le serveur sur Linux ou Mac, executez:

export FLASK_APP=app.py
export FLASK_ENV=development
flask run
Pour le démarrer sur Windows, executez:

set FLASK_APP=app.py
set FLASK_ENV=development
flask run
API REFERENCE
Getting starter

Type d'erreur
Les erreurs sont renvoyées sou forme d'objet au format Json: { "success":False "error": 400 "message":"Ressource non disponible" }

L'API vous renvoie 4 types d'erreur: . 400: Bad request ou ressource non disponible . 500: Internal server error . 422: Unprocessable . 404: Not found

Endpoints
. ## GET/livres

GENERAL:
    Cet endpoint retourne la liste des objets livres, la valeur du succès et le total des livres. 

    
EXEMPLE: curl http://localhost:5000/Livres
       
        {
    "Livres": [
        {
            "auteur": "Divine",
            "categorie_id": 9,
            "date_publication": "Fri, 30 Oct 1992 00:00:00 GMT",
            "editeur": "Larousse",
            "id": 6,
            "isbn": "01-02",
            "titre": "Magie blanche"
        },
        {
            "auteur": "Francky",
            "categorie_id": 7,
            "date_publication": "Sat, 03 Jan 2015 00:00:00 GMT",
            "editeur": "Larousse",
            "id": 7,
            "isbn": "01-03",
            "titre": "Boule*-boule"
        },
        {
            "auteur": "Berg",
            "categorie_id": 2,
            "date_publication": "Fri, 14 Feb 2020 00:00:00 GMT",
            "editeur": "Teletoon",
            "id": 9,
            "isbn": "20-07",
            "titre": "Kaeloo"
        },
        {
            "auteur": "Modus",
            "categorie_id": 1,
            "date_publication": "Thu, 31 Dec 2020 00:00:00 GMT",
            "editeur": "Modus",
            "id": 1,
            "isbn": "966-669",
            "titre": "Baiser sans"
        },
        {
            "auteur": "Modus",
            "categorie_id": 1,
            "date_publication": "Thu, 31 Dec 2020 00:00:00 GMT",
            "editeur": "Romuald",
            "id": 5,
            "isbn": "65-89",
            "titre": "Baiser sans"
        },
        {
            "auteur": "Modus",
            "categorie_id": 1,
            "date_publication": "Thu, 31 Dec 2020 00:00:00 GMT",
            "editeur": "Syfy",
            "id": 10,
            "isbn": "8-07",
            "titre": "Baiser sans"
        },
        {
            "auteur": "Modus",
            "categorie_id": 1,
            "date_publication": "Thu, 31 Dec 2020 00:00:00 GMT",
            "editeur": "Teletoon",
            "id": 8,
            "isbn": "20-07",
            "titre": "Baiser sans"
        },
        {
            "auteur": "bro",
            "categorie_id": 2,
            "date_publication": "Sat, 14 Nov 2015 00:00:00 GMT",
            "editeur": "Viven",
            "id": 4,
            "isbn": "966-669",
            "titre": "Elle aime sa mère"
        }
    ],
    "success": true,
    "total_livres": 8
}
.##GET/livres(Livres_id) GENERAL: Cet endpoint permet de récupérer les informations d'un livre particulier s'il existe par le biais de l'ID.

EXEMPLE: http://localhost:5000/Livres/7
    {
    "auteur": "Francky",
    "categorie_id": 7,
    "date_publication": "Sat, 03 Jan 2015 00:00:00 GMT",
    "editeur": "Larousse",
    "id": 7,
    "isbn": "01-03",
    "titre": "Boule*-boule"
}
. ## DELETE/livres (Livres_id)

GENERAL:
    Supprimer un element si l'ID existe. Retourne l'ID du livre supprimé, la valeur du succès et le nouveau total.

    EXEMPLE: curl -X DELETE http://localhost:5000/Livres/4
    {
        "id_Livres": 4,
        "new_total": 3,
        "success": true
    }
. ##PATCH/livres(Livres_id) GENERAL: Cet endpoint permet de mettre à jour, le titre, l'auteur, et l'éditeur du livre. Il retourne un livre mis à jour.

EXEMPLE.....Avec Patch

  {
      "auteur": "Azychika, Takumi Fukui",
      "code_ISBN": "979-1-0327",
      "date_publication": "03-02-2022",
      "editeur": "Ki-oon",
      "id": 1,
      "titre": "Jujutsu Kaisen"
  }
  ```

. ## GET/categories

  GENERAL:
      Cet endpoint retourne la liste des categories de livres, la valeur du succès et le total des categories disponibles. 
  
      
  EXEMPLE: curl http://localhost:5000/categories

    {
    "Categorie": [
        {
            "id": 2,
            "libelle_categorie": "Physiques et chimie"
        },
        {
            "id": 1,
            "libelle_categorie": "Maths"
        },
        {
            "id": 6,
            "libelle_categorie": "Policier"
        },
        {
            "id": 7,
            "libelle_categorie": "Drame"
        },
        {
            "id": 8,
            "libelle_categorie": "Herotique"
        },
        {
            "id": 9,
            "libelle_categorie": "Fiction"
        },
        {
            "id": 10,
            "libelle_categorie": "Romantique"
        }
    ],
    "success": true,
    "total_categories": 7
}
.##GET/categories(categorie_id) GENERAL: Cet endpoint permet de récupérer les informations d'une categorie si elle existe par le biais de l'ID.

EXEMPLE: http://localhost:5000/categories/6
    {
        "categorie": "Cuisine",
        "id": 6
    }
. ## DELETE/categories (categories_id)

GENERAL:
    Supprimer un element si l'ID existe. Retourne l'ID da la catégorie supprimé, la valeur du succès et le nouveau total.

    EXEMPLE: curl -X DELETE http://localhost:5000/categories/11
    {
        "id_cat": 11,
        "new_total": 10,
        "status": 200,
        "success": true
    }
. ##PATCH/categories(categorie_id) GENERAL: Cet endpoint permet de mettre à jour le libelle ou le nom de la categorie. Il retourne une nouvelle categorie avec la nouvelle valeur.

EXEMPLE.....Avec Patch

  {
      "categorie": "Bandes Dessinées",
      "id": 4
  }

.##GET/livres/categories(categorie_id)
GENERAL:
Cet endpoint permet de lister les livres appartenant à une categorie donnée.
Il renvoie la classe de la categorie et les livres l'appartenant.

  EXEMPLE: http://localhost:5000/categories/4/livres
{
"Status_code": 200,
"Success": true,
"livres": [
    {
        "auteur": "Gege Atakumi",
        "code_ISBN": "979-1-0328",
        "date_publication": "03-02-2022",
        "editeur": "Ki-oon",
        "id": 2,
        "titre": "Jujutsu Kaisen T13"
    },
    {
        "auteur": "Azychika, Takumi Fukui",
        "code_ISBN": "979-1-0327",
        "date_publication": "03-02-2022",
        "editeur": "Ki-oon",
        "id": 1,
        "titre": "Jujutsu Kaisen"
    }
],
"classe": {
    "categorie": "Bandes Dessinées",
    "id": 4
}
}
