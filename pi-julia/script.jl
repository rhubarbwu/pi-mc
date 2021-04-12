using Printf
using Statistics

r = 1000.


function gen(x)
    return rand(1:x)
end


function in_circle(x, y)
    d_x, d_y = r - x, r - y
    d_2 = d_x * d_x + d_y * d_y
    d = sqrt(d_2)

    return d <= r
end


function in_bottom_left(x, y)
    return x <= r && y <= r
end


function run_trial(n)
    n_circle = 0
    n_bottom_left = 0

    for _ = 1:n
        x, y = gen(r * 2), gen(r * 2)
        if in_circle(x, y)
            n_circle += 1
        end
        if in_bottom_left(x, y)
            n_bottom_left += 1
        end
    end

    return n_circle / n_bottom_left
end

n = 1000000
n_trials = 1000
estimates = zeros(n_trials)
for t = 1:n_trials
    estimate = run_trial(n)
    @printf("%.16f\n", estimate)
    estimates[t] = estimate
end

println("\nMean: ", 
    Statistics.mean(estimates),
    ", Variance: ",
    Statistics.var(estimates))
