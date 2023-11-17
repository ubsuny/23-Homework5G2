def calculate_actual_frequencies(X):
    sample_spacing = 1  # assuming monthly data, so the spacing is 1 month
    N = len(X)
    freqs = np.fft.fftfreq(N, d=sample_spacing)
    return freqs[:N//2]  # return only the positive frequencies

# Calculate frequencies
frequencies = calculate_actual_frequencies(X)
print(frequencies)
