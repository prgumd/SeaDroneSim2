# SeaDroneSim2
SeaDroneSim2 is a python script to create a parametrized, simulated ocean in Blender. The scripts take advantage of Blender's python API, bpy, to create a parametrized ocean that allows one to alter the water, waves, and camera without having to interact with Blender's physical UI. 

## Running SeaDroneSim2
First, clone SeaDroneSim2 onto your machine with the following: ```git clone https://github.com/akshajgaur/ocean-sim.git```. Then, open a new file in blender and navigate to the ```scripting``` tab. Open the ```src``` directory and view the ```main.py``` file. When opened, the file should look like this. 


```
import bpy
import sys
import os

dir = os.path.dirname(bpy.data.filepath)
if not dir in sys.path:
    sys.path.append(dir )
    
    
from water import Water
from plane import create_plane, delete_plane
from waves import Waves

def create_sim(mat, geo, size): 
    delete_plane()
    create_plane(size)
    t = Water(mat)
    t.edit_water()
    t.change_color()
    w = Waves(geo)
    
if __name__ == "__main__":

    
    create_sim("sample_mat", "sample_geo", 2)
```

To change the simulated, modify the ```create_sim()``` function. However, the function must contain at least three components no matter the modifications. First, the ```create_plane()``` function must be called to initialize the plane for the ocean. Then, a ```Water``` object must be initialized to construct the initial ocean. Finally, a ```Waves``` object must be created to create the waves. Each object has associated functions to edit certain features of the object. For example, to change the color of the water we can run the following fragment of code. 

```
# Create initial object
water = Water()

# Change color
water.change_color(10, 10, 10)
```

Similarly, we can also change features of the ```Wave``` object. To change the tilt of the waves, we can run the following fragment: 

```
# Create initial object
wave = Waves()

# Change tilt
waves.change_tilt(.4)
```

The link of the real whale dataset can be found here: https://drive.google.com/drive/folders/1PSnCZjzI8r2HYEc_uQ8sDGcIhW3EA4O3?usp=drive_link
