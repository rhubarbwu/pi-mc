#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include "stdbool.h"

// radius of circle, half side length of square
double r = 1000.;

double gen(double x) {
    double num = (double)rand() / (double)(RAND_MAX / x);
    return num;
}

bool in_circle(double x, double y) {
    double d_x = r - x;
    double d_y = r - y;
    double d_2 = d_x * d_x + d_y * d_y;
    double d = sqrt(d_2);

    return d <= (double)r;
}

bool in_bottom_left(double x, double y) {
    return x <= r && y <= r;
}

double run_trial(int n) {
    srand(time(0));
    int n_circle = 0;
    int n_bottom_left = 0;

    for (int i = 0; i < n; i++) {
        double x = gen(r * 2);
        double y = gen(r * 2);
        n_circle += in_circle(x, y);
        n_bottom_left += in_bottom_left(x, y);
    }

    return (double)((double)n_circle / (double)n_bottom_left);
}

int main() {
    int n = 1000000;
    int n_trials = 1000;

    double estimates[n_trials];

    double estimate_sum = 0;
    for (int t = 0; t < n_trials; t++) {
        double estimate = run_trial(n);
        printf("%0.16lf\n", estimate);

        estimates[t] = estimate;
        estimate_sum += estimate;
    }
    double mean = estimate_sum / (double)n_trials;

    double estimate_var_sum = 0;
    for (int t = 0; t < n_trials; t++)
        estimate_var_sum += (mean - estimates[t]) * (mean - estimates[t]);

    double var = estimate_var_sum / (double)n_trials;
    printf("\nMean: %0.16lf, Variance: %0.16lf\n", mean, var);
}
