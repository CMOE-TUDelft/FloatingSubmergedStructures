# Modal Analysis

With the matrices that are associated with the free degrees of freedom, a modal analysis can be performed to understand the structural behaviour of the Submerged Floating Tunnel by decomposing the vibrational response into a series of natural modes, each characterised by a specific natural frequency and mode shape. These dynamic characteristics are particularly relevant for identifying potential **resonance** of the SFT. 

:::{card} Resonance
**Resonance** is a physical phenomenon that occurs when an external periodic force acts on a structure at a frequency matching one of its natural frequencies. When this alignment happens, the system can absorb energy from the external source with maximum efficiency, leading to rapidly increasing oscillation amplitudes. For a structure like a Submerged Floating Tunnel, identifying these resonant frequencies is critical because even small, repetitive loads (from waves, vortex shedding, or wind) can cause catastrophic structural failure or severe fatigue damage if they align with the tunnel's natural modes of vibration.
:::

## Modal Superposistion

The modal analysis can be performed by computing the reduced global matrices $K_{FF}$ and $M_{FF}$, and solving the following eigenvalue problem:

$$
(K_{FF}-\omega^2 M_{FF})\phi = 0
$$

Where:
- $\omega$: the natural circular frequency (rad/s)
- $\phi$: the mode shape vector
- $K_{FF}$ and $M_{FF}$: the reduced global stiffness and mass matrices

