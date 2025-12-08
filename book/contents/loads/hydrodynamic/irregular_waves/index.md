# Morison for Irregular Waves & Diffraction Effects

While the Morison equation is fundamentally derived for slender bodies where diffraction is negligible, questions often arise about its applicability when diffraction starts to play a role (short wavelengths).

### Diffraction Corrections
Standard Morison forces do not account for wave scattering. However, for intermediate cases where diffraction effects are present but not dominant, modifications can be applied.

One approach is using **Newman’s approximation** or modifications to the coefficients based on diffraction theory. This allows the extension of Morison-like formulations to slightly larger bodies or shorter waves. However, for fully diffraction-dominated regimes, boundary element methods (BEM) solving the full diffraction potential $\phi_D$ are required.

<!-- >> **Note:** Detailed application of Newman's approximation is outside the scope of this course, but it is important to be aware that simple Morison theory loses accuracy as $D/\lambda$ increases. -->