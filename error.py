import numpy as np
from numpy import random
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

random.seed(0)
box_options = {"whis": [0, 100], "palette": "vlag"}
strip_options = {"color": ".3"}

n_sample = 100
error = pd.DataFrame(
    {
        "σ=0.1, df=1": random.standard_t(1, n_sample) * 0.1,
        "σ=1, df=10": random.standard_t(10, n_sample) * 1,
    }
)
abs_error = pd.melt(np.abs(error), var_name="method", value_name="absolute error")

plot_values = {"x": "absolute error", "y": "method", "data": abs_error}
sns.boxplot(**plot_values, **box_options)
sns.stripplot(**plot_values, **strip_options)
plt.savefig("error.svg", bbox_inches="tight")
