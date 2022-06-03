import numpy as np

# radius of circle, half side length of square
r = 1000.


def gen(x):
    num = np.random.uniform(0.0, x)
    return num


def in_circle(x, y):
    d_x, d_y = r - x, r - y
    d_2 = d_x * d_x + d_y * d_y
    d = np.sqrt(d_2)

    return d <= r


def in_bottom_left(x, y):
    return x <= r and y <= r


def run_trial(n):
    n_circle = 0
    n_bottom_left = 0

    for _ in range(n):
        x, y = gen(r * 2), gen(r * 2)
        n_circle += 1 if in_circle(x, y) else 0
        n_bottom_left += 1 if in_bottom_left(x, y) else 0

    return n_circle / n_bottom_left


n = 1000000
n_trials = 1000
estimates = np.array([run_trial(n) for _ in range(n_trials)])

print("\nMean: {}, Variance: {}".format(np.mean(estimates), np.var(estimates)))
