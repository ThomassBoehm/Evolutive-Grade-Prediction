from ga.py import GradeGeneticAlgorithm
import random

def test_ga():
    # Gera dados aleatórios ANTES de criar a instância
    current_tests = [round(random.uniform(3, 10) * 2) / 2 for i in range(random.randint(0, 4))]
    current_assignments = [round(random.uniform(3, 10) * 2) / 2 for i in range(random.randint(0, 4))]

    # Calcula restantes
    num_remaining_tests = max(1, 4 - len(current_tests))
    num_remaining_assignments = max(1, 4 - len(current_assignments))

    # Gera pesos
    test_weight = random.uniform(0.3, 0.7)  # Entre 30% e 70%
    assignment_weight = 1.0 - test_weight

    print("=== CONFIGURAÇÃO DO TESTE ===")
    print(f"Provas atuais: {current_tests} (total: {len(current_tests)})")
    print(f"Trabalhos atuais: {current_assignments} (total: {len(current_assignments)})")
    print(f"Provas restantes: {num_remaining_tests}")
    print(f"Trabalhos restantes: {num_remaining_assignments}")
    print(f"Pesos: Provas {test_weight*100:.1f}% | Trabalhos {assignment_weight*100:.1f}%")
    print(f"Meta: 6.0\n")

    ga = GradeGeneticAlgorithm(
        current_tests=current_tests,
        current_assignments=current_assignments,
        num_remaining_tests=num_remaining_tests,
        num_remaining_assignments=num_remaining_assignments,
        test_weight=test_weight,
        assignment_weight=assignment_weight,
        target_average=6,
        max_grade=10.0,
        population_size=150,
        generations=500
    )

    print("Executando Algoritmo Genético...")
    solution, fitness = ga.run()
    ga.display_results(solution)

# Executa o teste
test_ga()