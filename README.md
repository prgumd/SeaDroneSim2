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

Similarly, we can also change the features of the ```Wave``` object. To change the tilt of the waves, we can run the following fragment: 

```
# Create initial object
wave = Waves()

# Change tilt
waves.change_tilt(.4)
```

The link of the real whale dataset can be found here: [https://drive.google.com/drive/folders/1PSnCZjzI8r2HYEc_uQ8sDGcIhW3EA4O3?usp=drive_link](https://drive.google.com/file/d/1CpmW6vBOW9xZRhbsa-dcT6lb0FGroT8p/view?usp=drive_link)
Please cite the below if you used the real dataset. Thanks to Hannah C. Cubaynes, they open-sourced their real dataset. 
```bibtext
@article{cubaynes2022whales,
  title={Whales from space dataset, an annotated satellite image dataset of whales for training machine learning models},
  author={Cubaynes, Hannah C and Fretwell, Peter T},
  journal={Scientific data},
  volume={9},
  number={1},
  pages={245},
  year={2022},
  publisher={Nature Publishing Group UK London}
}
```
The code can be found here: https://colab.research.google.com/drive/1yjfjL0ND3LQRI4N16pLLD-Sik9IdcmmU?usp=sharing

Link to paper: https://arxiv.org/abs/2308.07766

please cite our work if you find it useful!
```bibtext
@inproceedings{gaur2023whale,
  title={Whale detection enhancement through synthetic satellite images},
  author={Gaur, Akshaj and Liu, Cheng and Lin, Xiaomin and Karapetyan, Nare and Aloimonos, Yiannis},
  booktitle={OCEANS 2023-MTS/IEEE US Gulf Coast},
  pages={1--7},
  year={2023},
  organization={IEEE}
}
```
