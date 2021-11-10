bpy.data.window_managers["WinMan"].addon_search = "node"
bpy.data.window_managers["WinMan"].addon_search = "arch"
bpy.data.window_managers["WinMan"].addon_search = "extr"
bpy.data.window_managers["WinMan"].addon_search = ""
Cannot read file '/opt/devel/blender/mother/001.blend': No such file or directory
bpy.context.space_data.context = 'OUTPUT'
bpy.context.space_data.context = 'OUTPUT'
bpy.context.scene.render.resolution_x = 1000
bpy.context.scene.render.resolution_x = 1920
bpy.context.scene.render.resolution_y = 1000
bpy.context.scene.render.resolution_y = 1080
bpy.context.space_data.system_bookmarks_active = 0
bpy.context.space_data.params.filename = "animation.blend"
Saved "animation.blend"
bpy.ops.sequencer.image_strip_add(directory="/home/artista/3D/maria-bernade/images/", files=[{"name":"cover.png", "name":"cover.png"}], relative_path=True, show_multiview=False, frame_start=1, frame_end=26, channel=1, fit_method='FIT')
bpy.ops.transform.seq_slide(value=(7, 0))
bpy.ops.sequencer.effect_strip_add(type='TEXT', frame_start=1, frame_end=26, channel=1)
bpy.context.active_sequence_strip.text = "Maria Bernadete Micgelotti"
bpy.ops.font.open(filepath="//../../../../../usr/share/fonts/exo-2/Exo2[wght].ttf", relative_path=True)
bpy.context.active_sequence_strip.use_bold = True
bpy.context.active_sequence_strip.font_size = 30
bpy.ops.sequencer.effect_strip_add(type='COLOR', frame_start=1, frame_end=26, channel=1)
bpy.context.active_sequence_strip.color = (1, 1, 1)
bpy.context.active_sequence_strip.color = (1, 1, 1)
bpy.ops.transform.seq_slide(value=(71, 0))
bpy.context.scene.frame_end = 2750

