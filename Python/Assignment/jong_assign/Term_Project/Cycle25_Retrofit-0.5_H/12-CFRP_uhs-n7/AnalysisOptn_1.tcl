# AnalysisOptn_2.tcl 

# AnalysisOptn Gravity load
# ------------------------------------------------ 
# Constraint Handler 
constraints Transformation;		# how it handles boundary conditions
numberer RCM;						# renumber dof's to minimize band-width (optimization)
system BandGeneral;			# how to store and solve the system of equations in the analysis (large model: try UmfPack)
test NormDispIncr 1.0e-5 100;	# tolerance, max iterations
algorithm Newton;					# use Newton's solution algorithm: updates tangent stiffness at every iteration
integrator LoadControl 0.1; 	# determine the next time step for an analysis, # apply gravity in 10 steps
analysis Static;					# define type of analysis static or transient


