# Diffraction Loads

When the structure is large relative to the wavelength (Regime II), the assumption that the wave field remains undisturbed ($\phi \approx \phi_I$) is no longer valid. The body **scatters** and **diffracts** the incoming waves.

In this regime, the total velocity potential $\phi$ is the sum of:
*   $\phi_I$: Incident wave potential
*   $\phi_D$: Diffraction (scattering) potential
*   $\phi_R$: Radiation potential (due to body motion)

$$
\phi = \phi_I + \phi_D + \phi_R
$$

### Diffraction Force ($F_S$)
The presence of the stationary body causes wave scattering ($\phi_D \neq 0$). The associated force is:

$$
F_S = \int_S -\rho \left( \frac{\partial \phi_D}{\partial t} \right) \vec{n}_S \, dS
$$

### Radiation Force ($F_R$)
If the structure moves, it generates its own waves, creating a radiation force:

$$
F_R = \int_S -\rho \left( \frac{\partial \phi_R}{\partial t} \right) \vec{n}_S \, dS = -m_a(\omega) \ddot{x} - c_a(\omega) \dot{x}
$$

Here, $m_a(\omega)$ is the **added mass** and $c_a(\omega)$ is the **hydrodynamic damping**.

### Equation of Motion
The total dynamic equilibrium for a large floating body is:

$$
(m + m_a(\omega))\ddot{x} + (c + c_a(\omega))\dot{x} + kx = F_h + F_{FK} + F_S
$$

Where $F_{FK} + F_S$ represents the total wave excitation force (Froude-Krylov + Diffraction).