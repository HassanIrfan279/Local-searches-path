import random

values = {
"A":20,"B":28,"C":34,"D":42,"E":52,"F":58,"G":63,"H":70,"I":76,"J":80,
"K":72,"L":60,"M":74,"Q":83,"N":90,"O":95,"P":100,"S":40,"T":55,
"U":67,"V":79,"R":88
}

graph = {
"A":["B"],"B":["A","C"],"C":["B","D"],"D":["C","E","S"],"E":["D","F"],
"F":["E","G"],"G":["F","H"],"H":["G","I","L"],"I":["H","J"],"J":["I","K"],
"K":["J","M","Q"],"L":["M","H"],"M":["K","L","Q"],"Q":["K","M","N","V"],
"N":["Q","O"],"O":["N","P"],"P":["O"],"S":["D","T"],"T":["S","U"],
"U":["T","V"],"V":["U","R","Q"],"R":["V"]
}

k = 3
max_iterations = 50

beam = random.sample(list(values.keys()), k)

print("Initial Beam:", beam)

best_zone = None
best_value = -1

for i in range(max_iterations):

    successors = []

    for zone in beam:
        successors.extend(graph[zone])

    successors = list(set(successors))

    successors.sort(key=lambda x: values[x], reverse=True)

    beam = successors[:k]

    if i < 5:
        print(f"Iteration {i+1} Beam:", beam)

    for zone in beam:
        if values[zone] > best_value:
            best_value = values[zone]
            best_zone = zone

print("\nBest Zone Found:", best_zone)
print("Best Value:", best_value)