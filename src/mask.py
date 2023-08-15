import bpy
import os


def create_mask_nodes(pass_ind, file_out): 

    # Find correct context
    bpy.context.scene.use_nodes = True
    

    bpy.context.area.ui_type = 'CompositorNodeTree'
    tree = bpy.context.scene.node_tree

    # Create nodes
    render_node = tree.nodes.new(type='CompositorNodeRLayers')
    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.view_layers["ViewLayer"].use_pass_object_index = True
    mask_node = tree.nodes.new(type='CompositorNodeIDMask')
    output_node = tree.nodes.new(type='CompositorNodeOutputFile')

    # Create links
    tree.links.new(render_node.outputs["IndexOB"], mask_node.inputs[0])
    tree.links.new(mask_node.outputs["Alpha"], output_node.inputs[0])

    # Set Attributes
    tree.nodes["ID Mask"].index = pass_ind
    tree.nodes["File Output"].base_path = file_out

def generate_masks(path, start, end):
    
    # Generate single render
    path = "/Users/akshajgaur/Documents/Spring\ 2023/Outside/imgs/masked"
    r = bpy.context.scene.render
    r.resolution_x = 145
    r.resolution_y = 145
    bpy.ops.render.render()

    # Copy masks for all images
    ret_code = os.system("for i in {%s..%s}; do cp %s %s; done" % (start, end, os.path.join(path, "masked" "Image0001.png"),  os.path.join(path, "masked", "img-$i-mask.png")))
    if ret_code: 
        print("Error in generating masks...")
        exit(1)






