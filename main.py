import random
from telegram import Update
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater, CallbackContext
from youtubesearchpython import VideosSearch

BOT_TOKEN = '6603185267:AAFEVtH7-VPVcJV5kS08vO0FTX6AQT-KVU8'

# Liste des blagues


blagues_responses = [
    "Quelle mamie fait peur aux voleurs ?\nMamie Traillette.",
    "Pourquoi est-ce si difficile de conduire dans le Nord ?\nParce que les voitures n’arrêtent pas de caler. ("
    "Pas-de-Calais)",
    "Pourquoi est-ce qu'on dit que les bretons sont tous frères et sœurs ?\nParce qu’ils n’ont Quimper.",
    "Que faisaient les dinosaures quand ils n'arrivaient pas à se décider?\nDes tirageosaures.",
    "Pourquoi est-ce qu'il faut mettre tous les crocos en prison ?\nParce que les crocos dealent.",
    "Comment fait-on pour allumer un barbecue breton ?\nOn utilise des breizh.",
    "Pourquoi dit-on que les poissons travaillent illégalement ?\nParce qu’ils n’ont pas de FISH de paie.",
    "Pourquoi est-ce que les mexicains mangent-ils aux toilettes ?\nParce qu’ils aiment manger épicé. (et pisser)",
    "Qu'est-ce qu'un tennisman adore faire ?\nRendre des services.",
    "Pourquoi est-ce que les vêtements sont toujours fatigués quand ils sortent de la machine ?\nParce qu’ils sont "
    "lessivés.",
    "Pourquoi est-ce que les livres ont-ils toujours chaud ?\nParce qu’ils ont une couverture.",
    "Où est-ce que les super-héros vont-ils faire leurs courses ?\nAu supermarché.",
    "Que se passe-t-il quand 2 poissons s'énervent ?\nLe thon monte.",
    "Quel fruit est assez fort pour couper des arbres ?\nLe citron.",
    "Quel est le jambon que tout le monde déteste ?\nLe sale ami.",
    "Que fait un cendrier devant un ascenseur ?\nIl veut des cendres.",
    "Que dit une imprimante dans l'eau ?\nJ’ai papier.",
    "Quel est l'aliment le plus hilarant ?\nLe riz.",
    "Quel est le sport préféré des insectes ?\nLe cricket.",
    "Pourquoi les girafes n'existent pas ?\nParce que c’est un coup monté.",
    "Pourquoi est-ce que Hulk a un beau jardin ?\nParce qu’il a la main verte.",
    "C'est deux fous qui marchent dans la rue\nLe premier demande au second : « je peux me mettre au milieu ? »",
    "Comment est-ce que les abeilles communiquent entre elles ?\nPar e-miel.",
    "Quel est l'arbre préféré des chômeurs ?\nLe bouleau.",
    "Que dit-on d'une fleur qui a eu zéro à son contrôle ?\nQu’elle s’est plantée.",
    "Comment appelle-t-on un jeudi vraiment nul ?\nUne trajeudi.",
    "Que fait un employé de chez Sephora à sa pause clope ?\nIl parfumer.",
    "Qu'est-ce qu'une frite enceinte ?\nUne patate sautée.",
    "Qu'est ce qu'une lampe moche ?\nUn LEDron.",
    "Est-ce qu'une poule peut parler anglais ?\nYes chicken. (she can)",
    "Qui vit dans les tavernes ?\nLes hommes de bières.",
    "Quelle est la danse préférée des chats ?\nLe cha cha cha.",
    "Qu'est ce qu'une carotte dans une flaque d'eau ?\nUn bonhomme de neige en été.",
    "Pourquoi est-ce que les bières sont toujours stressées ?\nParce qu’elles ont la pression.",
    "Quelle princesse a les lèvres gercées ?\nLabello bois dormant.",
    "Pourquoi est ce que les poissons n'ont plus de maison ?\nParce qu’on les a des truites.",
    "Pourquoi est ce que le lapin est bleu ?\nParce qu’on l’a peint.",
    "Pourquoi est ce que Potter est triste ?\nParce que personne Harry à sa blague.",
    "Comment appelle-t-on un combat entre un petit pois et une carotte ?\nUn bon duel.",
    "Pourquoi est-ce que les éoliennes n'ont pas de copain ?\nParce qu’elles se prennent toujours des vents.",
    "D'où viennent les gens les plus dangereux ?\nD’Angers.",
    "Qu'est ce qu'un cadeau qui s'en va ?\nUne surprise party.",
    "Quelle est la fée que les enfants détestent ?\nLa fessée.",
    "Quel poisson n'a pas de certificat de naissance ?\nLe poisson pané.",
    "Quel est le médecin qui nous fait tous craquer ?\nL’ostéo.",
    "Quel est le super héros qui a tout le temps peur ?\nLe super-sticieux.",
    "Pourquoi est-ce que les chercheurs ont-ils des trous de mémoire ?\nParce qu’ils se creusent la tête.",
    "Comment les musiciens choisissent-ils leur parquet ?\nIls choisissent un parquet facile à cirer. (Fa Si La Si Ré)",
    "Quel est le musicien préféré des maladies ?\nBach-terie.",
    "Quel est le réseau préféré des pêcheurs ?\nTruiteur.",
    "Que fait un geek quand il a peur ?\nIl URL.",
    "Quel est le carburant le plus détendu ?\nLe kérozen.",
    "Quel est le fast food préféré de Flash ?\nQuick.",
    "Qu'est-ce qui est vert et qui se déplace sous l'eau ?\nUn chou marin.",
    "Quel est le pays le plus cool du monde ?\nLe Yééémen.",
    "Que fait une vache quand elle ferme les yeux ?\nDu lait concentré.",
    "Quel est le super héros qui donne l'heure le plus vite ?\nSpiderman. (Speed heure man)",
    "Pourquoi est-ce que les anges sont sourds ?\nParce que Jésus crie. (Jésus Christ)",
    "Quel est le fruit préféré des profs d'histoire ?\nLes dattes.",
    "Quelle est la déesse de l'internet ?\nL’ADSL. (La déesse L)",
    "Qu'est-ce qui est pire que le vent ?\nUn vampire.",
    "Quelle est l'arme préférée des vegan ?\nLe lance roquette.",
    "Quelle est la femme du hamster ?\nL’Amsterdam.",
    "Dans quel pays ne bronze-t-on pas du nez ?\nAu Népal.",
    "Que fait une théière devant un ascenseur ?\nElle veut mon thé.",
    "Pourquoi est-ce que Winnie l'Ourson veut absolument se marier ?\nPour partir en lune de miel.",
    "Que dit une mère à son fils geek quand le dîner est servi ?\nAlt Tab !",
    "Quelle est la meilleure heure pour écouter de la musique ?\nDeezer !",
    "Que fait un geek quand il descend du métro ?\nIl libère la RAM.",
    "Quel est l'animal le plus connecté ?\nLe porc USB.",
    "Où vont les biscottes pour danser ?\nEn biscothèque.",
    "Quel est le style musical préféré des médecins ?\nLe blouse.",
    "Comment appelle-t-on un chat qui va dans l'espace ?\nUn chatellite.",
    "Que fait un jardinier quand il ment ?\nIl raconte des salades.",
    "Où est-ce que l'homme invisible part en vacances ?\nChez ses transparents.",
    "Pourquoi est-ce que Napoléon n'a pas voulu acheter de maison ?\nParce qu’il avait déjà un Bonaparte.",
    "Que dit Frodon devant sa maison ?\nC’est là que j’hobbit.",
    "Quels sont les fruits qu'on trouve dans toutes les maisons ?\nDes coings et des mûres.",
    "Pourquoi un chasseur emmène-t-il son fusil aux toilettes ?\nPour tirer la chasse.",
    "Quel est le crustacé le plus léger de la mer ?\nLa palourde.",
    "Que dit un informaticien quand il s'ennuie ?\nJe me fichier.",
    "Avec quelle monnaie les marins payent-ils ?\nAvec des sous marins.",
    "Que dit un italien pour dire au revoir ?\nPasta la vista.",
    "Où va Messi quand il se blesse ?\nÀ la pharmessi.",
    "Que demande un footballeur à son coiffeur ?\nLa coupe du monde s’il vous plaît.",
    "Que dit un rappeur lorsqu'il rentre dans une fromagerie ?\nFaites du briiiie !",
    "Que dit une lampe lorsqu'elle a un problème ?\nElle crie « à LED ! »",
    "Quelle est la viande préférée des Russes ?\nLe steak tsar tsar.",
    "Quel est le poisson le moins cher ?\nLe requin marteau : il ne vaut pas un clou.",
    "Qu'est-ce qu'un hamster dans l'espace ?\nUn hamstéroïde.",
    "Comment appelle-t-on deux canards qui se disputent ?\nUn conflit de canards.",
    "Pourquoi est-ce que les moutons aiment le chewing-gum ?\nParce que c’est bon pour l’haleine. (la laine)",
    "Pourquoi les cordonniers sont-ils curieux ?\nParce qu’ils se mêlent de tout. (semelle)",
    "Que dit le citron quand il braque une banque ?\n« Pas un zeste, ze suis pressé ! »",
    "Comment appelle-t-on une manifestation d'aveugles ?\nUn festival de cannes.",
    "Que risque-t-on à lancer de l'ail sur un mur ?\nLe retour du jet d’ail.",
    "Quelle est la fée la plus paresseuse ?\nLa fée Néante.",
    "Que dit une noisette qui tombe à l'eau ?\n« Au secours, je me noix ! »",
    "Tu connais l'histoire de l'armoire ?\nElle est pas commode.",
    "Tu connais l'histoire de la feuille de papier ?\nElle déchire !",
    "Comment appelle-t-on un chat tout-terrain ?\nUn cat cat."

]


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Bienvenue dans ce bot !\nCommandes:\nclip ... : Pour vous generer le lien du clip sur '
                              'youtube'
                              'opérations\n/blague : Pour vous raconter une blague')


def blague(update: Update, context: CallbackContext) -> None:
    nomre_aleatoire = random.randint(0, 101)
    blague_reponse = f"{blagues_responses[nomre_aleatoire]}"
    update.message.reply_text(blague_reponse)


def youtubeVideo(query):
    videosSearch = VideosSearch(query, limit=1)
    for i in videosSearch.result().values():
        for j in i:
            return f'<iframe width="560" height="315" src="{j["link"]}" frameborder="0" allowfullscreen></iframe>'


def handle_text(update: Update, context: CallbackContext) -> None:
    user_input = update.message.text
    response = process_user_input(user_input)  # Remplacez par votre logique de traitement
    update.message.reply_text(response)


def process_user_input(user_input: str) -> str:
    if "clip" in user_input.lower():
        return youtubeVideo(user_input)
    else:
        return "Commande non reconnu"


def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Ajoutez un gestionnaire de commande pour /start
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("blague", blague))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_text))

    updater.start_polling()  # Démarrez le bot
    updater.idle()  # Attendez que le bot soit arrêté proprement


if __name__ == '__main__':
    main()
