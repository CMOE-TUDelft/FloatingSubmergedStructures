# Fem Introduction

The Finite Element Method (FEM) is a numerical technique for solving ordinary and partial diffrential equations by dividing a domain into smaller, finite elements. This discretisation allows for the analysis of complex engineering problems like heat transfer and fluid mechanics.

In this course, the Finite Element Method is used to assess the dynamic behaviour of a Submerged Floating Tunnel (SFT) under the governing loads. To analyse the dynamic response of an SFT, one follows the following methodological steps:

1. Discretise the system into elements using one of the following assumptions:
   - Euler-Bernoulli beam Element;
   - Timoshenko beam element.

2. Assemble the global stiffness, mass and transformation matrices and provide geometric and material properties. (One can opt to integrate mooring stiffness into the global stiffness matrix at pre-determined intervals, but other methods exist as well).
3. Apply boundary conditions at the nodes.
4. Perform a modal analysis by solving the generalised eigenvalue problem, extracting the natural frequencies of the tunnel and the corresponding mode shapes.
5. Compute the Modal mass ($M_m$), stiffness ($K_m$) and damping matrices ($C_m$), using the modal damping ratio. 
6. Compute the external loads (hydrodynamic, dead load, traffic forces, earthquake's, etc.) and project these loads onto the modes. 
7. Integrate the reduces modal equations to capture the dynamic response over the simulation time, using a numerical integrator like `scipy.solve_ivp`. 
8. Select the modes that significantly contribute to the response of the tunnel, based on modal displacement amplitudes.
9. Transform these modal displacements back to global space to compute the structural response, from where stress components like axial stress, bending stress, shear stres and torsional stress can be calculated. 


:::{card} Finite Element Method
This book provides information about the application of the Finite Element Method for Floating and Submerged structures. Information in this book is derived from the book *Finite Elements in Civil Engineering and Geosciences* which can be accessed through the following link: https://teachbooks.tudelft.nl/computational-modelling/intro.html. 
:::