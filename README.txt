1 :
    Historique liste double chainée
    - de quoi voir la dernière commande rentrée :
        (ORAL) Toutes commandes visibles via index ($V index)
    - de quoi voir toutes les commandes rentrée par un utilisateur depuis sa première connexion :
        (ORAL) Toutes commandes users visibles via pseudo ($VA pseudo)
    - de quoi se déplacer dans cet historique (en avant et en arrière) :
        (ORAL) Fleches pour deplacer 1 par 1 en index ou directement aux messages precedent ou suivant d'un meme utilisateur
    - de quoi vider l'historique :
        (ORAL) Commande $C pour admin

3 :
    Via un arbre binaire ou non, créer un système de discution permettant de faire un questionnaire à l'utilisateur. L'utilisateur pourra appeler une commande "help" permettant de
    lancer la conversation et le bot tentera de définir son besoin en lui posant une série de questions prédéfinies, à la fin de la conversation une réponse sera donné au besoin.
    les sujets que devra aborder sont libre :
        Commande $HELP
    - "reset" : permettra de recommencer la discution
        Reset auto quand $HELP
    - "speak about X" : permettra de savoir si un sujet est traité par le bot ou non (exemple : speak about python dira si oui ou non le bot parle de python)
        Commande $SA

5 :
    Trouver une solution afin que lorsque que le bot s'arrête ses données stockées dans les différentes structures et collections crées précédement se soient pas perdues.
    Vous êtes libre d'utiliser ce que vous voulez pour stocker les données, un fichier texte, un fichier Json, une base de données ...
        (ORAL) Fichier list.json avec save auto dans quit()

6 :
    Pour avoir les points restants, vous êtes libre de rajouter toutes les fonctionnalités que vous voulez à votre bot discord.
        - Sécu role admin sur certaines commandes
        - Commande $S pour save manuel de l'historique
        - Commande $DOG pour image de chien alleatoire (api)
        - Fichier json téléchargeable dans le bot ($DL)