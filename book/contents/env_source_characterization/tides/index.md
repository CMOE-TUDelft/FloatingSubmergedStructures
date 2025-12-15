# Tides

Unlike the stochastic and chaotic nature of waves, tides are deterministic phenomena driven by the gravitational interaction between the Earth, Moon, and Sun. While the timing of tides is highly predictable, their magnitude is heavily dependent on the local geography.

For floating tunnel design, the tide represents a slowly varying load cycle that fundamentally alters the hydrostatic equilibrium of the system once or twice a day (depending on the type of tidal cycle).


## Environmental Variation

The "Tidal Range" (the vertical difference between high and low water) is not constant across the globe; it is uniquely shaped by the local environment.
* **Open Ocean:** In deep open water, the tidal range is typically small (often less than 1 meter).
* **Estuaries and Fjords:** As the tidal wave propagates into shallower coastal waters, the energy is compressed, increasing the wave height (shoaling). In funnel-shaped estuaries or bays, the geometry can constrict the water, forcing it to pile up.
* **Resonance:** If the natural period of oscillation of a bay matches the tidal period (approx. 12.4 hours), resonance occurs, leading to massive tidal ranges.

Designers must determine the **Highest Astronomical Tide (HAT)** and **Lowest Astronomical Tide (LAT)** specific to the tunnel site to define the extreme boundaries of operation.

## Impact on Tunnel Configuration

The influence of the tide depends entirely on how the tunnel is supported. We distinguish between systems that move with the water (surface-floating) and systems that are fixed to the bottom (anchored).

### 1. Floating Tunnel with Floaters (Surface-floating)

In this configuration, the tunnel is a submerged tube suspended from surface-piercing pontoons. The defining characteristic is that the **structure wants to move vertically with the tide.**

* **Shore Connections (The "Hinge" Problem):** This is the most critical design challenge. While the main tunnel rises and falls by several meters, the landfall points are fixed concrete points. The tunnel must allow for significant flexibility or expansion joints at the ends to accommodate this vertical travel without snapping.
* **Mooring Geometry:** As the water level rises, the distance between the floating hull and the seabed anchors increases.
    * *Slack Lines:* At low tide, mooring chains may go slack, losing their restoring stiffness.
    * *Peak Tension:* At high tide, the lines are pulled taut, significantly increasing the static tension before any wave loads are applied.
    * *Footprint:* The allowable horizontal offset (sway) of the tunnel often changes depending on the tide level because the stiffness of the mooring system is non-linear and depth-dependent.

### 2. Floating Tunnel with Mooring Lines (Anchored)

In this configuration, the tunnel is submerged at a specific depth and held down by vertical tethers (tension legs) anchored to the seabed. The defining characteristic is that the **structure is fixed** and does *not* move with the tide.

* **Hydrostatic Pressure Variation:** Since the tunnel stays at a fixed elevation while the water surface rises above it, the hydrostatic pressure acting on the concrete shell fluctuates constantly.
    * *Fatigue:* This creates a predictable stress cycle every tidal change. Over a 100-year lifespan, the concrete shell must withstand these cycles, making it an important fatigue load case to consider.
