# Morison Equation

In the **slender body regime** (Regime III & V), diffraction effects are negligible ($\pi D / \lambda$ is small), but flow separation can lead to significant drag forces. The **Morison equation** is an empirical formula used to calculate these hydrodynamic loads.

It assumes the total force is the sum of two components:
1.  **Inertia force ($F_i$):** Proportional to fluid acceleration. It includes both the Froude-Krylov force and the added mass effect.
2.  **Drag force ($F_d$):** Proportional to the square of fluid velocity (viscous drag).

### The Standard Morison Equation (Waves Only)
For a fixed cylinder in oscillatory flow $u(t)$:

$$
F = F_i + F_d = \rho \frac{\pi D^2}{4} C_m \dot{u} + \frac{1}{2} \rho C_d D u |u|
$$

Where:
*   $C_m$: Inertia coefficient ($C_m = 1 + C_a$). For a cylinder, theoretically $C_m = 2$.
*   $C_d$: Drag coefficient.
*   $D$: Diameter of the cylinder.
*   $u, \dot{u}$: Fluid velocity and acceleration.

### Inertia vs. Drag Dominated
*   **Large Inertia (Regime III):** When fluid acceleration dominates (low $KC$), the inertia term is more relevant.
*   **Inertia and Drag (Regime V):** When flow separation occurs (higher $KC$), both terms contribute significantly.
