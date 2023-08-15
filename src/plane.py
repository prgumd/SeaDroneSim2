import bpy
import os
import sys 



def del_cube(): 
    """Delete the default cube"""
    cube = bpy.data.objects['Cube']
    bpy.data.objects.remove(cube, do_unlink=True)

def create_plane(size=4):
    """Create plane for ocean"""

    # Create plane
    bpy.ops.mesh.primitive_plane_add(size=size, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

    plane = bpy.data.objects['Plane']
    bpy.context.view_layer.objects.active = plane
    
    # Create subdivision for waves
    plane.modifiers.new(type='SUBSURF', name="Subdivision")
    plane.modifiers["Subdivision"].subdivision_type = 'SIMPLE'
    plane.modifiers["Subdivision"].use_limit_surface = False
    plane.modifiers["Subdivision"].levels = 7
    plane.modifiers["Subdivision"].render_levels = 7

if __name__ == "__main__":

    # Parse arguments for output file
    argv = sys.argv
    try: 
        argv = argv[argv.index("--") + 1:] 
    except ValueError: 
         print("Usage: blender -b --python plane.py -- [output file with .blend]")
         exit(1)

    # Check if argumentsa are valid
    if len(argv) != 1 or not argv[0].endswith(".blend"): 
        print("Usage: blender -b --python plane.py -- [output file with .blend suffix]")
        exit(2)

    # Create plane for ocean and save blender file
    save_dir = os.path.join(os.getcwd(), argv[0])
    del_cube()
    create_plane()
    bpy.ops.wm.save_as_mainfile(filepath=save_dir)