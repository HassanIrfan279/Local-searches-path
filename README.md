# Local-searches-path
simple local searches implementaion
## Overview

This project implements three **Local Search Algorithms** in Python to solve an optimization problem over a graph of interconnected zones. Each zone has an associated **advantage score**, and the objective is to find the zone with the **highest score** using different local search strategies.

The algorithms implemented are:

* Random Restart Hill Climbing (RRHC)
* Simulated Annealing (SA)
* Local Beam Search (LBS)

These algorithms demonstrate different strategies for navigating a search space and avoiding local optima.

---

## Project Structure

```
AI-Lab-7-Local-Search/
│
├── rrhc.py
├── simulated_annealing.py
├── local_beam_search.py
└── README.md
```

### File Descriptions

**rrhc.py**
Implements the **Random Restart Hill Climbing algorithm**.
The algorithm starts from random zones multiple times and performs hill climbing to find better neighboring states.

**simulated_annealing.py**
Implements the **Simulated Annealing algorithm**, which probabilistically accepts worse solutions early on to escape local maxima.

**local_beam_search.py**
Implements **Local Beam Search**, where multiple states are explored simultaneously and the best successors are retained.

---

## Problem Description

The problem represents a **graph of zones**, where:

* Each node represents a **zone**
* Each zone has an **advantage score**
* Edges represent **possible movements between zones**

The objective is to **discover the zone with the maximum advantage score** using different search techniques.

---

## Algorithms Implemented

### 1. Random Restart Hill Climbing

Hill climbing repeatedly moves to the neighboring state with the highest value.
To overcome local maxima, the algorithm restarts from random states multiple times.

Key characteristics:

* Greedy search
* Susceptible to local maxima
* Improved using multiple restarts

---

### 2. Simulated Annealing

Simulated Annealing introduces randomness by occasionally accepting worse states based on a probability function.

Key characteristics:

* Uses temperature parameter
* Accepts downhill moves probabilistically
* Gradually reduces randomness

---

### 3. Local Beam Search

Local Beam Search keeps **multiple candidate states simultaneously** and expands their neighbors.

Key characteristics:

* Explores multiple states at once
* Keeps the best `k` states
* Shares information across paths

---

## Requirements

* Python 3.x
* Standard libraries only:

  * `random`
  * `math`

No external dependencies are required.

---

## How to Run

Run each Python file individually from the terminal or VS Code.

Example:

```bash
python rrhc.py
```

```bash
python simulated_annealing.py
```

```bash
python local_beam_search.py
```

---

## Expected Output

Each script prints:

* Starting zone
* Path or explored states
* Final zone reached
* Final advantage score

Simulated Annealing additionally reports:

* Total moves
* Downhill attempts
* Downhill acceptances

---

## Learning Objectives

This lab demonstrates:

* Understanding **local search strategies**
* Differences between **deterministic and probabilistic search**
* Techniques to avoid **local optima**
* Practical implementation of AI search algorithms

---

## Author

Hassan Irfan
Artificial Intelligence Lab
