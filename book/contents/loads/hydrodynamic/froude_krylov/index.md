# Froude-Krylov Loads

In the **large inertia regime** (Regime I), we assume:
1.  **Linear potential flow:** Higher order terms like $\frac{1}{2}|\nabla \phi|^2$ are approximately zero.
2.  **Negligible diffraction:** The presence of the body does not significantly alter the wave field ($\phi \approx \phi_I$).

Under these assumptions, the hydrodynamic force is determined solely by the pressure field of the **unperturbed incident wave**. This is known as the **Froude-Krylov force** ($F_{FK}$).

$$
F \approx F_h + F_{FK} = -\rho g S \vec{n}_z + \int_S -\rho \left( \frac{\partial \phi_I}{\partial t} \right) \vec{n}_S \, dS
$$

### Linear Wave Theory Application
Using linear Airy wave theory, the velocity potential $\phi_I$ and surface elevation $\eta_I$ are given by:

$$
\phi_I(t, x, z) = \sum_i \left[ -\frac{A_i g}{\omega_i} e^{kz} \sin(\omega_i t - kx) \right]
$$

$$
\eta_I(t, x, z) = \sum_i [A_i \cos(\omega_i t - kx)]
$$

Substituting this into the force integral gives the Froude-Krylov force component for a single wave frequency:

$$
F_{FK, i} = \int_S \rho A_i g e^{kz} \cos(\omega_i t - kx) \vec{n}_S \, dS
$$

### Small Body Approximation
If the body is very small relative to the wavelength ($kS \approx 0$), the spatial variation of the wave phase across the body can be neglected. The force simplifies to:

$$
F_{FK, i} = \rho A_i g \cos(\omega_i t) \int_S e^{kz} \vec{n}_S \, dS = \rho g \left( \int_S e^{kz} \vec{n}_S \, dS \right) \eta_{I,i}
$$

This implies the force is directly proportional to the instantaneous wave elevation and the submerged geometry.
