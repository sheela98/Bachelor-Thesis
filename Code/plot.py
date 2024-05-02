import csv
import math

import matplotlib.pyplot as plt


def get_data(file, t, x, category, spec):
    with open(file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row
        x_data = []
        y_data = []

        baseline = []
        SGreedy_data = []
        SKaHyPar_data = []
        CtgGreedy_data = []
        CtgKaHyPar_data = []
        OeRGreedy_data = []

        for row in reader:
            if spec != "time":
                if row[0] == 'OEGreedy':
                    element = math.pow(10, float(row[2]))
                    baseline.append(element)
                if row[0] == 'OurGreedy':
                    x += 5
                    x_data.append(x)
                    SGreedy_data.append(float(row[2]))
                elif row[0] == 'CotengraGreedy':
                    CtgGreedy_data.append(float(row[2]))
                elif row[0] == 'CotengraKaHyPar':
                    CtgKaHyPar_data.append(float(row[2]))
                elif row[0] == 'OERandomGreedy' and t != "timeout":
                    OeRGreedy_data.append(float(row[2]))
            else:
                if row[0] == 'OEGreedy':
                    baseline.append(float(row[1]))
                if row[0] == 'OurGreedy':
                    x += 5
                    x_data.append(x)
                    SGreedy_data.append(float(row[1]))
                elif row[0] == 'CotengraGreedy':
                    CtgGreedy_data.append(float(row[1]))
                elif row[0] == 'CotengraKaHyPar':
                    CtgKaHyPar_data.append(float(row[1]))
                elif row[0] == 'OERandomGreedy':
                    OeRGreedy_data.append(float(row[1]))

    for i in range(len(baseline)):
        if spec == "speedup":
            SGreedy_data[i] = baseline[i] / math.pow(10, SGreedy_data[i])
            SKaHyPar_data[i] = baseline[i] / math.pow(10, SKaHyPar_data[i])
            CtgGreedy_data[i] = baseline[i] / math.pow(10, CtgGreedy_data[i])
            CtgKaHyPar_data[i] = baseline[i] / math.pow(10, CtgKaHyPar_data[i])
            if t != "timeout" and category != "mc":
                OeRGreedy_data[i] = baseline[i] / math.pow(10, OeRGreedy_data[i])
        elif spec == "flops":
            SGreedy_data[i] = math.pow(10, SGreedy_data[i])
            SKaHyPar_data[i] = math.pow(10, SKaHyPar_data[i])
            if CtgGreedy_data != 50:
                CtgGreedy_data[i] = math.pow(10, CtgGreedy_data[i])
            if CtgKaHyPar_data != 50:
                CtgKaHyPar_data[i] = math.pow(10, CtgKaHyPar_data[i])
            if t != "timeout":
                if OeRGreedy_data != 50:
                    OeRGreedy_data[i] = math.pow(10, OeRGreedy_data[i])

    if spec != "time":
        for i in range(0, len(CtgGreedy_data)):
            if CtgGreedy_data[i] == 1.0:
                CtgGreedy_data[i] = math.pow(10, 50)
        for i in range(0, len(OeRGreedy_data)):
            if OeRGreedy_data[i] == 1.0:
                OeRGreedy_data[i] = math.pow(10, 50)
    if spec == "time":
        for i in range(0, len(CtgGreedy_data)):
            if CtgGreedy_data[i] == 0.0:
                CtgGreedy_data[i] = 1000
        for i in range(0, len(OeRGreedy_data)):
            if OeRGreedy_data[i] == 0.0:
                OeRGreedy_data[i] = 1000

    y_data.append(SGreedy_data)
    y_data.append(SKaHyPar_data)
    y_data.append(CtgGreedy_data)
    y_data.append(CtgKaHyPar_data)
    if t != "timeout":
        y_data.append(OeRGreedy_data)

    return x_data, y_data, baseline


def read_data(file, store, title, t, spec):
    category = "mc"
    x_data_mc, y_data_mc, baseline_mc = get_data(file[0], t, 0, category, spec)
    category = "qc"
    x_data_qc, y_data_qc, baseline_qc = get_data(file[1], t, 50, category, spec)
    category = "gp"
    x_data_gp, y_data_gp, baseline_gp = get_data(file[2], t, 100, category, spec)
    category = "lm"
    x_data_lm, y_data_lm, baseline_lm = get_data(file[3], t, 150, category, spec)

    # Model Counting
    if spec == "flops":
        plt.scatter(x=x_data_mc, y=baseline_mc, s=12, marker='*', color='#508CA4')
    plt.scatter(x=x_data_mc, y=y_data_mc[0], s=12, marker='d', color='#1D2D44')
    plt.scatter(x=x_data_mc, y=y_data_mc[2], s=12, marker='v', color='#CC7178')
    plt.scatter(x=x_data_mc, y=y_data_mc[3], s=12, marker='^', color='#89023E')
    if t != "timeout":
        plt.scatter(x=x_data_mc, y=y_data_mc[4], s=12, marker='p', color='#BFD7EA')

    # Qanutum Circuits
    if spec == "flops":
        plt.scatter(x=x_data_qc, y=baseline_qc, s=12, marker='*', label='OEGreedy', color='#508CA4')
    plt.scatter(x=x_data_qc, y=y_data_qc[0], s=12, label='$\mathbf{OurGreedy}$', marker='d', color='#1D2D44')
    plt.scatter(x=x_data_qc, y=y_data_qc[2], s=12, label='CotengraGreedy', marker='v', color='#CC7178')
    plt.scatter(x=x_data_qc, y=y_data_qc[3], s=12, label='CotengraKaHyPar', marker='^', color='#89023E')
    if t != "timeout":
        plt.scatter(x=x_data_qc, y=y_data_qc[4], s=12, label='OERandomGreedy', marker='p', color='#BFD7EA')

    # Graph Problems
    if spec == "flops":
        plt.scatter(x=x_data_gp, y=baseline_gp, s=12, marker='*', color='#508CA4')
    plt.scatter(x=x_data_gp, y=y_data_gp[0], s=12, marker='d', color='#1D2D44')
    plt.scatter(x=x_data_gp, y=y_data_gp[2], s=12, marker='v', color='#CC7178')
    plt.scatter(x=x_data_gp, y=y_data_gp[3], s=12, marker='^', color='#89023E')
    if t != "timeout":
        plt.scatter(x=x_data_gp, y=y_data_gp[4], s=12, marker='p', color='#BFD7EA')

    # Language Models
    if spec == "flops":
        plt.scatter(x=x_data_lm, y=baseline_lm, s=12, marker='*', color='#508CA4')
    plt.scatter(x=x_data_lm, y=y_data_lm[0], s=12, marker='d', color='#1D2D44')
    plt.scatter(x=x_data_lm, y=y_data_lm[2], s=12, marker='v', color='#CC7178')
    plt.scatter(x=x_data_lm, y=y_data_lm[3], s=12, marker='^', color='#89023E')
    if t != "timeout":
        plt.scatter(x=x_data_lm, y=y_data_lm[4], s=12, marker='p', color='#BFD7EA')

    if spec == "time":
        x_data = []
        for sublist in [x_data_mc, x_data_qc, x_data_gp, x_data_lm]:
            x_data.extend(sublist)
        y_data = []
        for sublist in [y_data_mc, y_data_qc, y_data_gp, y_data_lm]:
            y_data.extend(sublist[0])
        plt.plot(x_data, y_data, linewidth=0.7, color='#1D2D44')

    # Add a horizontal line at y=1
    if spec == "speedup":
        plt.axhline(y=1, color='#C5BAAF', linestyle='-', label='Baseline', linewidth=0.8)

    # Add vertical lines for problem categories
    plt.axvline(x=0, color='#E0DFD5', linestyle='--', linewidth=0.8)
    plt.axvline(x=52.5, color='#E0DFD5', linestyle='--', linewidth=0.8)
    plt.axvline(x=102.5, color='#E0DFD5', linestyle='--', linewidth=0.8)
    plt.axvline(x=152.5, color='#E0DFD5', linestyle='--', linewidth=0.8)
    plt.axvline(x=202.5, color='#E0DFD5', linestyle='--', linewidth=0.8)

    # Labels and title
    tick_labels = ["Model Counting", "Quantum Circuits", "Graph Problems", "Language Models"]
    midpoints = [25, 75, 125, 175]
    plt.xticks(midpoints, tick_labels, fontsize=8)

    # Logarithmic scale
    plt.yscale('log')

    plt.xlabel('Test Problems', fontsize=10)
    if spec == "speedup":
        plt.ylabel('Speed-up', fontsize=10)
    elif spec == "flops":
        plt.ylabel('Flops log 10', fontsize=10)
    else:
        plt.ylabel('Time in Seconds', fontsize=10)

    plt.title(title)
    plt.plot(0, 100000, color='white')

    # Legend
    plt.legend(loc='upper right')

    # Store plot as svg
    plt.savefig(store, format='svg')

    # Show plot
    plt.show()


if __name__ == '__main__':
    # Plot 128 paths - time
    file_mc = "Results/Tables/results_mc_128paths.csv"
    file_qc = "Results/Tables/results_qc_128paths.csv"
    file_gp = "/Results/Tables/results_gp_128paths.csv"
    file_lm = "Results/Tables/results_lm_128paths.csv"
    files = [file_mc, file_qc, file_gp, file_lm]

    store = "Results/Graphics/plot_128p_time.svg"
    title = "Time for the computation of 128 paths"
    t = "128 paths"
    spec = "time"

    read_data(files, store, title, t, spec)

    # Plot 128 paths - flops
    file_mc = "Results/Tables/results_mc_128paths.csv"
    file_qc = "Results/Tables/results_qc_128paths.csv"
    file_gp = "Results/Tables/results_gp_128paths.csv"
    file_lm = "Results/Tables/results_lm_128paths.csv"
    files = [file_mc, file_qc, file_gp, file_lm]

    store = "Results/Graphics/plot_128p_flops.svg"
    title = "Results for the computation of 128 paths"
    t = "128 paths"
    spec = "flops"

    read_data(files, store, title, t, spec)

    # Plot Timeout
    file_mc = "Results/Tables/results_mc_timeout.csv"
    file_qc = "Results/Tables/results_qc_timeout.csv"
    file_gp = "Results/Tables/results_gp_timeout.csv"
    file_lm = "Results/Tables/results_lm_timeout.csv"
    files = [file_mc, file_qc, file_gp, file_lm]

    store = "Results/Graphics/plot_t_flops.svg"
    title = "Results with timeout 1 second"
    t = "timeout"
    spec = "flops"

    read_data(files, store, title, t, spec)
