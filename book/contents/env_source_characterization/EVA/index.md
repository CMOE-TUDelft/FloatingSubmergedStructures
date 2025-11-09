# Extreme Value Analysis


```
This section was written with the help of backround material written by Patricia Mares Nasarre 
```

While data can be used to obtain information about regular behaviour, it can also be used to quantify stochastic behaviour. In many engineering problems, there is typically an interest in the tail of distributions. For instance, flood protection systems will be designed to withstand extreme rainfall events or extreme river discharges (low exceedance probabilities), not only daily conditions (high exceedance probabilities); these extreme events are located in the tails of the distribution. Moreover, by definition, extreme events are typically scarce in our datasets, as they occur infrequently. The available time series are usually short (e.g., 20 years) in comparison with the design events that the system needs to withstand (e.g., 1,000 years event).

:::{card} Definition
**Extreme Value Analysis (EVA)** focuses on those events located at the tails of the distribution (extreme events) and provides a framework to identify and model the stochastic behaviour of these extreme events such that events which have not been observed can be inferred.
:::

In the following sections, the formal concept of extreme will be introduced, as well as the techniques to sample them, without data, and probabilistically model them.

:::{card} Extreme Value Analysis Outline

We will cover two methods of performing an extreme value analysis: **block maxima** and **peak over threshold,** both of which are applied in the same way:

1. Identify a random variable of interest that can be modelled with a continuous parametric probability distribution
2. Prepare and explore the data set that will be used to fit a distribution
3. **Sample** the data to collect a set of the _extreme_ observations
4. Fit a distribution to the sampled set of data
5. Repeat the sampling and fitting process as needed, evaluating the alternatives, until a suitable model is identified

:::

