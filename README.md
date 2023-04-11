# Project 1 - Velocities of Gas Particles in a Boltzmann Distribution

**Formal write up is located in this repository, named "Rafizadeh_WRITEUP.pdf"**

## Data Generation

The Boltzmann distributions are generated by the `rng_MaxBoltz.py` python file. This file requires python3 to run, and includes the following packages listed at the top of the script:

```
  import sys
  import numpy as np
  import matplotlib.pyplot as plt
  import scipy.optimize as optimize
  import scipy.stats as stats
```

To run this script from the terminal in linux, run:

> $ python3 rng_MaxBoltz.py

This runs the file with the default parameter of 100 experiments (Nexp).

This value can be altered from the command line in the terminal by simply adding an argument after the file name.

For example, it may looks something like this in linux:

> $ python3 rng.MaxBoltz.py -Nexp 10

which would generate 10 curves from differing parameters for the Boltzmann distribution. I recommend not exceeding 100 experiments as it may take the script a while to run. 

## Data Analysis

The generated data is plotted and analyzed by the `plot_MaxBoltz.py` python file. This file requires python3 to run, and includes the following packages listed at the top of the script:

```
  import sys
  import numpy as np
  import matplotlib.pyplot as plt
  import scipy.stats as ss
  import scipy.optimize as optimize
  from scipy.stats import ttest_ind
  import math
  from statsmodels.stats.power import  tt_ind_solve_power
```

To run this script from the terminal in linux, run:

> plot_MaxBoltz.py

This creates a Neyman construction from an input data set. By default, it will analyze the data generated and outputted by the rng_MaxBoltz.py file, yet any data file can be used as an input by use of some arguments.

### Using the `rng_MaxBoltz.py` generated data:

The anaylsis file is set to read the output of the generator file by default, the only argument you need to include is the same number of experiments you used in the previous file. If you did not specify a number for that file, you do not need to here either. For example,

> $ python3 plot_MaxBoltz.py -Nexp 10

which sets the number of parameters tested as 10 instead of the default 100. This is for plotting purposes, if you use a different number here it will try to plot a different amount of points. 

The script will then plot the data as a scatter plot around the total correlation line, as seen below.




