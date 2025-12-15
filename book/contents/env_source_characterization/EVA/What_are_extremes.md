---
thebe: true
---

# What are extremes?


If you hear the word “extreme”, the first thing that may come to your mind are extreme sports or natural disasters, such as a hurricane or a typhoon. That gives us an intuition of what is an extreme observation in probability theory. Let’s see it in further detail with a dummy example.

```{raw} html
<iframe
  src="../../../_static/widgets/discharge_widget.html"
  width="100%" height="520" style="border:0" loading="lazy">
</iframe>
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

For instance, going back to the example of the discharge, EVA allows us to get a better understanding of how the discharge behave. We focus on modelling the very high discharge and forget about the low discharge data (which represents the bulk of the dataset). The probabilistic model developed with EVA will allow us to gain information about discharges higher than those already recorded in our dataset and gain insight on how this may present in extreme situations.

In the following sections, you will see how to select extreme observations within a database (timeseries of observations) and select, fit and use probability distribution functions to characterize their uncertainty and infer the needed extreme values for design.

## Return Level

The **Return Level** is a fundamental concept for risk analysis and engineering design. It defines the threshold value for an extreme variable (like wave-height, wind speed or water level) that is expected to be exceeded, on average, once during the specified time interval called the **Return Period ($T$)**. For example, a 100-year return period refers to an event that has a 1 in 100 (or 1%) probability of being exceeded each single year. 

Statistically, the return level is linked to the **Cumulative Distribution Function (CDF)**, denoted as $F(x)$. If $F(x)$ represents the probability that a variable is *less than or equal* to a value $x$, then the probability of *exceeding* that value is $1-F(x)$.

The relation between the Return Period $T$ and the CDF is:

$$
T = \frac{1}{1 - F(x_T)}
$$

To determine the specific design value $x_t$ for a chosen return period, this equation can be rewritten, where the inverse of the CDF is taken:

$$
x_t = F^{-1}(1 - \frac{1}{T})
$$

