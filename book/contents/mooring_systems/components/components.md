## 2. Components
Chains, wire ropes, synthetic lines—each has trade-offs in terms of strength, flexibility, corrosion resistance, and cost. Connectors, such as shackles and fairleads, form the critical links (literally) between segments

A mooring system consists of several key components:

- **[Foundations](https://en.wikipedia.org/wiki/Offshore_embedded_anchors)**  
- **Connection elements** (chains, wires, connectors)  
- **Floaters and their attachments** (fairleads, winches, etc.)

---

### 2.1 Foundations

Mooring lines aren’t much use without a secure anchor point. Anchors, piles, or suction caissons must be chosen according to seabed properties (clay, sand, rocky terrain) and load requirements. An anchor designed for soft clay might underperform in a rocky seabed.

Mooring foundations transfer loads from the mooring lines into the seabed. Common foundation types include:


1. **Gravity Anchor**  
   - Relies on its own weight to resist loads.  
   - Can be cumbersome for installation or removal if very large.

2. **Driven Pile**  
   - Offers high capacity for both vertical and horizontal loads in a wide range of soil conditions.  
   - Typically installed by impact driving (noise concerns).  
   - Not easily removed.

3. **Drag Anchor**  
   - Most efficient in cohesive soils (though also used in sands).  
   - Provides primarily horizontal capacity.  
   - Easy to install and remove.

4. **Suction Pile**  
   - Uses differential pressure to embed into the seabed; suited for certain soil types.  
   - Offers high horizontal capacity; vertical capacity depends on soil conditions.  
   - Generally easy to install and remove.

5. **Torpedo Pile**  
   - Deployed by free-fall, penetrating the seabed via kinetic energy.  
   - Common in deep water, soft to medium clay conditions.  
   - Provides both vertical and horizontal capacity.

6. **Vertical Load Anchor**  
   - Ideal for layered soft clays; provides horizontal and vertical capacity.  
   - Easy installation and removal.

**Figure 1 – Foundation Types**  
![Foundation Types](foundations.png)  
*Reference: [Mooring System Engineering for Offshore Structures](https://www.sciencedirect.com/book/9780128185513/mooring-system-engineering-for-offshore-structures)*

**Figure 2 – Foundations and their respective depths**  
![Foundations and their respective depths](figures/foundation_depths.png)  
*Reference: [Anchor geotechnics for floating offshore wind: Current technologies and future innovations](http://dx.doi.org/10.1016/j.oceaneng.2023.114327)*

#### Example Foundation Parameters for Floating Wind

- **Driven Pile**: Diameters up to 12 m, L/D up to 60, Horizontal & Vertical efficiency ~12–100 (Force/Mass).  
- **Drag Anchor**: Ultimate Holding Capacity (UHC) for a 30 mT Stevpris Mk5 can be ~1700 mT in sand/hard clay[^1], Horizontal efficiency ~30–300.  
- **Suction Pile**: Diameter ≤16 m, L/D ≤1 (sand) or 8 (clay), Horizontal efficiency ~50–250, Vertical ~9–100.

[^1]: Reference: *Vryhof Anchor Manual*.

---

<a name="connection-foundation-to-floater"></a>
### 2.2 Connection Foundation to Floater

- **Chain (Studless, Studlink)**  
  - Offers robust and flexible connections.  
  - High weight and good wear resistance.

- **Steel Spiral Strand Wire Rope**  
  - Lighter than chain.  
  - More prone to corrosion; higher cost.

- **Synthetic Wire Rope**  
  - Materials: Polyester, Nylon, HMPE (High Modulus PolyEthylene), Aramid.  
  - High strength, low submerged weight.  
  - Cost-efficient relative to steel wire in terms of strength/weight ratio.  
  - Fatigue-resistant for tension cycling.  
  - Subject to **visco-elastic behavior** (stiffness depends on load rate and temperature).  

```{note}
Design/analysis of fiber ropes often follow [DNV-RP-E305](https://rules.dnv.com/docs/pdf/DNV/en/standards/RP-E305.pdf) guidelines, considering upper and lower bound stiffness in mooring calculations.
```

**Floater Attachments**  
- **Fairleads / Hull Connection**: Guides mooring lines from the floater.  
- **Mooring Winches**: Tension control and line adjustment.  
- **Connector Systems**: In-line tensioners, pull-in connectors, intermediate line connectors.

---

<a name="system-approaches"></a>
## 1.3 System Approaches

A mooring system often combines several single-line moorings or a grid-based approach to form a **restoring system**. Common examples:

1. **Multi-Line Mooring System**  
   ![Multi-line mooring system](figures/multi_line.png)

2. **Body-to-Body Line Systems**  
   ![Body to body line systems](figures/body_to_body.png)

3. **Wishbone System**  
   ![Wishbone system](figures/wishbone.png)

4. **Tension Leg System**  
   ![Tension leg system](figures/tension_leg.png)

Each configuration has its own advantages based on site conditions, project requirements, and cost considerations.
