# Hydrodynamic Loads

Hydrodynamic loads are forces exerted on a structure due to the motion of the surrounding fluid, such as waves and currents. Unlike hydrostatic loads, which arise from static fluid pressure, hydrodynamic loads are dynamic and depend on the relative motion between the fluid and the structure.

To analyze these loads effectively, we often rely on **non-dimensional numbers**. These numbers help simplify complex physical phenomena by scaling variables and identifying dominant forces. They are independent of specific units and allow us to predict general system behavior under different conditions.

Some key non-dimensional numbers in hydrodynamics include:

| Parameter | Formula (Current $U$) | Formula (Wave $u_0$) | Phenomena |
| :--- | :--- | :--- | :--- |
| **Reynolds number** | $Re = \frac{UD}{\nu}$ | $Re = \frac{u_0 D}{\nu}$ | Ratio between inertial and viscous forces |
| **Keulegan-Carpenter number** | - | $KC = \frac{u_0 T}{D}$ | Ratio between drag and inertial forces |
| **Froude number** | $Fr = \frac{U}{\sqrt{gD}}$ | $Fr = \frac{u_0}{\sqrt{gD}}$ | Ratio between inertial and gravity forces |
| **Diffraction parameter** | - | $\frac{\pi D}{\lambda}$ | Ratio between characteristic size and wavelength |
| **Strouhal number** | $St = \frac{f_e D}{U}$ | - | Ratio between vortex shedding frequency and characteristic frequency |
| **Reduced velocity** | $V_R = \frac{U}{f_s D}$ | - | Ratio between characteristic frequency of the system and structural modal frequency |

In the following sections, we will explore the different force regimes and specific methods to calculate these hydrodynamic loads.