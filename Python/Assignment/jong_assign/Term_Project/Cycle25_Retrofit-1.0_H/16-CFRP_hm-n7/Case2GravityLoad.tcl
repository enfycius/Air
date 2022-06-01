# Case2_sample1_V01.tcl 
puts   "########################" 
puts   "# Analysis-Sequence  1 #"
puts   "########################" 


# Start of model generation 
# ========================= 

# Create ModelBuilder 
# ------------------- 
model  BasicBuilder  -ndm  3  -ndf  6 

set dataDir PushoverOutput;				# name of output folder
file mkdir $dataDir/;					# create output folder

# Define geometry 
# --------------- 
source  NodeCoord.tcl 

# Define Single Point Constraints 
# ------------------------------- 
source  SPConstraint.tcl 

# Define nodal masses 
# ------------------- 
source  NodeMass.tcl 

# Define Multi Point Constraints 
# ------------------------------ 
source  MPConstraint.tcl 

# Define material(s) 
# ------------------ 
source  Materials.tcl 

# Define section(s) 
# ----------------- 
source  Sections.tcl 

# Define geometric transformation(s) 
# ---------------------------------- 
source  GeoTran.tcl 

# Define element(s) 
# ----------------- 
source  Elements.tcl 

# Define damping parameters 
# ------------------------- 

# Define time series 
# ------------------ 
#source  TimeSeries.tcl 

# Start of analysis generation 
# ============================ 

# Get Initial Stiffness 
# --------------------- 
# initialize 

puts "o Analysis: MODAL" 
# ~~~~~~~~~~~~~~~~~~~~~~ 

# Define load pattern 
# ------------------- 
# source  LoadPattern_2.tcl 


# Analyze model 
# ------------- 
set pi [expr acos(-1.0)] 
set eigFID [open MODAL_Node_EigenVectors_EigenVal.out w] 
set lambda [eigen    12] 
puts $eigFID " lambda          omega           period          frequency" 
foreach lambda $lambda { 
    set omega [expr sqrt($lambda)] 
    set period [expr 2.0*$pi/$omega] 
    set frequ [expr 1.0/$period] 
    puts $eigFID [format " %+1.6e  %+1.6e  %+1.6e  %+1.6e" $lambda $omega $period $frequ] 
} 
close $eigFID 

# Record eigenvectors 
# ------------------- 
record 

puts "o Analysis: Gravity" 

# Define gravity loads
# --------------------

# Set a parameter for the axial load
set P 4533000.0; 

# define GRAVITY  
pattern Plain 1 "Linear" {
  load 3  0.0  0.0 [expr -$P] 0.0  0.0  0.0;		# node#, FX FY FZ MX MY MZ --  superstructure-weight
}

# Define Gravity Analysis commands
source AnalysisOptn_1.tcl

analyze 10;						# perform gravity analysis

# Print out the state of nodes 3 and 4
print node 3 
