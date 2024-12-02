def get_number(prompt):
    """Demande un nombre à l'utilisateur avec gestion des erreurs."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Erreur : Veuillez entrer un nombre valide.")

def get_number_list(prompt):
    """Demande une liste de nombres avec gestion des erreurs."""
    while True:
        try:
            raw_input = input(prompt)
            numbers = list(map(float, raw_input.split()))
            if not numbers:
                raise ValueError("La liste ne peut pas être vide.")
            return numbers
        except ValueError as e:
            print(f"Erreur : {e}. Essayez à nouveau.")
