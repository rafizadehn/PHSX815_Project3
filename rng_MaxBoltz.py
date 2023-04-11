import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import scipy.stats as stats

# import our Random class from Random.py file
sys.path.append(".")
from Random import Random

def boltz(x, temp):
    scale = np.sqrt(temp)
    return stats.norm.pdf(x, loc = 0, scale = scale)

def log_likelihood(x, data):
    log_likelihood = 0
    for d in data:
        log_likelihood += np.log(boltz(d, x))
    return -log_likelihood

if __name__ == "__main__":
    if '-h' in sys.argv or '--help' in sys.argv:
        print("Usage: %s -temp1 [temperature (k)] -temp2 [temperature (k)] -seed [seed] -Nmeas [number of particles sampled] -mass [mass in amu]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 5555

    # default Nexp
    Nexp = 85 
    
    # read the user-provided inputs from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = int(sys.argv[p+1])
    if '-Nexp' in sys.argv:
        p = sys.argv.index('-Nexp')
        Nexp = int(sys.argv[p+1])

    temps = np.linspace(275, 350, Nexp)
    data = []
    
    for temp in temps:
        sample = stats.norm.rvs(loc = 0, scale = np.sqrt(temp), size=100)
        data.append(sample)

    estimates = []
    for d in data:
        result = optimize.minimize(log_likelihood, x0 = 300, args = (d,))
        estimates.append(result.x[0])

    with open(r'truevals.txt', 'w') as fp:
        for item in data:
            fp.write("%s\n" % item)

    with open(r'likelihoods.txt', 'w') as fp:
        for item in estimates:
            fp.write("%s\n" % item)




