#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Essaye de formater et d'imprimer la valeur comme un entier
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # Si une erreur survient (par ex., si ce n'est pas un entier), retourne False
        return False
