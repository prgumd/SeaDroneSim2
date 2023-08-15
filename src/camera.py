import bpy
from render import render_img

# Force Enter the Object Mode
try:
    bpy.ops.object.mode_set(mode = 'OBJECT')
except:
    pass

def set_light(x=0,y=0,z=60,energy=50000):
    # Select all the lights:
    bpy.ops.object.select_by_type(type='LIGHT')

    # Delete all the lights:
    bpy.ops.object.delete()

    bpy.ops.object.light_add(type='POINT', radius=1, align='WORLD', location=(x,y,z), scale=(1, 1, 1))
    # bpy.context.space_data.context = 'DATA'
    bpy.context.object.data.energy = energy



def set_camera(x=0, y=0, z=2, roll=0, pitch=0, yaw=0, track=False, focal_length=36):

    # creates a new camera object at x,y,z, roll, pitch, yaw
    bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(x, y, z),\
     rotation=(roll, pitch, yaw), scale=(1, 1, 1))

    if track:
        bpy.ops.object.constraint_add(type='TRACK_TO')
        bpy.context.object.constraints["Track To"].target = bpy.data.objects["BlueROV"]
    bpy.context.object.data.lens = focal_length

    return bpy.context.object.name, bpy.context.object


def loop_camera(out, name, start_x, end_x, start_y, end_y, start_z, end_z):
    count = 0
    for i in range(start_x, end_x): 
        for j in range(start_y, end_y): 
            for k in range(start_z, end_z): 
                obj = bpy.data.objects['Camera'] # bpy.types.Camera
                obj.location.x = i
                obj.location.y = j
                obj.location.z = k
                render_img(out, count, name)
                count += 1 
               

def loop_light(out, name, start_x, end_x, start_y, end_y, start_z, end_z):
    count = 0
    for i in range(start_x, end_x): 
        for j in range(start_y, end_y): 
            for k in range(start_z, end_z): 
                obj = bpy.data.objects['Light'] # bpy.types.Camera
                obj.location.x = i
                obj.location.y = j
                obj.location.z = k
                render_img(out, count, name)
                count += 1