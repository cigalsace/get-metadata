# get-metadata

Python script to get remote XML files on HTML server and put them in a local directory.

## Objectif:

Récupérer une liste de fichier XML situés sur un serveur HTTP et les placer dans un dossier local.


## Fonctionnement:

L'application interroge une page HTML, récupère les liens disponibles et télécharge les fichiers correspondants.

Les points de téléchargement ou "noeuds" sont configurés dans des fichiers JSON stockés dans le dossier "nodes".
Chaque fichier peut contenir plusieurs noeuds.
Organisation recommandée: un fichier par organisme et un noeud de moissonnage par page HTML.
Pour désactiver un fichier, faire débuter son nom par un underscore "_".
Pour désactiver un noeud, mettre l'attribut "active" à la valeur "0".


## Fichier JSON de configuration:

Modèle de fichier JSON (avec commentaires):

{  
    "organisme": "Organism 1", # Nom de l'organisme concerné  
    "nodes": [  
        {  
            "description": "Harvesting node 1 of Org 1",        # Description du point de moissonage   
            "active": "1",                                      # Indique si le noeud est catif et sera moissoné  
            "src_domain": "http://my-domain.dom",               # Nom de domaine source  
            "src_path": "path/to/metadata/XML/",                # Chemin vers les fichiers à télécharger sur le serveur à partir du nom de domaine source  
            "dst_path": "xml/org-1/",                           # Chemin local cible (relatif ou absolu)  
            "pattern": "<a href=\"/%s.*?\"><tt>(.*?)</tt></a>"  # Pattern de récupération des noms de fichier sur la page HTML source  
        },  
        {  
            "description": "Empty harvesting node",  
            "active": "0",  
            "src_domain": "",  
            "src_path": "",  
            "dst_path": "",  
            "dst_path": "",  
            "pattern": ""  
        }  
    ]  
}  
