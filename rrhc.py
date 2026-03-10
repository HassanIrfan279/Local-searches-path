import random

# Zone values (Advantage Score)
values = {
"A":20,"B":28,"C":34,"D":42,"E":52,"F":58,"G":63,"H":70,"I":76,"J":80,
"K":72,"L":60,"M":74,"Q":83,"N":90,"O":95,"P":100,"S":40,"T":55,
"U":67,"V":79,"R":88
}

# Graph connections
graph = {
"A":["B"],"B":["A","C"],"C":["B","D"],"D":["C","E","S"],"E":["D","F"],
"F":["E","G"],"G":["F","H"],"H":["G","I","L"],"I":["H","J"],"J":["I","K"],
"K":["J","M","Q"],"L":["M","H"],"M":["K","L","Q"],"Q":["K","M","N","V"],
"N":["Q","O"],"O":["N","P"],"P":["O"],"S":["D","T"],"T":["S","U"],
"U":["T","V"],"V":["U","R","Q"],"R":["V"]
}

restarts = 20
max_steps = 50


def hill_climb(start):
    current = start
    path = [current]

    for _ in range(max_steps):
        neighbors = graph[current]

        best_neighbor = current
        best_value = values[current]

        for n in neighbors:
            if values[n] > best_value:
                best_neighbor = n
                best_value = values[n]

        if best_neighbor == current:
            break

        current = best_neighbor
        path.append(current)

    return path, current, values[current]


best_zone = None
best_value = -1

for r in range(restarts):

    start = random.choice(list(values.keys()))
    path, final_zone, final_val = hill_climb(start)

    print(f"\nRestart {r+1}")
    print("Start Zone:", start)
    print("Path:", path)
    print("Final Zone:", final_zone)
    print("Final Value:", final_val)

    if final_val > best_value:
        best_zone = final_zone
        best_value = final_val

print("\nOverall Best Zone:", best_zone)
print("Best Value:", best_value)