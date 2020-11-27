import population as pop

# parameters (popoulation size, file, and seed() )
population = pop.population(5, "L4-5-5.txt", 1)
for x in population:
    print(x)