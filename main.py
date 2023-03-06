import sys
from termcolor import colored

# Liste de vos projets
projets = [
    {
        'nom': 'Fullbot',
        'description': 'Creation of a Discord bot to automate certain tasks related to content creators.',
        'lien': 'Private'
    },
    {
        'nom': 'Bot Telegram',
        'description': "Creation of a Telegram bot to send automated messages and interact with users.",
        'lien': 'Private'
    },
    {
        'nom': 'Scrapping d\'informations sur Pexels',
        'description': 'Automated retrieval of videos from Pexels.',
        'lien': 'https://github.com/Charles-84/Pexels-downloader'
    }
]

# Affichage des projets dans la console avec des couleurs
for projet in projets:
    nom = colored(projet['nom'], 'blue', attrs=['bold'])
    description = colored(projet['description'], 'white')
    lien = colored(projet['lien'], 'green', attrs=['underline'])

    print(f"{nom}\n{description}\nLien : {lien}\n")
