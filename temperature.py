def temperature(t, a, b, c):
    return a * t**2 + b * t + c

# Example coefficients
a = 1.5
b = -3.2
c = 10

# Test at different time points
times = [0, 5, 12, 24]

for t in times:
    temp = temperature(t, a, b, c)
    print(f"At time {t}, Temperature = {temp}")
