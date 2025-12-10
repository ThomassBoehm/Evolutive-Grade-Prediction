from ga.py import GradeGeneticAlgorithm
import random
def test_ga_silent(i):
    approved = 0
    reproved = 0

    for test_num in range(i):
        current_tests = [round(random.uniform(3, 10) * 2) / 2 for _ in range(random.randint(0, 4))]
        current_assignments = [round(random.uniform(3, 10) * 2) / 2 for _ in range(random.randint(0, 4))]

        num_remaining_tests = max(1, 4 - len(current_tests))
        num_remaining_assignments = max(1, 4 - len(current_assignments))

        test_weight = random.uniform(0.3, 0.7)
        assignment_weight = 1.0 - test_weight

        ga = GradeGeneticAlgorithm(
            current_tests=current_tests,
            current_assignments=current_assignments,
            num_remaining_tests=num_remaining_tests,
            num_remaining_assignments=num_remaining_assignments,
            test_weight=test_weight,
            assignment_weight=assignment_weight,
            target_average=7,
            max_grade=10.0,
            population_size=150,
            generations=200  # Reduzido para velocidade
        )

        solution, _ = ga.run()

        all_tests = ga.current_tests + solution['tests']
        all_assignments = ga.current_assignments + solution['assignments']
        final_avg = ga.calculate_weighted_average(
            all_tests, all_assignments,
            ga.spec_test_weight, ga.spec_assignment_weight
        )

        if final_avg >= 5.95:
            approved += 1
        else:
            reproved += 1

        # Progresso
        if (test_num + 1) % 10 == 0:
            print(f"Progresso: {test_num + 1}/{i} testes concluídos")

    print(f"\n{'='*60}")
    print(f"✅ APROVADOS: {approved}/{i} ({approved/i*100:.1f}%)")
    print(f"❌ REPROVADOS: {reproved}/{i} ({reproved/i*100:.1f}%)")
    print('='*60)

test_ga_silent(100)