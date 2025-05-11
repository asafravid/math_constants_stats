from mpmath import mp
from collections import Counter
import os

# Set precision to digits
mp.dps = 1000000
NUM_ELEMENTS_TO_PLOT = 20

def plot_frequencies_text_color(freq_data, title, xlabel, color, num_elements):
    max_width = 345  # Maximum width of the bar in characters
    # ANSI color codes
    colors = { 'black': '\033[30m', 'red': '\033[31m', 'green': '\033[32m', 'yellow': '\033[33m', 'blue': '\033[34m', 'magenta': '\033[35m', 'cyan': '\033[36m', 'white': '\033[37m', 'reset': '\033[0m' }
    color_code = colors.get(color, colors['blue'])  # Default to blue if color not found
    
    labels, values = zip(*freq_data)
    max_value = max(values)
    
    print(f"{title}: num_elements={num_elements} - {xlabel} → Frequency shown by bar length:")
    for label, value in freq_data:
        bar_length = int((value / max_value) * max_width)
        bar = '█' * bar_length  # Use ASCII block character
        print(f"{label:5} | {color_code}{bar}{colors['reset']} ({value}, {value / num_elements:.4%})")

# Function to count frequencies of n-length digit sequences
def count_frequencies(digits, n):
    sequences = [digits[i:i+n] for i in range(len(digits)-n+1)]
    sequence_strings = [''.join(map(str, seq)) for seq in sequences]
    return Counter(sequence_strings)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

# Get pi as a string and remove the decimal point
print("Calculating Pi...")
pi_str = str(mp.pi).replace('.', '')
print("Calculating e (Euler's Number)...")
e_str = str(mp.e).replace('.', '')
print("Calculating φ (Golden Ratio)...")
g_str = str(mp.phi).replace('.', '')

combine_str = pi_str + e_str + g_str

# Convert to list of integers
print("Converting to list of digits...")
pi_digits = [int(d) for d in pi_str]
e_digits = [int(d) for d in e_str]
g_digits = [int(d) for d in g_str]
combine_digits = [int(d) for d in combine_str]

# Count frequencies of single digits, pairs, triplets, and quadruplets
print("Counting frequencies...\n")
pi_single_digit_freq = count_frequencies(pi_digits, 1)
e_single_digit_freq = count_frequencies(e_digits, 1)
g_single_digit_freq = count_frequencies(g_digits, 1)
combine_single_digit_freq = count_frequencies(combine_digits, 1)

pi_pair_freq = count_frequencies(pi_digits, 2)
e_pair_freq = count_frequencies(e_digits, 2)
g_pair_freq = count_frequencies(g_digits, 2)
combine_pair_freq = count_frequencies(combine_digits, 2)

pi_triplet_freq = count_frequencies(pi_digits, 3)
e_triplet_freq = count_frequencies(e_digits, 3)
g_triplet_freq = count_frequencies(g_digits, 3)
combine_triplet_freq = count_frequencies(combine_digits, 3)

pi_quadruplet_freq = count_frequencies(pi_digits, 4)
e_quadruplet_freq = count_frequencies(e_digits, 4)
g_quadruplet_freq = count_frequencies(g_digits, 4)
combine_quadruplet_freq = count_frequencies(combine_digits, 4)

pi_pentuplet_freq = count_frequencies(pi_digits, 5)
e_pentuplet_freq = count_frequencies(e_digits, 5)
g_pentuplet_freq = count_frequencies(g_digits, 5)
combine_pentuplet_freq = count_frequencies(combine_digits, 5)

# Sort frequencies from highest to lowest
sorted_pi_single_digit_freq = pi_single_digit_freq.most_common(NUM_ELEMENTS_TO_PLOT)
sorted_e_single_digit_freq = e_single_digit_freq.most_common(NUM_ELEMENTS_TO_PLOT)
sorted_g_single_digit_freq = g_single_digit_freq.most_common(NUM_ELEMENTS_TO_PLOT)
sorted_combine_single_digit_freq = combine_single_digit_freq.most_common(NUM_ELEMENTS_TO_PLOT)

sorted_pi_pair_freq = pi_pair_freq.most_common(NUM_ELEMENTS_TO_PLOT)
sorted_e_pair_freq = e_pair_freq.most_common(NUM_ELEMENTS_TO_PLOT)
sorted_g_pair_freq = g_pair_freq.most_common(NUM_ELEMENTS_TO_PLOT)
sorted_combine_pair_freq = combine_pair_freq.most_common(NUM_ELEMENTS_TO_PLOT)

sorted_pi_triplet_freq = pi_triplet_freq.most_common(NUM_ELEMENTS_TO_PLOT)
sorted_e_triplet_freq = e_triplet_freq.most_common(NUM_ELEMENTS_TO_PLOT)
sorted_g_triplet_freq = g_triplet_freq.most_common(NUM_ELEMENTS_TO_PLOT)
sorted_combine_triplet_freq = combine_triplet_freq.most_common(NUM_ELEMENTS_TO_PLOT)

sorted_pi_quadruplet_freq = pi_quadruplet_freq.most_common(NUM_ELEMENTS_TO_PLOT)
sorted_e_quadruplet_freq = e_quadruplet_freq.most_common(NUM_ELEMENTS_TO_PLOT)
sorted_g_quadruplet_freq = g_quadruplet_freq.most_common(NUM_ELEMENTS_TO_PLOT)
sorted_combine_quadruplet_freq = combine_quadruplet_freq.most_common(NUM_ELEMENTS_TO_PLOT)

sorted_pi_pentuplet_freq = pi_pentuplet_freq.most_common(NUM_ELEMENTS_TO_PLOT)
sorted_e_pentuplet_freq = e_pentuplet_freq.most_common(NUM_ELEMENTS_TO_PLOT)
sorted_g_pentuplet_freq = g_pentuplet_freq.most_common(NUM_ELEMENTS_TO_PLOT)
sorted_combine_pentuplet_freq = combine_pentuplet_freq.most_common(NUM_ELEMENTS_TO_PLOT)

plot_frequencies_text_color(sorted_pi_single_digit_freq, 'Single Digit Freqs in Pi', 'Digits', 'blue', mp.dps)
plot_frequencies_text_color(sorted_e_single_digit_freq, 'Single Digit Freqs in e', 'Digits', 'green', mp.dps)
plot_frequencies_text_color(sorted_g_single_digit_freq, 'Single Digit Freqs in φ', 'Digits', 'yellow', mp.dps)
plot_frequencies_text_color(sorted_combine_single_digit_freq, 'Single Digit Freqs in Combined', 'Digits', 'red', mp.dps*3)

plot_frequencies_text_color(sorted_pi_pair_freq, 'Digit Pairs Freqs in Pi', 'Pairs', 'blue', mp.dps)
plot_frequencies_text_color(sorted_e_pair_freq, 'Digit Pairs Freqs in e', 'Pairs', 'green', mp.dps)
plot_frequencies_text_color(sorted_g_pair_freq, 'Digit Pairs Freqs in φ', 'Pairs', 'yellow', mp.dps)
plot_frequencies_text_color(sorted_combine_pair_freq, 'Digit Pairs Freqs in Combined', 'Pairs', 'red', mp.dps*3)

plot_frequencies_text_color(sorted_pi_triplet_freq, 'Triple Digits Freqs in Pi', 'Triplets', 'blue', mp.dps)
plot_frequencies_text_color(sorted_e_triplet_freq, 'Triple Digits Freqs in e', 'Triplets', 'green', mp.dps)
plot_frequencies_text_color(sorted_g_triplet_freq, 'Triple Digits Freqs in φ', 'Triplets', 'yellow', mp.dps)
plot_frequencies_text_color(sorted_combine_triplet_freq, 'Triple Digits Freqs in Combined', 'Triplets', 'red', mp.dps*3)

plot_frequencies_text_color(sorted_pi_quadruplet_freq, 'Quadruple Digits Freqs in Pi', 'Quadruplets', 'blue', mp.dps)
plot_frequencies_text_color(sorted_e_quadruplet_freq, 'Quadruple Digits Freqs in e', 'Quadruplets', 'green', mp.dps)
plot_frequencies_text_color(sorted_g_quadruplet_freq, 'Quadruple Digits Freqs in φ', 'Quadruplets', 'yellow', mp.dps)
plot_frequencies_text_color(sorted_combine_quadruplet_freq, 'Quadruple Digits Freqs in Combined', 'Quadruplets', 'red', mp.dps*3)

plot_frequencies_text_color(sorted_pi_pentuplet_freq, 'Pentuple Digits Freqs in Pi', 'Pentuplets', 'blue', mp.dps)
plot_frequencies_text_color(sorted_e_pentuplet_freq, 'Pentuple Digits Freqs in e', 'Pentuplets', 'green', mp.dps)
plot_frequencies_text_color(sorted_g_pentuplet_freq, 'Pentuple Digits Freqs in φ', 'Pentuplets', 'yellow', mp.dps)
plot_frequencies_text_color(sorted_combine_pentuplet_freq, 'Pentuple Digits Freqs in Combined', 'Pentuplets', 'red', mp.dps*3)
