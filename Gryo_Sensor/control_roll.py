#psedocode for controlling the rocket roll
#assumes that the x-axis will face the nosecone

# as this is pseudocode, do not attempt to run this yet.

# @author Drew Bowman
# @version 02.24.20

x_coord = []
y_coord = []
z_coord = []

def control_roll(axis x, axis y, axis z):
    # need at least two points of reference in order to determine which
    # way the rocket is rotating, if at all.
    # called every physics tick
    
    x_coord += x
    y_coord += y    #add the current orientation to the arrays
    z_coord += z
    
    if len(x_coord) >= 3:
        x_slope = x_coord[len(x_coord)-1] - x_coord[len(x_coord) - 2]
        y_slope = y_coord[len(y_coord)-1] - y_coord[len(y_coord) - 2]
        z_slope = z_coord[len(z_coord)-1] - z_coord[len(z_coord) - 2]
        
        x_concav = x_slope - (x_coord[len(x_coord)-2] - x_coord[len(x_coord) - 3])
        y_concav = y_slope - (y_coord[len(y_coord)-2] - y_coord[len(y_coord) - 3])
        z_concav = z_slope - (z_coord[len(z_coord)-2] - z_coord[len(z_coord) - 3])
        
#        compare first and second derivatives of the change of y

        if y_slope > 0.25: #value of y is increasing
            if y_concav > 0:    #slope is increasing
                # move y in the opposite direction
            elif y_concav < -0.25: # the movement of y is slowing down
                # move y slightly in the direction it is already going
        elif y_slope < -0.25: #value of y is decreasing
            if y_concav < 0:    #slope is decreasing
                # move y in the opposite direction
            elif y_concav > 0.25:
                # move y slightly in the direction it is already going
        
                
            
            
        
                
            

