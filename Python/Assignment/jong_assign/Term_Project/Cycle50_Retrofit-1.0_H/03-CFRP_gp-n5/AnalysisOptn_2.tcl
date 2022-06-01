# AnalysisOptn_2.tcl 

# AnalysisOptn "PushoverStaticDefault": Type: Static
# ------------------------------------------------ 
# Constraint Handler 
	constraints Transformation;					# how it handles boundary conditions
	numberer RCM;							# renumber dof's to minimize band-width (optimization)
	system SparseGeneral;						# how to store and solve the system of equations in the analysis (large model: try UmfPack)
	test NormDispIncr 0.5e-0 1000; # tolerance, max iterations
	algorithm NewtonLineSearch;			# use Newton's solution algorithm: updates tangent stiffness at every iteration
	#integrator DisplacementControl  3  1  1
	#integrator LoadControl  0.1
	analysis Static;						# define type of analysis: static for pushover
