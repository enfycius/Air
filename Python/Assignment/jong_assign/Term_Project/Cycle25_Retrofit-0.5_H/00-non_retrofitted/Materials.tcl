# Materials.tcl 

# Material "4000Psi":    matTag    E    <eta>    <Eneg>  
uniaxialMaterial  Elastic       1  +2.485558E+04  +0.000000E+00 

# Material "A615Gr60":    matTag    E    <eta>    <Eneg>  
uniaxialMaterial  Elastic       2  +1.999480E+05  +0.000000E+00 

# Material "A992Fy50":    matTag    E    <eta>    <Eneg>  
uniaxialMaterial  Elastic       3  +1.999480E+05  +0.000000E+00 

# Material "Concrete":    matTag    E    <eta>    <Eneg>  
uniaxialMaterial  Elastic       4  +3.604997E+03  +0.000000E+00 

# Material "Pier_Confined":    matTag    fc'    epsc0    fcu'    epsu    lambda    ft    Ets 
uniaxialMaterial  Concrete02       5  -2.780000E+01  -7.000000E-03  -1.790000E+01  -2.400000E-02  +1.000000E-01  +3.270000E+00  +5.500000E+02 

# Material "Pier_Unconfined":    matTag    fc'    epsc0    fcu'    epsu    lambda    ft    Ets 
uniaxialMaterial  Concrete02       6  -2.4000E+01  -4.000000E-03  -4.800000E+00  -4.000000E-03  +1.000000E-01  +3.270000E+00  +1.220000E+03 

# Material "Steel":    matTag    E    <eta>    <Eneg>  
uniaxialMaterial  Elastic       7  +1.999480E+05  +0.000000E+00 

# Material "Steel02":    matTag          Fy             E               b              R0           cR1            cR2             <a1            a2             a3              a4>         <sig0> 
uniaxialMaterial	Steel02	8	+3.000000E+02	+2.000000E+05	+1.150000E-02	+1.850000E+01	+9.250000E-01	+1.500000E-01	+0.000000E+00	+1.000000E+00	+0.000000E+00	+1.000000E+00	+0.000000E+00

# Material "ConfinedConcrete01":     $tag  $secType $fpc   $Ec    -epscu $epscu      $nu   $L1    $phis  $S   $fyh   $Es0   $haRatio  $mu  phiLon      $cover $Am    $Sw  $ful    $Es0w    -stRatio  $stRatio
uniaxialMaterial	ConfinedConcrete01	9	C	-40.1	21900	-epscu	-0.0028194	-varub	1300.0	12.7	300.0	300.0	200000.0	0.1	10.0	28.6	-wrap	100.0	33.0	100.0	2410.0	430000.0	-stRatio	0.85

# Material "ConfinedConcrete01":     $tag  $secType $fpc   $Ec    -epscu $epscu       $nu   $L1    $phis  $S   $fyh   $Es0   $haRatio  $mu  phiLon -stRatio  $stRatio
uniaxialMaterial	ConfinedConcrete01	10	C	-40.1	21900	-epscu	-0.0028194	-varub	1300.0	12.7	300.0	300.0	200000.0	0.1	10.0	28.6	-stRatio	0.85
