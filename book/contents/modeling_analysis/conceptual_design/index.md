# Conceptual Design

[![Watch video](https://img.youtube.com/vi/SUwH6Izh6qo/hqdefault.jpg)](https://www.youtube.com/watch?v=SUwH6Izh6qo)

Learning Objective:

_Create conceptual solutions of floating and submerged structures, with understanding of the basic physical background of the design formula and methods for different floating and submerged solutions._

## Concept Design Approach

What steps to take?
For a concept design it is important to go through several steps. (Some) steps may need to be repeated to obtain a better concept definition. 
1. Explore and establish requirements for the infrastructure design based on client and stakeholders.
2. Identify environmental conditions and basic data (traffic loads etc.) to define design basis.
3. Perform ideation; create large number of ideas and concepts and select best options for further assessment.
4. Check feasibility of various concepts based on limited engineering.
5. Review life-cycle feasibility of the concepts.
6. Select preferred concept based on in-place and life-cycle engineering assessments and project requirements. 

An example of a concept design for a floating bridge with tidal power plant:
[Example Concept Design](https://www.bridgeweb.com/Go-ahead-given-for-floating-bridge-with-tidal-power-plant/4364)

### 1. Explore and establish requirments
By defining the use of the concept, the appropriate design basis can be defined:
* Function of the concept e.g. road connection between two landfalls, train tunnen, combination, etc.
* Number of care lanes / train tracks.
* Free passage of seagoing traffic.

### 2. Define design basis
By defining the use of the concept, the appropriate design basis can be defined:
* Design life: Generally 100 years for main strcuture and 50 years for replaceable components.
* Permanent loads: Self-weight & Equipment, Buoyancy, Ballast, (if used) Tether forces, (if used) Mooring pretension, etc.
* Variable loads: Traffic, Temperature, Tides, Waves, Current, Wind, Marine fouling, etc. See chapter: [Environmental Conditions](https://github.com/CMOE-TUDelft/FloatingSubmergedStructures/tree/mooring_experiment/book/contents/env_source_characterization). 
* Accidental loads: Ship impact, Falling objects, Filling of floating body, Failure in mooring system, etc.
* Design criteria: Vertical stability, Horizontal stability, Strength / Strain limitations, maximum deflections, accelerations, Fatigue.


Apply the 100-year environmental condition with the following two factors: Ultimate Limit State (ULS) and Load and Resistance Factor Design (LRFD). Given the dynamic characteristic of the offshore structure, in this concept design, partial environmental safety factors should be applied to the extreme value stresses.

_If time allows (an) Accitental Limit State (ALS) condition(s) can be used to check the ultimate capacity of the structure._

Values which can be used for the concept design exercise: 
* Self weight based on Steel / Concrete specific weights and cross sections. Steel 77kN/m3, Concrete (reinforced): 26 kN/m3
* Road surface (100 mm) 2.5 kN/m2
* Fixed Ballast: Rock (aggregate): 20 kN/m3 or Olivine: 24 kN/m3 or Iron ore: 38 kN/m3
* Traffic loads (model LMV) lanes are loaded with 9 kN/m and all pedestrian/cycle paths are loaded with 2 kN/m concurrently.
* Ships clearance draught 20 m over a width of 400 m.
* Vertical deflection (due to traffic) 0.7 x traffic load: Approx. 1 m (or for alternative structures Length between fixed points / 300).
* Vertical acceleration 1 year storm 0.5m/s2 ,Horizontal acceleration(curved/straight bridge) 1 year storm 0.5/0.3m/s2
* For ULS look at least at ULS-weight and ULS-wave conditions with appropriate factors
* Maximum slope 5% for cars, 1.5% for trains

Extract from Feasibility study for crossing the Sognefjord - Submerged floating tunnel:

<img width="300" height="200" alt="image" src="https://github.com/user-attachments/assets/a69548f0-3d71-4273-aee0-4bdac2d01b6c" />

Reference: [Vegvesen](https://www.vegvesen.no/globalassets/vegprosjekter/utbygging/e39stordos/vedlegg/design-basis-flytebru.pdf)

### 3. Perform ideation
It is paramount to identify many alterantive concepts and evaluate these. 
Key steps in ideation:
* Define framework
* 'How can we ...' question
* Idea generation
* Select methods (COCD box)
  
  <img width="300" height="300" alt="image" src="https://github.com/user-attachments/assets/76781655-56eb-4d4e-8634-c9b6b1d891a0" />
  
   Reference: [COCD box](https://schoolofcreativethinking.nl/en/cocd-box/) and [Creative Thinking](https://elbd.sites.uu.nl/wp-content/uploads/sites/108/2017/05/2297_17_workshopcreadenkenecent12mei011.ppt.pdf)
* Combine and work out
* Enrich the selected ideas
  
  <img width="300" height="180" alt="image" src="https://github.com/user-attachments/assets/c06620e8-5133-4666-880d-b826e385c06d" />

### 4. Check Feasibility
Once several preferred concepts have been identified, these need to be verified technically. This is best done by checking vertical & horizontal stability. To do this the following steps are important:
* Define structure (diameter, support structure/stiffness)
* Calculate weight / buoyancy
* Calculate static support loads
* Calculate environmental loads (first estimate)
* Calculate variable support loads / deflections

Note: The vertical stability is mainly dependent on the static loads while horizontal stability is driven mainly by the environmental loads.

<img width="300" height="110" alt="image" src="https://github.com/user-attachments/assets/ffb22081-dc28-4b97-a8d1-80a27b461bbc" /> <img width="310" height="130" alt="image" src="https://github.com/user-attachments/assets/272e8d10-23ad-4de9-8f88-82bcb2cf9eb3" />

Reference: [icoz](https://icozct.tudelft.nl/TUD_CT/CT3109/collegestof/invloedslijnen/files/VGN.pdf) 

### 5. Life-cycle Feasibility
See Chapter: [LCA](https://github.com/CMOE-TUDelft/FloatingSubmergedStructures/tree/mooring_experiment/book/contents/design_principles/lca)

### 6. Concept Selection
Select preferred concept based on in-place and life-cycle engineering assessments and project
requirements.

## Example Case - Submerged Floating Tunnel (SFT) Sognefjorden





