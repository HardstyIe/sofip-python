print("""
1.    Ajouter un livre à la bibliothèque.
2.    Supprimer un livre de la bibliothèque.
3.    Rechercher un livre par titre.
4.    Afficher tous les livres.
5.    Trier les livres par titre.
""")
valeur = int(input("Faire votre choix:"))

tableau=[{}]



def Librairie(valeur):
        if valeur == 1:
            nom = input("Quel est le nom de votre livre :")
            tableau.append(nom)
            print(f"Livre Ajouté a la liste: {nom}")

        elif valeur == 2:
            nom = input("Quel est le livre a supprimé ? :")
            if nom in tableau:   
              confirmation = print(f"{nom} se trouve bien la liste , voulez-vous continuer ? Y/N").lower()
              if (confirmation == "y"):
                  if (nom == tableau[nom]):
                      reponse = input(f"êtes-vous sur de vouloir supprimer : {nom} . Y/N").lower()
                      if (reponse == 'y') :
                          tableau.pop(nom)
                          print(f"{nom} a été supprimer de la liste")
                      else :
                          print(f"{nom} n'a pas été supprimer de la liste")
        








Librairie(valeur)
