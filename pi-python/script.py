import numpy as np

# radius of circle, half side length of square
r = 1000.


def gen(n_trials):
    return np.random.uniform(0.0, r * 2, n_trials)


def in_circle(x, y):
    d_x, d_y = r - x, r - y
    d_2 = d_x * d_x + d_y * d_y
    d = np.sqrt(d_2)

    return (d <= r)


def in_bottom_left(x, y):
    return (x <= r) * (y <= r)


def run_trials(n_trials, n_points):
    n_circle = np.zeros(n_trials, dtype=int)
    n_bottom_left = np.zeros(n_trials, dtype=int)

    for _ in range(n_points):
        x, y = gen(n_trials), gen(n_trials)
        n_circle += in_circle(x, y)
        n_bottom_left += in_bottom_left(x, y)

    return n_circle / n_bottom_left


from sys import argv

n_trials, n_points = 1000, 1000000
if len(argv) >= 3:
    n_trials, n_points = int(argv[1]), int(argv[2])

estimates = run_trials(n_trials, n_points)
for est in estimates:
    print(est)

print()
print(f"Mean: {np.mean(estimates)}")
print(f"Variance: {np.var(estimates)}")
