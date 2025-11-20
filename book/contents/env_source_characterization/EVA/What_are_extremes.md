---
thebe: true
---

# What are extremes?


If you hear the word “extreme”, the first thing that may come to your mind are extreme sports or natural disasters, such as a hurricane or a typhoon. That gives us an intuition of what is an extreme observation in probability theory. Let’s see it in further detail with a dummy example.

<<<<<<< HEAD
```{raw} html
<iframe
  src="../../../_static/widgets/discharge_widget.html"
  width="100%" height="520" style="border:0" loading="lazy">
</iframe>
=======
```python
import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets
from IPython.display import display

# mock PDF: log-normal-like (positive, right-skewed)
mu = 3.0
sigma = 0.7
x = np.linspace(0.01, 200, 1000)

def pdf(xv):
    return (1.0 / (xv * sigma * np.sqrt(2*np.pi))) * np.exp(- (np.log(xv) - mu)**2 / (2 * sigma**2))

y = pdf(x)

slider = widgets.FloatSlider(
    value=20.0,
    min=float(x.min()),
    max=float(x.max()),
    step=0.1,
    description='Discharge',
    continuous_update=True,
    layout=widgets.Layout(width='80%')
)

def update(discharge):
    prob = pdf(np.maximum(discharge, 0.01))
    fig, ax = plt.subplots(figsize=(8,4))
    ax.plot(x, y, lw=2, label='Probability density (mock)')
    ax.fill_between(x, y, where=(x >= discharge), color='gray', alpha=0.15)
    ax.axvline(discharge, color='red', lw=2, ls='--', label=f'Discharge = {discharge:.2f}')
    ax.axhline(prob, color='green', lw=2, ls='--', label=f'PDF = {prob:.4f}')
    ax.scatter([discharge], [prob], color='black')
    ax.set_xlabel('River discharge (units)')
    ax.set_ylabel('Probability density')
    ax.set_title('Mock Probability Density of River Discharge\n(move slider to see the changing discharge and probability of occurrence)')
    ax.legend(loc='upper right')
    ax.set_xlim(x.min(), x.max())
    ax.grid(alpha=0.3)
    plt.show()

out = widgets.interactive_output(update, {'discharge': slider})
display(slider, out)

>>>>>>> d2203d787c8f1975fd694968632f14a7cac7c133
```

Based on the graph above, we can define an extreme in probability theory as…

:::{tip} Extreme observation
An extreme is an observation which deviates from the mean and is therefore located in the tail of the distribution.  

Note that extremes are not only maxima (e.g. maximum river discharge or maximum traffic load)  
but also minima (e.g. droughts or minimum energy consumption in a network),  
depending on the direction that we move within the distribution function.
:::

**Why are we interested in extremes?**

As engineers or geoscientist, we design interventions and infrastructures to withstand scenarios which are linked to extreme conditions (does it ring the bell “Ultimate Limit State”?). For instance, if we are designing a bridge, we will be interested not only on the daily loads of the cars, but also on the maximum loads that the bridge will face along its design life (e.g.: several large trucks crossing at the same time).

**And how can we assess extreme conditions?**

Extreme Value Analysis (EVA) allows us to quantify the needed extremes for design. Typically, we have (limited) historical data (e.g.: few recorded years of traffic loads) and we need to quantify extremes which haven’t been observed yet. EVA allows us to model the stochastic behavior of extreme events and infer those which haven’t been observed (extrapolate).

For instance, going back to our toy example of the t-shirts, EVA allows us to get a better understanding of how the expensive t-shirts behave. We focus on modelling the expensive t-shirts and forget about the cheap options. The probabilistic model developed with EVA will allow us to gain information about prices higher than those already recorded in our dataset and gain insight on how the market might evolve.

In the following sections, you will see how to select extreme observations within a database (timeseries of observations) and select, fit and use probability distribution functions to characterize their uncertainty and infer the needed extreme values for design.

## Return Level

--> Here, may use chapter from MUDE

