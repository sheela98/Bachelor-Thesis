from experiments import *
from probs import *

import os
import time
import opt_einsum as oe
from probs import *
import pickle

os.system("CC=gcc-13 CXX=g++-13 cythonize -i con/alg.pyx")
from con.alg import CGreedy

# usage_demo.py shows how to compute and execute paths with our greedy algorithm
# and provides an example.

if __name__ == '__main__':
    # Path for the following problems: Quantum Circuits, Model Counting, Graph Problems
    ppath = "Problems/Einsum_Problems/"
    # Path for the following problems: Language Models
    ppath_lm = "Problems/Einsum_Problems_LM/"

    # Choose the problem and the id
    # Problems: model_counting, quantum_circuits, graphs, language_models
    # The problems are stored as lists with the respective names in probs.py.
    problem = language_models
    pid = 0

    # Set parameters
    max_repeats = 2048
    max_time = 1.0
    minimize = "flops"
    seed = random.randint(0, 1000000000)

    with open(ppath_lm + problem[pid], 'rb') as file:
        format_string, l = pickle.load(file)

    # Initialize optimizer
    optimizer = CGreedy(seed=seed, minimize=minimize, max_repeats=max_repeats, max_time=max_time, progbar=False,
                        threshold_optimal=12)

    tic = time.time()
    # Insert path in oe and execute
    path, path_info = oe.contract_path(format_string, *l, optimize=optimizer)

    # Compute the data: flops, max_intermediate, time
    flops = math.log10(path_info.opt_cost)
    max_intermediate = max(path_info.size_list)
    toc = time.time()
    t = toc - tic


    # Print the data
    print(problem[pid])
    print("log10[flops]:", flops)
    print("log2[max_size]:", math.log2(max_intermediate))
    print(t, "s")
    print()
