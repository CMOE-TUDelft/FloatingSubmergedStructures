# Multi Line

In Multi-line mooring systems, the force-excursion characteristics of the single lines are combined in a total system and are dependent on the pretension in each line.

Example characteristics:
Fairlead at +200 m
2 line full chain system
Pretension 1200 kN
The resulting stiffness is (refer curve):
Kmooring = 600 / 20 = 30 kN/m


Multi-line mooring system:

Effect of restoring forces on a floating body;
Horizontal force change
Vertical force change (picking up anchor line)
Change in moments on the body (depends on position of attachment points)
New balance with external loads (position in 6 degrees of freedom) depends on hydrostatic stiffness of the floater



This shows the modeling in Orcaflex (as an example) which in the modelling includes axial spring + damper, torsional spring + damper + bending springs + dampers to fully describe the behavior. 
As such suitable for slender structures (mooring line / pipeline) including bending and torsional stiffness. It is possible to model a steel spring as well. 
In the following methods the catenary equation is used excluding bending or torsional stiffness. 


