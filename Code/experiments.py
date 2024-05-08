import math
import time
import random
import statistics
import pickle
import csv
import numpy as np
import cotengra as ctg
import opt_einsum as oe
import os

os.system("CC=gcc-13 CXX=g++-13 cythonize -i con/alg.pyx")
from con.alg import CGreedy


# experiments.py contains the code to execute the experiments for the different problems and algorithms.
# It helps to create the csv tables to store the results of the experiments.
# It is used in main.py.


def get_sizes(einsum_notation, shapes):
    index_sizes = {}
    for einsum_index, shape in zip(einsum_notation.split("->")[0].split(","), shapes):
        if not hasattr(shape, '__iter__'):
            shape = list(shape)
        for index, dimension in zip(einsum_index, shape):
            if not index in index_sizes:
                index_sizes[index] = dimension
            else:
                if index_sizes[index] != dimension:
                    raise Exception(f"Dimension error for index '{index}'.")
    return index_sizes


def get_input(format_string, arguments):
    format_string = format_string.replace(" ", "")
    shapes = []
    for arg in arguments:
        if isinstance(arg, np.ndarray):
            shapes.append(arg.shape)
        elif isinstance(arg, list):
            shapes.append(arg)
        else:
            shapes.append(list(arg))
    sizes = get_sizes(format_string, shapes)
    str_in, str_out = format_string.split("->")
    inputs = list(map(set, str_in.split(",")))
    output = set(str_out)
    return inputs, output, sizes


def get_result_t(ppath, pid, problems, alg):
    global optimizer
    with open(ppath + problems[pid], 'rb') as file:
        format_string, l = pickle.load(file)

    max_repeats = 2048
    max_time = 1.0
    minimize = "flops"
    seed = random.randint(0, 1000000000)

    if alg == "OurGreedy":
        optimizer = CGreedy(seed=seed, minimize=minimize, max_repeats=max_repeats, max_time=max_time,
                            progbar=False, threshold_optimal=12)
    elif alg == "CotengraGreedy":
        optimizer = ctg.HyperOptimizer(minimize=minimize, max_repeats=max_repeats, max_time=max_time, progbar=False,
                                       methods="greedy")
    elif alg == "CotengraKaHyPar":
        optimizer = ctg.HyperOptimizer(minimize=minimize, max_repeats=max_repeats, max_time=max_time, progbar=False,
                                       methods="kahypar")

    tic = time.time()
    if alg == "OERandomGreedy":
        path, path_info = oe.contract_path(format_string, *l, optimize="random-greedy-128")
    elif alg != "OEGreedy":
        path, path_info = oe.contract_path(format_string, *l, optimize=optimizer)
    else:
        path, path_info = oe.contract_path(format_string, *l, optimize="greedy")

    flops = math.log10(path_info.opt_cost)
    max_intermediate = max(path_info.size_list)
    toc = time.time()
    t = toc - tic

    print(alg, pid)
    print("log10[flops]:", flops)
    print("log2[max_size]:", math.log2(max_intermediate))
    print(t, "s")
    print()

    result = [alg, t, flops, max_intermediate, pid]
    return result


def get_result_p(ppath, pid, problems, alg):
    global path_info
    with open(ppath + problems[pid], 'rb') as file:
        format_string, l = pickle.load(file)

    n = format_string.count(',') + 1  # number of tensors
    print("file=", problems[pid], ", n=", n)

    max_repeats = 128
    minimize = "flops"
    seed = random.randint(0, 1000000000)

    if alg == "OurGreedy":
        optimizer = CGreedy(seed=seed, minimize=minimize, max_repeats=max_repeats, progbar=False,
                            threshold_optimal=12)
    elif alg == "CotengraGreedy":
        optimizer = ctg.HyperOptimizer(minimize=minimize, max_repeats=max_repeats, progbar=False, methods="greedy")

    elif alg == "CotengraKaHyPar":
        optimizer = ctg.HyperOptimizer(minimize=minimize, max_repeats=max_repeats, progbar=False, methods="kahypar")
    else:
        optimizer = 0

    tic = time.time()
    if alg == "OERandomGreedy":
        path, path_info = oe.contract_path(format_string, *l, optimize="random-greedy-128")
    elif alg != "OEGreedy":
        path, path_info = oe.contract_path(format_string, *l, optimize=optimizer)
    else:
        path, path_info = oe.contract_path(format_string, *l, optimize="greedy")

    flops = math.log10(path_info.opt_cost)
    max_intermediate = max(path_info.size_list)
    toc = time.time()
    t = toc - tic

    print(alg, pid)
    print("log10[flops]:", math.log10(flops))
    print("log2[max_size]:", math.log2(max_intermediate))
    print(t, "s")
    print()

    result = [alg, t, flops, max_intermediate, pid]
    return result


def create_table(file_name, ppath, problems, alg, ttype):
    global pid
    results = [None] * 10
    flops_list = [None] * 5
    max_intermediate_list = [None] * 5
    time_list = [None] * 5
    name = ""

    for i in range(len(problems)):
        if ttype == "time":
            for m in range(0, 5):
                if alg != "OERandomGreedy":
                    result = get_result_t(ppath, i, problems, alg)
                    print(result)
                    name = result[0]
                    time_list[m] = result[1]
                    flops_list[m] = result[2]
                    max_intermediate_list[m] = result[3]
                    pid = result[4]
            result = [name, statistics.median(time_list), statistics.median(flops_list),
                      statistics.median(max_intermediate_list), pid]
            results[i] = result

        elif ttype == "128 paths":
            for m in range(0, 5):
                result = get_result_p(ppath, i, problems, alg)
                print(result)
                name = result[0]
                time_list[m] = result[1]
                flops_list[m] = result[2]
                max_intermediate_list[m] = result[3]
                pid = result[4]
            result = [name, statistics.median(time_list), statistics.median(flops_list),
                      statistics.median(max_intermediate_list), pid]
            results[i] = result

    print("Final result: \n", results[0])
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(results)

    return results
