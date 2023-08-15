import os
import bpy

def render_img(img_dir,keyframe, name, camera_name='Camera', save_RGB=True, save_both=False, save_regular=False, max_depth=45):

    bpy.context.scene.render.engine = 'CYCLES'
    bpy.context.scene.cycles.device = 'GPU'

    if save_RGB:
        rgb_dir = os.path.join(img_dir, "RGB_imgs")
        if not os.path.exists(rgb_dir):
            os.makedirs(rgb_dir)
        # save rendered rgb img
        bpy.data.cameras[camera_name].dof.use_dof = False
        bpy.context.scene.camera = bpy.data.objects[camera_name]
        save_path = rgb_dir+"//"+str(name)+'.png'
        r = bpy.context.scene.render
        r.resolution_x = 145
        r.resolution_y = 145
        r.filepath=save_path
        bpy.ops.render.render(write_still=True)
    if save_regular:
        
        bpy.context.scene.camera = bpy.data.objects[camera_name]

        save_path = img_dir+"//"+str(keyframe)+'.jpg'
        r = bpy.context.scene.render
        r.resolution_x = 640
        r.resolution_y = 480
        r.filepath=save_path
        bpy.ops.render.render(write_still=True)