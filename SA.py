import random
import math

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

T = 10
alpha = 0.95
max_iterations = 200

current = random.choice(list(values.keys()))
start_zone = current

best_zone = current
best_value = values[current]

downhill_attempts = 0
downhill_accepts = 0

for i in range(max_iterations):

    neighbor = random.choice(graph[current])

    delta = values[neighbor] - values[current]

    if delta > 0:
        current = neighbor
    else:
        downhill_attempts += 1
        prob = math.exp(delta / T)

        if random.random() < prob:
            current = neighbor
            downhill_accepts += 1

    if values[current] > best_value:
        best_value = values[current]
        best_zone = current

    T = T * alpha

print("Start Zone:", start_zone)
print("Best Zone Found:", best_zone)
print("Best Value:", best_value)
print("Total Moves:", max_iterations)
print("Downhill Attempts:", downhill_attempts)
print("Downhill Accepted:", downhill_accepts)