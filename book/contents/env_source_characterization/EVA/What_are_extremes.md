# What are extremes?

If you hear the word “extreme”, the first thing that may come to your mind are extreme sports or natural disasters, such as a hurricane or a typhon. That gives us an intuition of what is an extreme observation in probability theory. Let’s see it in further detail with a dummy example.

```{code-cell} python
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

```