import bpy
import os
import os
import sys

# Append to path to 
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

from render import render_img
from mask import create_mask_nodes, generate_masks
from water import Water

OUT_PATH = ""
START_INDEX = 1
END_INDEX = 854
if __name__ == "__main__":
    # Water texture
    water_text = Water("water_text")
    
    #Generate masks 
    create_mask_nodes(1, OUT_PATH)
    generate_masks(OUT_PATH, START_INDEX, END_INDEX)
    count = START_INDEX
    bpy.context.active_object.active_material = bpy.data.materials["water_text"]

    # Generate images
    for scale in range(10, 101, 30): 
        for lac in range(15, 21, 5): 
            for dimension in range(0, 2, 1): 
                for strength in range(5, 16, 5): 
                    for red in range(0, 4, 3): 
                        for green in range(6, 16, 4): 
                            for blue in range(10, 51, 7): 
                                # Change texture and render image
                                water_text.change_color(float(red/100), float(green/100), float(blue/100))
                                water_text.edit_water(scale, 1.5, dimension, 0.575, float(strength/100), 15)
                                render_img(os.path.join(OUT_PATH, "unmasked"), 0, "img-{}".format(str(count))) 
                                count += 1