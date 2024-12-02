from lib.calculator import Calculator

def get_float_input(prompt):
    """Demander un nombre à l'utilisateur et vérifier si c'est valide"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Erreur : veuillez entrer un nombre valide.")

def get_int_input(prompt):
    """Demander un entier à l'utilisateur et vérifier si c'est valide"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Erreur : veuillez entrer un entier valide.")

def menu():
    calc = Calculator()
    while True:
        print("\n----- Menu -----")
        print("1. Addition de deux nombres")
        print("2. Soustraction de deux nombres")
        print("3. Multiplication de deux nombres")
        print("4. Division de deux nombres")
        print("5. Moyenne d'une liste de nombres")
        print("6. Ecart-type d'une liste de nombres")
        print("7. Statistiques d'une liste de nombres")
        print("8. Quitter le programme")
        
        choice = get_int_input("Choisissez une option (1-8): ")

        if choice == 1:
            a = get_float_input("Entrez le premier nombre: ")
            b = get_float_input("Entrez le deuxième nombre: ")
            print("Résultat de l'addition:", calc.add(a, b))
        elif choice == 2:
            a = get_float_input("Entrez le premier nombre: ")
            b = get_float_input("Entrez le deuxième nombre: ")
            print("Résultat de la soustraction:", calc.subtract(a, b))
        elif choice == 3:
            a = get_float_input("Entrez le premier nombre: ")
            b = get_float_input("Entrez le deuxième nombre: ")
            print("Résultat de la multiplication:", calc.multiply(a, b))
        elif choice == 4:
            a = get_float_input("Entrez le numérateur: ")
            b = get_float_input("Entrez le dénominateur: ")
            try:
                print("Résultat de la division:", calc.divide(a, b))
            except ValueError as e:
                print(f"Erreur: {e}")
        elif choice == 5:
            numbers = get_numbers_from_user()
            print("Moyenne:", calc.mean(numbers))
        elif choice == 6:
            numbers = get_numbers_from_user()
            print("Ecart-type:", calc.standard_deviation(numbers))
        elif choice == 7:
            numbers = get_numbers_from_user()
            stats = calc.summary_statistics(numbers)
            print("Statistiques:", stats)
        elif choice == 8:
            print("Au revoir! Madame 😊")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

def get_numbers_from_user():
    """Demander une liste de nombres à l'utilisateur et gérer les erreurs"""
    while True:
        try:
            numbers = input("Entrez une liste de nombres séparés par des espaces: ")
            numbers = [float(num) for num in numbers.split()]
            return numbers
        except ValueError:
            print("Erreur : veuillez entrer uniquement des nombres séparés par des espaces.")

if __name__ == "__main__":
    menu()
