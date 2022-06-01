# Case2_sample1_V01.tcl 
source Case2GravityLoad.tcl
puts "Gravity Analysis Completed"

# Set the gravity loads to be constant & reset the time in the domain
loadConst -time 0.0;				# hold gravity constant and restart time

puts "o Analysis: PUSHOVER" 

# Define LATERAL load ------------------------------------------------------
# Set some parameters
set H 10.0;		# Reference lateral load

# Set lateral load pattern with a Linear TimeSeries
pattern Plain 2 "Linear" {
#	load 88  5.0 0.0  0.0  0.0  0.0  0.0;			# node#, FX FY FZ MX MY MZ
#	load 10  10.0 0.0  0.0  0.0  0.0  0.0;	
#	load 12  10.0 0.0  0.0  0.0  0.0  0.0;	
	load 3   $H  0.0  0.0  0.0  0.0  0.0;
#	load 16  10.0 0.0  0.0  0.0  0.0  0.0;	
#	load 18  10.0 0.0  0.0  0.0  0.0  0.0;
#	load 20  10.0 0.0  0.0  0.0  0.0  0.0;	
#	load 199 5.0 0.0  0.0  0.0  0.0  0.0;
}

set	dU	0.5;	#	Displacement	increment
integrator DisplacementControl  3  1  $dU  1  $dU  $dU

# Define recorder(s) 
# ------------------ 
source  Recorder_3.tcl 


# Define Pushover Analysis commands
source AnalysisOptn_2.tcl


# pushover: diplacement-controlled static analysis
#integrator DisplacementControl 14 2 0.005;		# switch to displacement control, for node 14, dof 2, 0.005 increment

analyze	115;	#	apply	steps	of	pushover	analysis
