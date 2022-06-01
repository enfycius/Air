# TimeSeries.tcl 

# TimeSeries "DEAD":    tsTag    cFactor 
timeSeries  Linear       1  -factor +1.000000E+00 

# TimeSeries "RAMPTH":    tsTag    time    values    cFactor    <-useLast> 
timeSeries  Path       2  -time {0  1  4}  -values {0  1  1}  -factor +1.000000E+00 

# TimeSeries "UNIFTH":    tsTag    time    values    cFactor    <-useLast> 
timeSeries  Path       3  -time {0  1}  -values {1  1}  -factor +1.000000E+00 

