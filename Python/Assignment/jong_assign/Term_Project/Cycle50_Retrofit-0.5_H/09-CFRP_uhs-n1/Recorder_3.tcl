# Recorder_2.tcl 

# Top Displacement
recorder  Node  -file $dataDir/Node3_Dsp.out  -time  -node 3  -dof 1  disp

# Displacement
recorder  Node  -file $dataDir/Node2_Dsp.out  -time  -node 2  -dof 5 disp

# Stress-strain
recorder  Element  -file $dataDir/Ele43_StressStrainConc1.out  -time  -ele 43 section 2 fiber 750 0 9 stressStrain
recorder  Element  -file $dataDir/Ele43_StressStrainConc2.out  -time  -ele 43 section 2 fiber -750 0 9 stressStrain
recorder  Element  -file $dataDir/Ele43_StressStrainConc3.out  -time  -ele 43 section 2 fiber 650 0 9 stressStrain
recorder  Element  -file $dataDir/Ele43_StressStrainSteel.out  -time  -ele 43 section 2 fiber 650 0 8 stressStrain
recorder  Element  -file $dataDir/Ele43_StressStrainSteel2.out  -time  -ele 43 section 2 fiber -650 0 8 stressStrain

# Base Shear
recorder  Node  -file  $dataDir/Node4_Rection.out    -time   -node  4   -dof  1 2 3 4 5 6 reaction