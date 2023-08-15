import bpy

class Water: 
    def __init__(self, mat_name="water-text"):

        # Select plane and create new material
        self.obj = bpy.data.objects['Plane']
        if bpy.data.materials.get(mat_name):
            self.water = bpy.data.materials.get(mat_name)
        else:     
            self.water =  bpy.data.materials.new(mat_name)
        self.water.use_nodes = True
        print("Hlhflsdkhlsdkhfklshf")
        # Create nodes
        self.tree = self.water.node_tree
        self.bsdf = self.tree.nodes.get("Principled BSDF")  
        self.musgrave = self.tree.nodes.new('ShaderNodeTexMusgrave')
        self.bump = self.tree.nodes.new('ShaderNodeBump')
        self.musgrave.location = (-500,100)
        self.bump.location = (-300,100)
        
        # Add links
        self.links = []
        self.links.append(self.tree.links.new(self.bsdf.inputs["Normal"], self.bump.outputs["Normal"]))
        self.links.append(self.tree.links.new(self.bump.inputs["Height"], self.musgrave.outputs["Fac"]))

    def hex_to_rgb(hex_value):
        """Convert a hex value to its rgb equivalent"""
        b = (hex_value & 0xFF) / 255.0
        g = ((hex_value >> 8) & 0xFF) / 255.0
        r = ((hex_value >> 16) & 0xFF) / 255.0
        return r, g, b
    
    def edit_water(self, scale=79, lac=.2, dimension=.8, metallic=.85, strength=.19, detail=2):
        """Change the texture of the water"""

        self.musgrave.inputs["Scale"].default_value = scale
        self.musgrave.inputs["Dimension"].default_value = dimension
        self.musgrave.inputs["Lacunarity"].default_value = lac
        self.bsdf.inputs["Metallic"].default_value = metallic
        self.bump.inputs["Strength"].default_value = strength
        self.musgrave.inputs["Detail"].default_value = detail
        
    def change_color(self, red=0.06, green=0.14, blue=6.33, alpha=5.4):
        """Change the color of the water given rgb value"""
        self.bsdf.inputs[0].default_value = (red, green, blue, alpha)
    
    def change_hex_color(self, hex_value, alpha=1):
        """Change the color of the water given hex value"""
        b = (hex_value & 0xFF) / 255.0
        g = ((hex_value >> 8) & 0xFF) / 255.0
        r = ((hex_value >> 16) & 0xFF) / 255.0
        self.bsdf.inputs[0].default_value = (r, g, b, alpha)