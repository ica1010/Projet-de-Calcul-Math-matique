def mean(numbers):
    """Calcule la moyenne d'une liste de nombres."""
    return sum(numbers) / len(numbers)

def standard_deviation(numbers):
    """Calcule l'écart-type d'une liste de nombres."""
    avg = mean(numbers)
    # Calcul de la variance
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    
    # Calcul de la racine carrée sans utiliser math.sqrt()
    sqrt_variance = variance ** 0.5
    return sqrt_variance

def summary_statistics(numbers):
    """Retourne un résumé statistique : moyenne et écart-type."""
    return {
        "mean": mean(numbers),
        "standard_deviation": standard_deviation(numbers),
    }
