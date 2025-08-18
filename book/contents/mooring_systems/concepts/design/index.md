# Concept design

Design to be based on LRFD (Load and Resistance Factor Design) or partial factor design:
Considers four types of limit states:
ULS – Ultimate Limit State
SLS – Serviceability limit state
FLS – Fatigue limit state
ALS – Accidental limit state
A strength check consists of comparing a factored demand (action) on the structure with a factored strength:
Dd <= Sd  //  Dd = γg * Gc + γe * Ec // Sd = Sc / γs 

Factors of safety considerations in design codes (ISO, DNV, API, ..):
Requirements depend on the consequence of failure (ISO defines life safety and consequence classes) due to;
Loss of Human lives / Adjacent structures / Environmental impacts (e.g. oil)
Factors of safety (High impact case – Consequence class 2):
Target nominal annual probability of failure of 10-5
100 Year (Extreme) return period includes minimum FoS, ULS & ALS
DNV-ST-0119 Floating wind turbine structures: ULS γe = 1,55, γg = 1,00 for consequence class 2 
10.000 Year (Survival) return period with FoS of 1.0 – ALS - not always applied
Factors of safety (Low impact case – Consequence class 1):
Target nominal annual probability of failure of 10-4
50 Year return period includes minimum FoS
Minimum Fatigue FoS >10 for all mooring components. Corrosion allowance assumed at 50% corroded.
Consider out-of-plane bending

Frequency Domain Quasi static approach calculation of design forces:
Determine mean forces and associated excursion & stiffness:
Mean Wind
Mean Current
2nd order mean wave drift force
Determine 2nd order wave drift spectra
Calculate 2nd order excursions (NB: stiffness of system at mean offset position & line/riser damping)
At the extreme excursion add 1st order maximum wave motions
The tensions associated with these motions are the design tensions over and above the mean tension:
Maximum tension is based on maximum of either [sign 2nd order + max 1st order] or [max 2nd + sign 1st]
Next to this, engineering practice uses time domain, joint probability analysis

Importance of effect of system natural periods and 2nd order wave loads:
1st order response
Pitch response to 2nd order wave load
Surge response to 2nd order wave load (Nat period 125 s)
Example shows principle of response to 2nd order surge forces:
𝑆𝑋(𝜔)=〖𝐻(𝜔)〗^2×𝑆𝐹(𝜔)
Low damping
Stiffness/damping of mooring important for surge, sway and yaw.

Following aspects to be considered in the design:
Mooring line connection to (suction) pile and ‘inverse catenary’
Installation tolerances such as positioning inaccuracy of the anchors
Mooring line length tolerances
Effect of tensioning tolerances
Effect of loads from additional appurtenances
Torsion development over the line length during installation
What is the acceptable uplift at the anchor?
Potential for trenching of the lines (where does the line come of the seabed?)
