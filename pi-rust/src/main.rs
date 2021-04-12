use rand::prelude::*;
use std::f64;

// radius of circle, half side length of square
const R: f64 = 1000.;

fn gen(x: f64) -> f64 {
    let mut rng = thread_rng();
    let num = rng.gen_range(0.0..x);
    return num;
}

fn in_circle(x: f64, y: f64) -> bool {
    let (d_x, d_y) = (R - x, R - y);
    let d_2 = d_x * d_x + d_y * d_y;
    let d = d_2.sqrt();
    d <= R
}

fn in_bottom_left(x: f64, y: f64) -> bool {
    x <= R && y <= R
}

fn run_trial(n: u32) -> f64 {
    let (mut n_circle, mut n_bottom_left) = (0, 0);

    for _ in 0..n {
        let (x, y) = (gen(R * 2.), gen(R * 2.));
        n_circle += if in_circle(x, y) { 1 } else { 0 };
        n_bottom_left += if in_bottom_left(x, y) { 1 } else { 0 };
    }

    (n_circle as f64) / (n_bottom_left as f64)
}

fn main() {
    let n = 1000000;
    let n_trials = 1000;

    let mut estimates: Vec<f64> = Vec::new();

    let mut estimate_sum: f64 = 0.;
    for _ in 0..n_trials {
        let estimate = run_trial(n);
        println!("{}", estimate);

        estimates.push(estimate);
        estimate_sum += estimate;
    }
    let mean = estimate_sum / (n_trials as f64);

    let mut estimate_var_sum = 0.;
    for e in estimates {
        estimate_var_sum += (mean - e) * (mean - e);
    }

    let var = estimate_var_sum / (n_trials as f64);
    println!("\nMean: {}, Variance: {}", mean, var);
}
