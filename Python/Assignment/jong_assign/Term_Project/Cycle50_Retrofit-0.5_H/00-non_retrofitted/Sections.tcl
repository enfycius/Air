# Sections.tcl 

# Section "Fiber_Pier":    secTag 
section  Fiber       1  { 
    # PatchCirc "Patch01":    matTag    nfcirc    nfrad    y    z    intRad    extRad    <startAng    endAng> 
	patch	circ	10	48	8	+0.000000E+00	+0.000000E+00	+0.000000E+00	+7.500000E+02	+0.000000E+00	+3.600000E+02
    # LayerCircular "Layer01":    matTag    numBar    areaBar    y    z    radius    <startAng    endAng> 
	layer	circ	8	40	+6.4242428E+02	+0.000000E+00	+0.000000E+00	+6.500000E+02	+0.000000E+00	+3.600000E+02
} 

# Section "Fiber_Pier_FRP":    secTag 
section  Fiber       2  { 
    # PatchCirc "Patch01":    matTag    nfcirc    nfrad    y    z    intRad    extRad    <startAng    endAng> 
	patch	circ	10	48	8	+0.000000E+00	+0.000000E+00	+0.000000E+00	+7.500000E+02	+0.000000E+00	+3.600000E+02
    # LayerCircular "Layer01":    matTag    numBar    areaBar    y    z    radius    <startAng    endAng> 
	layer	circ	8	40	+6.4242428E+02	+0.000000E+00	+0.000000E+00	+6.500000E+02	+0.000000E+00	+3.600000E+02
} 

# Section "Pier":    secTag    E    A    Iz    Iy    G    J    <alphaY>    <alphaZ> 
section  Elastic       3  +3.604997E+03  +1.755813E+06  +2.453297E+11  +2.453297E+11  +1.502082E+03  +4.906252E+11  +9.027646E-01  +9.027646E-01 

# Section "Pier_FRP":    secTag    E    A    Iz    Iy    G    J    <alphaY>    <alphaZ> 
section  Elastic       4  +3.604997E+03  +1.755813E+06  +2.453297E+11  +2.453297E+11  +1.502082E+03  +4.906252E+11  +9.027646E-01  +9.027646E-01 

