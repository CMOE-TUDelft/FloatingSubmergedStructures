# Mooring Experiment Guidelines: Characterization of Mooring System Stiffness for Floating Structures

## Objective

The goal of this experiment is to characterize the stiffness of a mooring system for floating structures through physical measurements and compare the experimental results with numerical model predictions.

---

## Safety Guidelines

- **Lab Access**: The experiment will be located at the *blue floor* at the Stevin Lab (Civil Engineering and Geosciences faculty, TU Delft). This location is for public access, but this is still a laboratory and special attention has to be taken to prevent accidents. Please, be careful with other setups that might be in the same location or ongoing work in the surroundings.
- **PPE (Personal Protective Equipment)**:
  - No safety shoes or lab coats are required. Please, wear confortable clothing.
  - You will work with a water tank and might to get your hands wet. Bring a small towel with you to keep things dry.
- **Electrical and Water Hazards**: Be cautious around electrical systems and water tanks. Keep instruments dry unless designed for submersion.
- **Mechanical Hazards**:
  - The loads on the structure are very small, no hazards on the experiment itself.
  - Be carful with tripping on the safety tank surrounding the water tank.
- **Emergency Procedures**: Before starting with the experiment, familiarize yourself with:
  - Location of emergency stop buttons
  - Nearest fire extinguisher
  - Emergency exits

---

## Materials Provided

The following materials will be available at your lab station:

- Scale model of a floating platform
- Synthetic mooring lines 
- Steel chain lines 
- Anchoring system (fixed points in the tank)
- Load cells
- Rulers, clamps, pulleys
- Data acquisition interface (e.g., NI DAQ or Arduino-based)
- Power supplies and USB interface cables

You do **not** need to bring your own equipment unless instructed. Notify staff immediately if any component is missing or defective.

---

## Software to Be Installed

Before the lab session, install the following software on your laptop:

- **DAQ Control & Plotting Interface**
  - Mp3 software (provided by the instructors). Note that this software only works with Windows operating systems.
  - *A python script could be made available to replace the graphic interface from Mp3*.
- **Python 3.x** with:
  - `numpy`, `matplotlib`, `pandas`, `scipy`

---

## Calibration of Measurement Instruments

Before starting the experiment:

- **Load Cells**:
  - Zero the readings with no load applied.
  - Use known weights to verify linearity and calibration curve.
  - See also chapter 'Mp3 Guidelines'.
   
- **Data Acquisition System**:
  - Check sensor connection and correct signal channel mapping.
    - Port D(1-4): red cable
    - Port E(1-4): green cable
    - Port F(1-4): white cable
    - Port G(1-4): black cable
    - yellow cable not connected
  - Set appropriate sampling rate (suggested: 10–50 Hz).

<img width="300" height="400" alt="image" src="https://github.com/user-attachments/assets/3451c019-d1a9-4324-bfb5-a626f43c3e27" />


Make a calibration set up (see picture below), record calibration data and store it for validation.

<img width="300" height="400" alt="image" src="https://github.com/user-attachments/assets/ab0c9abb-1a5d-4b7a-8c90-7460111b320c" />

---

## Experimental Setup Characterization

### Equipment
- Small-scale floating platform model
- Synthetic mooring lines (e.g., nylon)
- Anchoring system
- Load cells and displacement sensors
- Rigid frame or pulley system (for horizontal pulling tests)

### Setup Steps
1. Before connecting all the components, measure their weight (dry and wet) and lengths.
1. Connect the mooring lines to the platform.
2. Fix the anchors at known positions.
3. Connect load cells in-line with the mooring lines.
4. Attach displacement sensors to measure platform offset or mooring elongation.
5. Verify all mechanical connections and safety clamps.

Sketch the setup and label all components. Measure and note the geometry of the mooring lines (length, pretension, angle). The set up should look like the pictures below. 

<img width="300" height="400" alt="image" src="https://github.com/user-attachments/assets/90afbecb-0f72-4d4f-a9f1-fff07d3b65e1" />

<img width="300" height="400" alt="image" src="https://github.com/user-attachments/assets/60df1c9d-ab48-47d4-9a5e-e5578ed90c73" />

---

## Performing the Measurement

### Test Types
- **Quasi-static pull test**: Add weights to the pulling line incrementally (e.g., ±5-10 g) and hold position until system reaches steady state (~ 10-20 seconds at each step).
- **Free oscillation test (optional)**: Displace and release the platform, observe restoring motion and damping.

<img width="300" height="400" alt="image" src="https://github.com/user-attachments/assets/e093a8fd-cc89-454f-8581-6018968e815e" />

<img width="300" height="400" alt="image" src="https://github.com/user-attachments/assets/44db4678-8eb3-4f34-a870-a025cc031731" />


### Data to Record
- Displacement of platform in the direction of the pulling line
- Tension in each mooring line
- Time-stamped data for time-based tests

Ensure all measurements are repeated at least 3 times for repeatability.

---

## Data Processing

1. **Raw Data Cleanup**:
   - Filter noise (use low-pass filter if necessary).
   - Remove baseline offset from tension/displacement readings.

2. **Compute Mooring Stiffness**:
   - Use the relation:  
     \( k = \frac{\Delta F}{\Delta x} \)  
     where \( F \) is tension and \( x \) is displacement.

3. **Stiffness Matrix (optional)**:
   - If testing in 2D, derive the directional stiffness matrix  
     \( \mathbf{K} = \frac{\partial \mathbf{F}}{\partial \mathbf{x}} \)

4. **Plot Results**:
   - Tension vs displacement curves.
   - Hysteresis loops (if cyclic or dynamic tests are done).

---

## Comparison with Numerical Model

- Use a simplified numerical model (e.g., catenary or elastic line model).
- Input same mooring line length, pretension, material properties and geometric configuration.
- Plot numerical tension vs displacement alongside experimental.
- Discuss sources of difference: e.g., line elasticity, friction, nonlinearity.

---

## Interpretation and Discussion

Discuss the following points:
- Is the mooring system linear or nonlinear?
- Are hysteresis effects observed?
- How do boundary conditions and material choices affect stiffness?
- What is the role of pretension in mooring stiffness?
- How does stiffness relate to platform stability and motion damping?

---

## Conclusions

Summarize:
- Key findings from the stiffness characterization.
- Agreement or discrepancy with numerical models.
- Implications for design of full-scale mooring systems.
- Limitations of the lab-scale model.

---

## Appendix

- Material properties of mooring lines
- Dimensions of platform model
- Suggested reading:  
  - API RP 2SK  
  - DNV-GL RP-E301  
  - “Mooring system design for floating structures,” journal articles

