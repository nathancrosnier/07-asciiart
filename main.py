#### Imports et définition des variables globales
"""AAAAAAAA"""
import sys
sys.setrecursionlimit(10000)
#### Fonctions secondaires

def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée en argument 
    selon un algorithme itératif
    Args:
        s (str): la chaîne de caractères à encoder
    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    occ = []
    cmpt = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cmpt += 1
        else:
            occ.append((s[i-1],cmpt))
            cmpt = 1
    occ.append((s[-1], cmpt))
    return occ

def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne de caractères passée 
    en argument selon un algorithme récursif
    Args:
        s (str): la chaîne de caractères à encoder
    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    cmpt = 1
    while cmpt < len(s) and s[0] == s[cmpt]:
        cmpt += 1
    return [(s[0], cmpt)] + artcode_r(s[cmpt:])

#### Fonction principale

def main():
    """
    Tests
    """
    print(artcode_i("AAABBBCCCABC"))
    print(artcode_r("AAABBBCCCABC"))
    print(artcode_r("gggfhhhhhhggg"))

if __name__ == "__main__":
    main()
