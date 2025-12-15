# Modal Analysis

With the matrices that are associated with the free degrees of freedom, a modal analysis can be performed to understand the structural behaviour of the Submerged Floating Tunnel by decomposing the vibrational response into a series of natural modes, each characterised by a specific natural frequency and mode shape. These dynamic characteristics are particularly relevant for identifying potential **resonance** of the SFT. 

:::{card} Resonance
**Resonance** is a physical phenomenon that occurs when an external periodic force acts on a structure at a frequency matching one of its natural frequencies. When this alignment happens, the system can absorb energy from the external source with maximum efficiency, leading to rapidly increasing oscillation amplitudes. For a structure like a Submerged Floating Tunnel, identifying these resonant frequencies is critical because even small, repetitive loads (from waves, vortex shedding, or wind) can cause catastrophic structural failure or severe fatigue damage if they align with the tunnel's natural modes of vibration.
:::

## Modal Superposistion

The modal analysis can be performed by computing the reduced global matrices $\mathbf{K}_{FF}$ and $\mathbf{M}_{FF}$, and solving the following eigenvalue problem:

$$
(\mathbf{K}_{FF}-\omega^2 \mathbf{M}_{FF})\phi = 0
$$

Where:
- $\omega$: the natural circular frequency (rad/s)
- $\phi$: the mode shape vector
- $\mathbf{K}_{FF}$ and $\mathbf{M}_{FF}$: the reduced global stiffness and mass matrices

The structural displacement is then approximated using the first $n$ moded:

$$
\mathbf{x}(t) \approx \sum_{i=1}^n \phi_i q_i(t)
$$

Where:
- $\phi$: the i$^{th}$ eigenvector
- $q_i(t)$: modal coordinate

Substituting the expression for structural displacement into the global system lead to the reduced-order equations of motion for each mode:

$$
\mathbf{M}_m \ddot{q}_i(t) + \mathbf{K}_m q_i(t) = \phi_i^T \mathbf{F}_{FF}(t) 
$$

Where the subscript $m$ indicates that these matrices are expressed in modal space:

$$
\mathbf{M}_m = \phi_i^T \mathbf{M}_{FF} \phi_i, \quad \mathbf{K}_m = \phi_i^T \mathbf{K}_{FF} \phi_i 
$$

And $\mathbf{F}_{FF}(t)$ represents the time-dependent external loading. 

### Damping

To account for energy dissipation in the system, a constand modal damping ratio $\zeta$ can be applied. Damping reduces the amplitude of vibrations over time. This damping can be introduced into the reduced modal system through the modal damping matrix $\mathbf{C}_m$, which is constructed as:

$$
C_m = 2\zeta \sqrt{M_m K_m} 
$$

Here, $M_m$, and $K_m$ are the modal mass and stiffness matrix defined above. This damping matrix enters the reduced equations of motion as:

$$
\mathbf{M}_m \ddot{q}_i(t) + \mathbf{C}_m \dot{q}_i(t) + \mathbf{K}_m q(t) = \phi_i^T \mathbf{F}_{FF}(t) 
$$

Where:

* $\mathbf{u}(t)$: Displacement vector
* $\mathbf{M}$: Mass matrix
* $\mathbf{K}$: Stiffness matrix
* $\mathbf{C}$: Damping matrix
* $\mathbf{F}(t)$: Time-dependent external loading

## Solving the Equation of Motion

To solve the governing equation $\mathbf{M} \mathbf{\ddot{x}} + \mathbf{C} \mathbf{\dot{x}} + \mathbf{K} \mathbf{x} = \mathbf{F}(t)$, one has to re-write the equation, placing the all terms involing structural acceleration on the left side, and all terms involving velocity and structural motion on the right side. This yields the following equation:

$$
\dot{q}_i(t) = v_i(t)
$$

$$
\ddot{q}_i(t) = \dot{v}_i(t) = \frac{1}{M_{m,i}} [F_i(t) - C_{m,i} \cdot v_i(t) - K_{m,i} \cdot q_i(t)]
$$

Solving this equation, using a numerical solver like those incorporated in the *scipy* python package (for example, `scipy.solve_ivp`), yields the time-dependent modal coordinates $q_i(t)$ and modal velocities $v_i(t)$, which can subsequently be used to reconstruct the global displacement $\mathbf{x}(t)$. 


## Modal Selection

Solving the full dynamic system for every possible vibration mode is computationally intensive and often unnecessary, as not all modes contribute meaningfully to the structure's response. To optimise the simulation while maintaining accuracy, a selection process is performed to identify the "dominant" modes:

1.  **Define Frequency Range:** An initial range of modes is identified based on the governing wave spectrum, specifically targeting frequencies between the lower cut-off and the spectral peak where wave energy is concentrated.
2.  **Amplitude Thresholding:** A preliminary solution is computed using all modes within this range. The average displacement amplitude for each mode is calculated, and only those exceeding a specific threshold (indicating significant energetic excitation) are retained for the final analysis.
3.  **Validation:** The accuracy of this reduced set is validated by comparing its resulting displacements against those obtained from the full set of modes. If the difference is negligible, the selection is confirmed.

This process typically favors lower-frequency modes, which is consistent with the physics of long-period swell waves that penetrate deep enough into the water column to influence the submerged structure.

## Dynamic Response Analysis

Once the dominant modes are selected and the modal equations are solved, the results are translated back into global structural behavior. This phase evaluates the safety and performance of the SFT through two main steps:

1.  **Global Displacement Reconstruction:** The global displacement vector $\mathbf{x}(t)$ is reconstructed by summing the contributions of the active modes using the equation: $\mathbf{x}(t) = \sum_{i=1}^{n} \phi_i q_i(t)$
    
2.  **Stress Computation:** The displacement field is used to compute internal stresses within the beam elements. This includes axial ($\sigma_x$), bending ($\sigma_{xy}, \sigma_{xz}$), shear ($\tau_y, \tau_z$), and torsional ($\tau_x$) stresses. These components are often combined into a **Von-Mises stress** to provide a single scalar value for checking structural capacity.

The analysis of these stresses typically reveals that bending and shear components dominate the response due to the vertical hydrodynamic loading, while axial and torsional stresses play a secondary role. Additionally, the time-history of these stresses helps verify the system's damping behavior, showing how initial oscillations decay over time.


