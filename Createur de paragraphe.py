# -*- coding: utf-8 -*-
# creator 

import random

class GroupeNominal:
    def __init__(self, texte):
        self.texte = texte.lower()

class Phrase:
    def __init__(self, groupe_nominal):
        self.groupe_nominal = groupe_nominal

class Pave:
    def __init__(self, phrases):
        self.phrases = phrases

    def afficher(self):
        for phrase in self.phrases:
            for groupe_nominal in phrase.groupe_nominal:
                print(groupe_nominal.texte, end=' ')
            print()

def generer(sticker=False):
    def lire_mots_de_fichier(filename):
        with open(filename, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file]

    filenames = [
        "phrase1\\gp1.txt",
        "phrase1\\gp2.txt",
        "phrase1\\gp3.txt",
        "phrase2\\gp1.txt",
        "phrase2\\gp2.txt",
        "phrase2\\gp3.txt",
        "phrase2\\gp4.txt",
        "phrase3\\gp1.txt",
        "phrase3\\gp2.txt",
        "phrase3\\gp3.txt",
        "phrase3\\gp4.txt",
        "phrase4\\gp1.txt",
        "phrase4\\gp2.txt",
        "phrase4\\gp3.txt",
        "phrase4\\gp4.txt",
        "phrase4\\gp5.txt",
        "phrase4\\gp6.txt",
        "phrase5\\gp1.txt",
        "phrase5\\gp2.txt",
        "phrase5\\gp3.txt",
    ]
    
    if sticker:
        filenames.append("stickers\\stickers.txt")
    
    phrases = []
    paragraph_count = 0  # Compteur de paragraphes
    max_paragraphs = 10  # Nombre maximal de paragraphes paragraphe
    lines_in_paragraph = 0  # Compteur de lignes dans le paragraphe
    max_lines_per_paragraph = 10  # Nombre maximal de lignes par paragraphe
    
    for filename in filenames:
        mots = lire_mots_de_fichier(filename)
        groupe_nominal = [GroupeNominal(random.choice(mots)) for _ in range(1)]
        
        # Vérifiez si vous avez atteint le nombre maximal de lignes par paragraphe
        if lines_in_paragraph >= max_lines_per_paragraph:
            paragraph_count += 1
            lines_in_paragraph = 0
        
        # Vérifiez si vous avez atteint le nombre maximal de paragraphes
        if paragraph_count >= max_paragraphs:
            break
        
        phrases.append(Phrase(groupe_nominal))
        lines_in_paragraph += 1
    
    pave = Pave(phrases)
    pave.afficher()

def main():
    for _ in range(1):
        generer(sticker=False)
        print("\n\n\n")

if __name__ == "__main__":
    main()

input("Appuyez sur Entrée pour quitter...")