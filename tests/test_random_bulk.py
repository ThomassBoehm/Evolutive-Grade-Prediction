from  ga import GradeGeneticAlgorithm 
import random
def test_ga_silent(i):
    approved = 0
    reproved = 0
    impossible = 0
    reproved_solutions = []

    for test_num in range(i):
        current_tests = [round(random.uniform(3, 10) * 2) / 2 for _ in range(random.randint(0, 4))]
        current_assignments = [round(random.uniform(3, 10) * 2) / 2 for _ in range(random.randint(0, 4))]

        num_remaining_tests = max(1, 4 - len(current_tests))
        num_remaining_assignments = max(1, 4 - len(current_assignments))

        test_weight = random.uniform(0.3, 0.7)
        assignment_weight = 1.0 - test_weight

        target_average = round(random.uniform(6,9)*2)/2

        ga = GradeGeneticAlgorithm(
            current_tests=current_tests,
            current_assignments=current_assignments,
            num_remaining_tests=num_remaining_tests,
            num_remaining_assignments=num_remaining_assignments,
            test_weight=test_weight,
            assignment_weight=assignment_weight,
            target_average=target_average,
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

        if final_avg - target_average >= -0.05:
            approved += 1
        elif (target_average - final_avg > 0.05) and all(grade == 10.0 for grade in solution['tests'] + solution['assignments']):
            impossible += 1
        else:
            reproved += 1
            reproved_solutions.append((current_tests, current_assignments, solution, target_average, final_avg))
        # Progresso
        if (test_num + 1) % 10 == 0:
            print(f"Progresso: {test_num + 1}/{i} testes concluídos")

    print(f"\n{'='*60}")
    print(f"✅ APROVADOS: {approved}/{i} ({approved/i*100:.1f}%)")
    print(f"❌ REPROVADOS: {reproved}/{i} ({reproved/i*100:.1f}%)")
    print(f"⚠️ IMPOSSÍVEIS: {impossible}/{i} ({impossible/i*100:.1f}%)")
    print('OBS: Considera-se impossível quando a solução encontrada atinge todas as notas máximas (10.0) e ainda assim não alcança a média alvo.')
    print('='*60)
    for i in range(reproved):
        print(f"\n--- REPROVAÇÃO {i+1} ---")
        print("Testes atuais:", reproved_solutions[i][0])
        print("Atribuições atuais:", reproved_solutions[i][1])
        print("Solução encontrada:", reproved_solutions[i][2])
        print("Média alvo:", reproved_solutions[i][3])
        print("Média final:", reproved_solutions[i][4])

test_ga_silent(100)