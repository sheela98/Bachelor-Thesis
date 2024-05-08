# probs.py contains the file names of the problems used stored in lists.
# Four lists for the four categories: model_counting, quantum_circuits,
# graphs and language models.
# It also contains the names of the cost functions stored in a list.

# Model Counting Problem File Names
model_counting = [
    "mc2023_023.pkl",
    "mc2023_025.pkl",
    "mc2023_035.pkl",
    "preprocessed_mc2022_037.pkl",
    "preprocessed_mc2022_044.pkl",
    "preprocessed_mc2022_074.pkl",
    "preprocessed_mc2023_019.pkl",
    "preprocessed_mc2023_099.pkl",
    "wmc_2020_115.pkl",
    "wmc_2022_105.pkl",
]

# Quantum Circuit Problem File Names
quantum_circuits = [
    "qft_circuit-13.pkl",
    "qft_circuit-14.pkl",
    "quantum_circuits-01.pkl",
    "quantum_circuits-02.pkl",
    "quantum_circuits-14.pkl",
    "quantum_circuits-18.pkl",
    "quantum_circuits-21.pkl",
    "quantum_circuits-42.pkl",
    "quantum_circuits-46.pkl",
    "rand_supremacy2d-(2, 7, 2).pkl",
]

# Graph Problem File Names
graphs = [
    "blasted_case_56.pkl",
    "or-70-20-2-UC-10.pkl",
    "planar_graphs-29.pkl",
    "regular_graphs-12.pkl",
    "regular_graphs-13.pkl",
    "regular_graphs-14.pkl",
    "regular_graphs-15.pkl",
    "regular_graphs-31.pkl",
    "sat-grid-pbl-20.pkl",
    "square_lattices-09.pkl",
]

# Language Model Problem File Names
language_models = [
    "tensor_lm_batch_likelihood_brackets_random_depth_3_axis_size_8.pkl",
    "tensor_lm_batch_likelihood_brackets_random_depth_3_axis_size_12.pkl",
    "tensor_lm_batch_likelihood_brackets_random_depth_3_axis_size_16.pkl",
    "tensor_lm_batch_likelihood_brackets_random_depth_4_axis_size_4.pkl",
    "tensor_lm_batch_likelihood_brackets_random_depth_4_axis_size_12.pkl",
    "tensor_lm_batch_likelihood_brackets_random_depth_4_axis_size_16.pkl",
    "tensor_lm_batch_likelihood_simple_sentence_random_depth_3_axis_size_12.pkl",
    "tensor_lm_batch_likelihood_simple_sentence_random_depth_4_axis_size_4.pkl",
    "tensor_lm_batch_likelihood_simple_sentence_random_depth_4_axis_size_12.pkl",
    "tensor_lm_p_first_and_last_brackets_random_depth_4_axis_size_16.pkl",
]

# Cost Functions
cost_functions = [
    "cost_balanced_boltzmann<T>",     # 0
    "cost_boltzmann<T>",              # 1
    "cost_max_skew<T>",               # 2
    "cost_anti_balanced<T>",          # 3
    "cost_skew_balanced<T>",          # 4
    "cost_log<T>",                    # 5
    "cost_memory_removed_jitter<T>",  # 6
    "cost_batch_balanced<T>",         # 7
    "cost_log2<T>",                   # 8
    "cost_new<T>"                     # 9
]
