noms_articles = []
prix_articles = []
quantites_articles = []

for i in range(2):
    nom_article = input(f"Saisir le nom de l'article {i + 1} : ")
    prix_article = float(input(f"Saisir le prix de l'article {i + 1} : "))
    quantite_article = int(input(f"Saisir la quantité de l'article {i + 1} : "))

    noms_articles.append(nom_article)
    prix_articles.append(prix_article)
    quantites_articles.append(quantite_article)

montants_totaux = []
montant_total_facture = 0.0

for i in range(2):
    montant_ht = prix_articles[i] * quantites_articles[i]
    montant_ttc = montant_ht + (montant_ht * 0.2)
    montants_totaux.append(montant_ttc)
    montant_total_facture += montant_ttc

for i in range(2):
    print(f"\nDétails de l'article {i + 1}:")
    print(f"Nom : {noms_articles[i]}")
    print(f"Prix unitaire : {prix_articles[i]}")
    print(f"Quantité : {quantites_articles[i]}")
    print(f"Montant TTC : {montants_totaux[i]:.2f}")

print("\nMontant total de la facture :", montant_total_facture)
