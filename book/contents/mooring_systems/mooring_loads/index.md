# Mooring Loads

<iframe width="560" height="315" src="https://www.youtube.com/embed/D2dv57CpT-s?si=nEdlfAkWma7CPpHh" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Loads (actions) on a floating or submerged body can be classified as permanent, variable, environmental, or accidental.

````{dropdown} Permanent / Variable Loads
- **Hydrostatic loads:** Weight and buoyancy forces acting on the body.  
- **Ballast & variable weights:** Changes in mass distribution due to ballast adjustments or payload variations.
````
````{dropdown} Environmental Loads
- **Wind loads:** Including gusts and squalls acting on exposed surfaces.  
- **Current loads:** Steady or varying currents applying forces along the hull or mooring lines.  
- **Wave loads:**  
  - 1st order wave forces (oscillatory).  
  - 2nd order wave drift forces (slow-drift components).
````
````{dropdown} Accidental Loads
- **Impact forces:** From ships, submarines, or other floating objects.  
- **Accidental flooding/submergence:** Rapid changes in buoyancy or weight.  
- **Loss of mooring line(s):** Sudden redistribution of forces on remaining lines.
````
````{dropdown} Response Characteristics
- **Hydrostatic stiffness:** Restoring forces due to buoyancy and weight distribution.  
- **Mooring stiffness and damping:** Resistance and energy dissipation provided by mooring system.
````


<a name="catenary-equation"></a>
## 1.4 Catenary Systems

Heavy chain or cable rests partly on the seafloor, forming a classic “catenary” curve that resists horizontal movement by geometry alone. Effective for moderate water depths, but can require plenty of line length—and plenty of sea space.

> **Derivation of the Catenary Equation without stretch**  
> <details>
> <summary>Click to expand the simplified catenary formula derivation!</summary>
> 
> This derivation is taken from **OE44100: Floating Structures & Offshore Moorings by Sebastian Schreier**, in which the catenary equation is derived for a line/chain under its own weight (in water). Here, we aim for the simplified form *without* stretch, assuming no wave/current loads.
> 
> ---
> 
> ### 1. Elemental Forces & Assumptions
> We consider the following mooring element:
>
>![Mooring Element](figures/mooring_element.png)
>
> The element is part of a larger heavy mooring chain. The forces along the element are as follows (with simplifications):
> 1. **Horizontal Force Balance** in &#8594; $x$-direction: $$F_{x,i}+dF_x-F_{x,i}=0$$ 
>    Because no external horizontal forces are assumed, the horizontal component of tension 
>    $F_x$ remains **constant** along the line ($dF_x = 0$), which simplifies the equation as follows:
>    $$
>    F_{x,i+1} - F_{x,i} = 0 \quad \Rightarrow \quad F_x = \text{constant}.
>    $$
> 
> 2. **Vertical Force Balance** in &#8593; $y$-direction: $$F_{z,i}+dF_z-dm \cdot g + dF_B - F_{z,i} = 0 $$  
>    A small element $ds$ of the mooring line must support its *weight in water*:
>    $$
>    dF_z = w \, ds,
>    $$
>    where $w$ is the *submerged* weight per unit length,
>    $$
>    w = \left(1 - \frac{\rho_w}{\rho_s}\right)\mu g \quad (\text{constant along the line}),
>    $$
>    with $\mu$ = mass per unit length (in air), and $\rho_w, \rho_s$ the water and line densities, 
>    respectively.
> 
> 3. **Geometry (Slope Relationship)**  
>    By Pythagoras:
>    $$
>    ds = \sqrt{dx^2 + dz^2} = \sqrt{1 + \Bigl(\frac{dz}{dx}\Bigr)^2}\,dx.
>    $$
>    If we denote the tension’s *vertical* component by $F_z$, then near any point
>    $$
>    \frac{dz}{dx} = \frac{F_z}{F_x},
>    $$
>    because the line is flexible (no bending stiffness) and tension acts tangentially.
> 
> ---
> 
> ### 2. Setting Up the Differential Equation
> 
> From the vertical balance $dF_z = w\,ds$, we get:
> $$
> \frac{dF_z}{dx} \;=\; \frac{dF_z}{ds}\,\frac{ds}{dx} 
> \;=\; w\,\sqrt{\,1 + \Bigl(\frac{dz}{dx}\Bigr)^2}.
> $$
> But $F_z = F_x\,\tfrac{dz}{dx}$, so
> $$
> \frac{dF_z}{dx} 
> = \frac{d}{dx}\Bigl(F_x \,\frac{dz}{dx}\Bigr)
> = F_x \,\frac{d^2 z}{dx^2}.
> $$
> Thus,
> $$
> F_x\,\frac{d^2 z}{dx^2}
> = w\,\sqrt{\,1 + \Bigl(\frac{dz}{dx}\Bigr)^2}.
> $$
> 
> **Substitution**: let
> $$
> p = \frac{dz}{dx}.
> $$
> Then $\tfrac{d^2 z}{dx^2} = \tfrac{dp}{dx}$. The equation becomes
> $$
> F_x\,\frac{dp}{dx} = w \,\sqrt{1 + p^2}.
> $$
> Rearrange:
> $$
> \frac{dp}{\sqrt{1 + p^2}}
> = \frac{w}{\,F_x\,}\,dx.
> $$
> 
> ---
> 
> ### 3. First Integration: Slope
> 
> Integrate both sides:
> $$
> \int \frac{dp}{\sqrt{1+p^2}} 
> = \int \frac{w}{\,F_x\,}\,dx
> \quad\Longrightarrow\quad
> \sinh^{-1}(p)
> = \frac{w}{F_x}\,x + C_1.
> $$
> Hence,
> $$
> p \;=\; \frac{dz}{dx}
> = \sinh\Bigl(\frac{w}{F_x}\,x + C_1\Bigr).
> $$
> 
> ---
> 
> ### 4. Second Integration: Shape
> 
> Integrate once more:
> $$
> z(x)
> = \int \sinh\Bigl(\tfrac{w}{F_x} x + C_1\Bigr)\,dx.
> $$
> Recall $\int \sinh(ax+b)\,dx = \frac{1}{a}\cosh(ax+b) + \text{const}$. Thus,
> $$
> z(x)
> = \frac{F_x}{\,w\,}\;\cosh\Bigl(\tfrac{w}{F_x}x + C_1\Bigr) + C_2.
> $$
> 
> **Boundary Conditions**:  
> Typically, we set the anchor (touch-down) at $x=0$, $z=0$, and require **no vertical tension** there: 
> $$
> F_z(0) = F_x\,\left.\frac{dz}{dx}\right\vert_{x=0} = 0 
> \;\;\Rightarrow\;\; \sinh(C_1) = 0 \;\;\Rightarrow\;\; C_1 = 0.
> $$
> Then $z(0)=0$ gives:
> $$
> 0 = \frac{F_x}{\,w\,}\cosh(0) + C_2 
> \;\;\Longrightarrow\;\; C_2 = -\frac{F_x}{w}.
> $$
> 
> **Final Form**:
> $$
> \boxed{
> z(x)
> = \frac{F_x}{\,w\,}\Bigl[\cosh\Bigl(\tfrac{w}{F_x}\,x\Bigr) - 1\Bigr].
> }
> $$
> 
> This is the classic *no-stretch catenary equation* for a chain of weight $w$ per unit length, with horizontal tension $F_x$ at the anchor and reference $(x,z)=(0,0)$.
> 
> ---
> 
> ### 5. Key Observations
> 
> - **Horizontal Tension** $F_x$ is constant (no horizontal external loads).
> - **Vertical Tension** $F_z$ at a distance $x$ is $F_z = F_x\,\sinh(\tfrac{w}{F_x} x)$. 
> - **Top Tension** is highest at the fairlead because it supports the entire suspended line weight.
> - **Seabed Contact**: part of the chain may lie on the seabed if the total chain length is larger than the suspended length. 
> - This simplified approach is a great first estimate for mooring designs.
> 
> </details>