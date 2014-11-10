Procédure de démarrage
==================

#Matériel

## Emprunté à la tech-shop

* Haut-parleurs directif + ampli
* Mini-pc + alim
* Capteur ultrason + arduino


#Procédure d'installation

## Mise en place matériel

### Horloge pointeuse

L'horloge pointeuse nécessite le matériel suivant :

- Les haut-parleurs directif
   - Une paire de haut-parleur directifs
   - L'ampli associé
- Un lecteur mp3
- Ensemble de capteur:
   - Un capteur ultra-son branché sur ..
   - Un arduino (avec son cable usb)
- Un mimi pc
- Une enceinte audio et son cable jack


Il y a deux système indépendant :
- Les haut-parleurs directif et le lecteur mp3 qui jouent les "tic-tac" en continue.
- Le mini-pc, capteurs, enceinte audio, qui jouent le dialogue lorsqu'un visiteur s'approche.

#### Mise en place du "tic-tac"

- (Trouver un lecteur audio, y installer le son tic_tac.wav)
- Brancher les haut-parleurs directifs au lecteur mp3.
- Lancer le son sur le lecteur mp3.
- S'assurer que le son est joué en boucle.


#### Mise en place du dialogue

- Brancher l'arduino au mini-pc à l'aide du cable usb.
- Brancher l'enceinte sur le mini-pc (prise verte)
- Allumer le mini-pc. Attendre qu'il ai démarré (2/3 min)
- S'approcher du capteur pour s'assure que le son est correctement joué.




## Information technique.

Ces informations sont purement indicatives. Toute la partie "informatique" est automatisée.
Ces informations seront principalement nécessaire à quelqu'un voulant modifier le système.

- Le mini-pc tourne sur fedora 20.
- Le mdp root est azerty.
- L'utilisateur principal est "vacarme", il n'y a pas de mdp.

- L'arduino envoie les informations des capteurs sur un port serie via le cable usb.
- Le script python input2sound.py lit le port série et joue le son en fonction de la distance mesurée.
- L'utilisateur lançant le script input2sound.py (vacarme dans notre cas) doit être dans le group "dialout".
- Le script est automatiquement lancé au démmarage grace à un script systemd.



