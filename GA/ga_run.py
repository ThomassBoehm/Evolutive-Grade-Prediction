from ga.py import GradeGeneticAlgorithm

# ===== EXEMPLOS DE USO =====
if __name__ == "__main__":
    print("="*60)
    
    
    ga1 = GradeGeneticAlgorithm(
        current_tests=[5.0, 5.6, 7.0],
        current_assignments=[7, 5, 2],
        num_remaining_tests=1,
        num_remaining_assignments=1,
        test_weight=0.6,
        assignment_weight=0.4,
        target_average=6,
        max_grade=10.0,
        population_size=150,
        generations=500
    )

    print("Executando Algoritmo Genético...")
    solution1, fitness1 = ga1.run()
    final1 = ga1.display_results(solution1)