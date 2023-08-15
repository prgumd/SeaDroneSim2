import bpy 

class Waves:
    def __init__(self, name="waves"): 
        
        # Initialize basic metadata geometry nodes
        self.obj = bpy.context.object
        self.geo.name = name

        # Create geometry node group
        bpy.context.area.ui_type = 'GeometryNodeTree'
        bpy.ops.node.new_geometry_nodes_modifier()
        self.geo = bpy.data.node_groups["Geometry Nodes"]
        
        # Create basic geo nodes
        
        self.in_node = self.geo.nodes.get('Group Input')
        self.out_node = self.geo.nodes.get('Group Output')
        self.set_pos = self.geo.nodes.new("GeometryNodeSetPosition")
        self.pos = self.geo.nodes.new(type="GeometryNodeInputPosition")
        
        self.pos_noise = self.geo.nodes.new(type="GeometryNodeInputPosition")
        self.noise_tex = self.geo.nodes.new(type="ShaderNodeTexNoise")
        self.noise_tex.noise_dimensions = '2D'
         
        # Initialize math nodes
        self.mult = []
        
        for _ in range(6):
            temp = self.geo.nodes.new('ShaderNodeMath')
            temp.operation = 'MULTIPLY'
            self.mult.append(temp)
            
        self.add = [self.geo.nodes.new('ShaderNodeMath'), self.geo.nodes.new('ShaderNodeMath')]
        self.add[0].operation = "ADD"
        self.add[1].operation = "ADD"
        self.sub = self.geo.nodes.new('ShaderNodeMath')
        self.sub.operation = "SUBTRACT"
        self.cos = self.geo.nodes.new('ShaderNodeMath')
        self.cos.operation = "COSINE"
        self.sin = self.geo.nodes.new('ShaderNodeMath')
        self.sin.operation = "SINE"
        
        self.combined = self.geo.nodes.new('ShaderNodeCombineXYZ')
        self.separate = self.geo.nodes.new('ShaderNodeSeparateXYZ')
        
        # Basic links
        self.links = []
        self.links.append(self.geo.links.new(self.in_node.outputs[0], self.set_pos.inputs[0]))
        self.links.append(self.geo.links.new(self.set_pos.outputs[0], self.out_node.inputs[0]))
        self.links.append(self.geo.links.new(self.pos.outputs[0], self.separate.inputs[0]))
        self.links.append(self.geo.links.new(self.combined.outputs[0], self.set_pos.inputs["Offset"]))
        
        
        # Create actual wave
        self.mult[0].inputs[1].default_value = 6.28
        dr = self.sub.inputs[1].driver_add("default_value")
        dr.driver.expression = "frame/48"
        
        self.links.append(self.geo.links.new(self.separate.outputs[0], self.add[0].inputs[0]))
        self.links.append(self.geo.links.new(self.sub.inputs[0], self.add[0].outputs[0]))
        self.links.append(self.geo.links.new(self.sub.outputs[0], self.mult[0].inputs[0]))
        
        # Control number of waves with these links and self.mult[0]
        self.links.append(self.geo.links.new(self.mult[0].outputs[0], self.cos.inputs[0]))
        
        
        # Control height of waves with self.mult[1]
        self.mult[1].inputs[1].default_value = 0.25
        self.links.append(self.geo.links.new(self.mult[0].outputs[0], self.sin.inputs[0]))
        self.links.append(self.geo.links.new(self.mult[1].inputs[0], self.cos.outputs[0]))
        self.links.append(self.geo.links.new(self.combined.inputs[2], self.mult[5].outputs[0]))
        self.links.append(self.geo.links.new(self.mult[5].inputs[0], self.mult[1].outputs[0]))
        
        
        # Control sharpness of waves with self.mult[2]
        self.mult[2].inputs[1].default_value = -0.12
        self.links.append(self.geo.links.new(self.mult[2].inputs[0], self.sin.outputs[0]))
        self.links.append(self.geo.links.new(self.add[1].inputs[0], self.mult[2].outputs[0]))
        self.links.append(self.geo.links.new(self.combined.inputs[0], self.add[1].outputs[0]))
        
        
        #self.mult[3] controls tilt
        self.mult[3].inputs[1].default_value = 0.19
        self.links.append(self.geo.links.new(self.mult[3].inputs[0], self.cos.outputs[0]))
        self.links.append(self.geo.links.new(self.mult[3].outputs[0], self.add[1].inputs[1]))
        
        
        # Create texture for waves
        self.links.append(self.geo.links.new(self.pos_noise.outputs[0], self.noise_tex.inputs["Vector"]))
        self.links.append(self.geo.links.new(self.noise_tex.outputs["Fac"], self.mult[4].inputs[0]))
        self.links.append(self.geo.links.new(self.mult[4].outputs[0], self.add[0].inputs[1]))
        self.links.append(self.geo.links.new(self.noise_tex.outputs["Fac"], self.mult[5].inputs[1]))
        
        self.noise_tex.inputs["Scale"].default_value = 0.73
        self.noise_tex.inputs["Detail"].default_value = 7.10
        self.mult[4].inputs[1].default_value = 1.08
        bpy.context.area.ui_type = 'TEXT_EDITOR'

    def change_height(self, height=0.25):
        """Change the height of the wave"""
        self.mult[1].inputs[1].default_value = height
        
    def change_num_waves(self, num=6.28):
        """Change the number of waves"""
        self.mult[0].inputs[1].default_value = num
    
    def change_sharpness(self, sharpness=-0.12):
        """Change the sharpness of the waves"""
        self.mult[2].inputs[1].default_value = sharpness

    def change_tilt(self, tilt=0.19):
        """Change the tilt of the wave"""
        self.mult[3].inputs[1].default_value = tilt

    def change_texture(self, scale=0.73, detail=7.10, tex=1.08):
        """Change the texture of the wave"""
        self.noise_tex.inputs["Scale"].default_value = scale
        self.noise_tex.inputs["Detail"].default_value = detail
        self.mult[4].inputs[1].default_value = tex