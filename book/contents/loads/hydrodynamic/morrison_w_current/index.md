# Morison Equation with Current

In real offshore environments, waves often coexist with a steady current $U$. Furthermore, if the structure is flexible or floating, it moves with velocity $\dot{x}$ and acceleration $\ddot{x}$. The Morison equation must be adapted to account for relative velocities.

### Current and Waves (Fixed Structure)
The total fluid velocity is $u_{total} = U + u(t)$. The drag force depends on the total velocity:

$$
F = \rho \frac{\pi D^2}{4} C_m \dot{u} + \frac{1}{2} \rho C_d D (u(t) + U) |u(t) + U|
$$

Note that the inertia term depends only on the wave acceleration $\dot{u}$, as the steady current has zero acceleration.

### Current, Waves, and Moving Structure
When the structure itself moves, we use the **relative velocity formulation** for the drag term and adjust the inertia term for the added mass effect on the structure's acceleration.

$$
F = \rho \frac{\pi D^2}{4} \dot{u} + \rho \frac{\pi D^2}{4} C_a (\dot{u} - \ddot{x}) + \frac{1}{2} \rho C_d D (u + U - \dot{x}) |u + U - \dot{x}|
$$

This can be regrouped as:

$$
F = \underbrace{\rho \frac{\pi D^2}{4} C_m \dot{u}}_{\text{Wave Inertia}} - \underbrace{\rho \frac{\pi D^2}{4} C_a \ddot{x}}_{\text{Added Mass}} + \underbrace{\frac{1}{2} \rho C_d D v_{rel} |v_{rel}|}_{\text{Relative Drag}}
$$

where $v_{rel} = u(t) + U - \dot{x}$.