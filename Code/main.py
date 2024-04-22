from experiments import *
from probs import *

import os
import time
import opt_einsum as oe
import numpy as np
import sesum.sr as sr
from probs import *
import pickle
import csv

os.system("CC=gcc-13 CXX=g++-13 cythonize -i con/alg.pyx")
from con.alg import CGreedy

if __name__ == '__main__':
    ppath = "/Users/sheela_1/Documents/7_WS_23/Bachelorarbeit/Code/einsum_problems/"
    ppath_lm = "/Users/sheela_1/Documents/7_WS_23/Bachelorarbeit/Meeting_23_01_2024/Einsum_Problems_LM/"

    algorithms = ["OEGreedy", "SesumGreedy", "SesumKaHyPar", "CotengraGreedy", "CotengraKaHyPar", "OERandomGreedy"]

    # Get Min - Max Tensors
    problem = language_models
    print("language_models")

    # OERandom Greedy
    for p in problem:
        with open(ppath_lm + p, 'rb') as file:
            format_string, l = pickle.load(file)

        n = format_string.count(',') + 1  # number of tensors
        print("file=", p, ", n=", n)

    """
    # Model Counting - 128 paths

    file_name = "results_mc_128paths_testtest.csv"
    problem = model_counting
    t = "128 paths"
    print("Model Counting - 128 paths")

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        entry = ["Model Counting - 128 paths"]
        writer.writerow(entry)


    # OERandom Greedy
    create_table(file_name, ppath, [problem[0]], algorithms[1], t)
    create_table(file_name, ppath, [problem[1]], algorithms[1], t)
    create_table(file_name, ppath, [problem[2]], algorithms[1], t)
    create_table(file_name, ppath, [problem[3]], algorithms[1], t)
    create_table(file_name, ppath, [problem[4]], algorithms[1], t)
    create_table(file_name, ppath, [problem[5]], algorithms[1], t)
    create_table(file_name, ppath, [problem[6]], algorithms[1], t)
    create_table(file_name, ppath, [problem[7]], algorithms[1], t)
    create_table(file_name, ppath, [problem[8]], algorithms[1], t)
    create_table(file_name, ppath, [problem[9]], algorithms[1], t)


    

    # Language Models - 128 paths
    
    file_name = "results_lm_128paths.csv"
    problem = language_models
    t = "128 paths"
    print("Language Models - 128 paths")

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        entry = ["Language Models - 128 paths"]
        writer.writerow(entry)

    for alg in algorithms:
        create_table(file_name, ppath_lm, problem, alg, t)

        
    # Quantum Computing - 128 paths

    file_name = "results_qc_128paths.csv"
    problem = quantum_circuits
    t = "128 paths"
    print("Quantum Computing - 128 paths")

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        entry = ["Quantum Computing - 128 paths"]
        writer.writerow(entry)

    for alg in algorithms:
        create_table(file_name, ppath, problem, alg, t)
    
    # Graph Problems - 128 paths

    file_name = "results_gp_128paths.csv"
    problem = graphs
    t = "128 paths"
    print("Graph Problems - 128 paths")

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        entry = ["Graph Problems - 128 paths"]
        writer.writerow(entry)

    for alg in algorithms:
        create_table(file_name, ppath, problem, alg, t)

    

    # Model Counting - 128 paths

    file_name = "results_mc_128paths.csv"
    problem = model_counting
    t = "128 paths"
    print("Model Counting - 128 paths")

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        entry = ["Model Counting - 128 paths"]
        writer.writerow(entry)

    for alg in algorithms:
        create_table(file_name, ppath, problem, alg, t)
        
    """

    """

    # Language Models - timeout

    file_name = "results_lm_timeout.csv"
    problem = language_models
    t = "time"
    print("Language Models - timeout")

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        entry = ["Language Models - timeout"]
        writer.writerow(entry)

    for alg in algorithms:  # exclude OERandomGreedy
        create_table(file_name, ppath_lm, problem, alg, t)
    

    # Quantum Computing - timeout
    
    file_name = "results_qc_timeout.csv"
    problem = quantum_circuits
    t = "time"
    print("Quantum Computing - timeout")
    
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        entry = ["Quantum Computing - timeout"]
        writer.writerow(entry)

    
    for alg in algorithms:
        create_table(file_name, ppath, problem, alg, t)


    # Graph Problems - timeout

    file_name = "results_gp_timeout.csv"
    problem = graphs
    t = "time"
    print("Graphs - timeout")

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        entry = ["Graphs - timeout"]
        writer.writerow(entry)

    for alg in algorithms:
        create_table(file_name, ppath, problem, alg, t)
        
   
    # Model Counting - timeout

    file_name = "results_mc_timeout_testtest.csv"
    problem = model_counting
    t = "time"
    print("Model Counting - timeout")

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        entry = ["Model Counting - timeout"]
        writer.writerow(entry)

    for alg in algorithms:
        create_table(file_name, ppath, problem, alg, t)
        
    """


