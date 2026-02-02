from ga import GradeGeneticAlgorithm

# ===== EXEMPLOS DE USO =====
if __name__ == "__main__":
    print("="*60)
    
    ##### EXEMPLO BÁSICO #####


    """
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
    print("="*60)
    print(" ")
    response = ga1.get_results_json(solution1)
    print(f"JSON Response: {response}")

"""


### EXEMPLO COM PESOS ESPECÍFICOS PARA CADA PROVA E TRABALHO ###


    ga2 = GradeGeneticAlgorithm(
        current_tests=[5.0, 5.6, 7.0],      # 3 provas feitas
        current_assignments=[7, 5, 2],       # 3 trabalhos feitos
        num_remaining_tests=1,               # 1 prova restante
        num_remaining_assignments=1,         # 1 trabalho restante
        test_weight=0.6,
        assignment_weight=0.4,
        target_average=6,
        spec_test_weight=[0.1, 0.2, 0.3, 0.4],           # 4 provas (3+1)
        spec_assignment_weight=[0.2, 0.3, 0.2, 0.3],     # 4 trabalhos (3+1)
        max_grade=10.0,
        population_size=150,
        generations=500
    )

    print("Executando Algoritmo Genético...")
    solution2, fitness2 = ga2.run()

    print(solution2)
    
    final2 = ga2.display_results(solution2)
    response2 = ga2.get_results_json(solution2)
    print(f"JSON Response: {response2}")
    