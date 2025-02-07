#!/usr/bin/python3
#!/usr/bin/python3
'''Module - 7-base_geometry: Définit une classe de base pour la géométrie.''' 

class BaseGeometry:
    '''Classe de base pour la géométrie, servant de modèle pour d'autres formes géométriques.'''

    def area(self):
        """Méthode qui lève une exception car elle n'est pas implémentée.
        Elle doit être redéfinie dans une sous-classe pour fournir une implémentation spécifique.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        Méthode qui valide si un paramètre est un entier strictement positif.
        
        Arguments:
        name (str): Le nom du paramètre (utilisé dans le message d'erreur).
        value (int): La valeur à vérifier.
        
        Exceptions:
        - TypeError: Levée si `value` n'est pas un entier.
        - ValueError: Levée si `value` est inférieur ou égal à 0.
        '''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
