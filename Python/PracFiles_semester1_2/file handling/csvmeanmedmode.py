import pandas as pd
from statistics import mean, median, mode

def calculate_statistics(csv_file):
    data = pd.read_csv(csv_file)

    weights = data['Weight']
    heights = data['Height']

    mean_weight = mean(weights)
    median_weight = median(weights)
    mode_weight = mode(weights)

    mean_height = mean(heights)
    median_height = median(heights)
    mode_height = mode(heights)

    print("========================")
    print("Statistics for Weights:")
    print("Mean:", mean_weight)
    print("Median:", median_weight)
    print("Mode:", mode_weight)
    print("========================")
    print("Statistics for Heights:")
    print("Mean:", mean_height)
    print("Median:", median_height)
    print("Mode:", mode_height)
    print("========================")

csv_file = "heights_weights.csv"
calculate_statistics(csv_file)
