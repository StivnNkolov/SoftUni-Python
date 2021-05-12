all_electrons = int(input())

distribution = []
shell = 1

while all_electrons > 0:
    electrons_for_shell = 2 * (shell ** 2)
    if all_electrons < electrons_for_shell:
        distribution.append(all_electrons)
        break
    else:
        distribution.append(electrons_for_shell)
    shell += 1
    all_electrons -= electrons_for_shell
print(distribution)