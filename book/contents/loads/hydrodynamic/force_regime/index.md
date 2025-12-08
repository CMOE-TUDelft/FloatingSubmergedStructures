# Force Regimes

The total hydrodynamic force $F(t)$ on a submerged structure is a combination of several components:

$$
F(t) = F_h + F_d(t) + F_i(t) + F_v(t)
$$

Where:
*   $F_h$: Hydrostatic force (buoyancy)
*   $F_d(t)$: Drag force (due to flow separation)
*   $F_i(t)$: Inertia force (due to fluid acceleration)
*   $F_v(t)$: Viscous friction force (often negligible for bluff bodies)

If we neglect skin friction, the total force can be expressed as an integral of pressure over the surface $S$:

$$
F = \int_S p \vec{n}_S \, dS = \int_S -\rho \left( \frac{\partial \phi}{\partial t} + gz + \frac{1}{2}|\nabla \phi|^2 \right) \vec{n}_S \, dS
$$

The relative importance of inertia versus drag forces depends on the flow conditions and the size of the structure. This is often visualized in a **force regime diagram** (like the Chakrabarti diagram), which plots the Keulegan-Carpenter number ($KC$) against the Diffraction parameter ($\pi D / \lambda$).

There are distinct regions:
*   **Large Inertia / Diffraction:** When the structure is large relative to the wavelength ($\pi D / \lambda$ is large), diffraction effects become important.
*   **Drag & Inertia (Morison):** When the structure is slender ($\pi D / \lambda$ is small) and $KC$ is moderate to large, both drag and inertia forces matter.
*   **Drag dominated:** At very high $KC$ numbers.
*   **Inertia dominated:** At low $KC$ numbers.

:::{figure} ../../../figures/force_regimes.png
---
name: fig-force-regimes
align: center
---
Hydrodynamic force regimes based on KC number and diffraction parameter.
:::