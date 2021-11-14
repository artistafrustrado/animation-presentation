#!/usr/bin/python

import os, sys
import json
import bpy

#with open('images.json', 'w') as json_file:
#    json.dump(images, json_file)

class AnimationBuilder:

        def __init__(self):
            self.__json_file = "../media.json"
            self.__json_file = "/home/artista/3D/maria-bernade/media.json"
            
            self.__frameStart = 0
            self.__frameEnd = 0
            self.__imageDirectory = "/home/artista/3D/maria-bernade/images"            
            self.__assetsDirectory = "/home/artista/3D/maria-bernade/assets"

            self.__backgroundChannel = 0
            self.__imageChannel = 2
            self.__subtitlesBackgroundChannel = 3
            self.__subtitlesChannel = 4

            self.__textPositionX = 0
            self.__textPositionY = 0

        def setup(self):
            bpy.context.scene.render.resolution_x = 1920
            bpy.context.scene.render.resolution_y = 1080

            bpy.context.scene.render.engine = 'BLENDER_EEVEE'
            bpy.context.scene.eevee.use_gtao = True
            bpy.context.scene.eevee.use_ssr = True
            bpy.context.scene.eevee.use_motion_blur = True
            bpy.context.scene.render.film_transparent = True

            bpy.context.scene.view_settings.look = 'Medium Contrast'
             
            area = bpy.context.area
            old_type = area.type
            area.type = 'SEQUENCE_EDITOR'

        def __addMovies(self, image):
                pass

        def __addAudio(self, image):
                pass
        
        def __addSounstrack(self, image):
                pass

        def __addImages(self, image):
            area = bpy.context.area
            old_type = area.type
            area.type = 'SEQUENCE_EDITOR'

            bpy.ops.sequencer.image_strip_add(
                    directory = self.__imageDirectory,
                    files = [{"name": image["image"]}], 
                    relative_path = True, show_multiview = False, 
                    frame_start = self.__frameStart, frame_end = self.__frameEnd, 
                    channel = self.__imageChannel, fit_method = 'FIT')                    
            bpy.context.active_sequence_strip.blend_type = 'ALPHA_OVER'
            area.type = old_type 

        def __addSubitlesBackground(self, frameStart, frameEnd):
            area = bpy.context.area
            old_type = area.type
            area.type = 'SEQUENCE_EDITOR'
            
            bpy.ops.sequencer.image_strip_add(
                    directory = self.__assetsDirectory, 
                    files = [{"name": "subtitles.png"}], 
                    relative_path = True, show_multiview = False, 
                    frame_start = frameStart, frame_end = frameEnd, 
                    channel = self.__subtitlesBackgroundChannel,
                    fit_method = 'FIT')

            area.type = old_type 
            bpy.context.active_sequence_strip.blend_type = 'ALPHA_OVER'

        def __addSubtitle(self, frameStart, frameEnd, image):
            bpy.context.active_sequence_strip.text = image["subtitle"]
            bpy.ops.font.open(filepath="/usr/share/fonts/exo-2/Exo2[wght].ttf", 
                relative_path=True)
            bpy.context.active_sequence_strip.use_bold = True
            bpy.context.active_sequence_strip.font_size = 30

        def __addBackground(self, frameStart, frameEnd):
            area = bpy.context.area
            old_type = area.type
            area.type = 'SEQUENCE_EDITOR'
            print("+ Add Background")
            bpy.ops.sequencer.effect_strip_add(
                    type = 'COLOR', frame_start = frameStart, frame_end = frameEnd, 
                    channel = self.__backgroundChannel)
            bpy.context.active_sequence_strip.color = (1, 1, 1)
#            bpy.context.active_sequence_strip.blend_type = 'ALPHA_OVER'
            area.type = old_type 

        def run(self):
            
            self.setup()
            file = open(self.__json_file,"r")
            json_str = file.read()
            file.close()

            images = json.loads(json_str)

            #print(images)
            for image in images:
                print(image)
                self.__frameStart = self.__frameEnd 
                self.__frameEnd = self.__frameEnd + image["duration"]
                if image["type"] == "image":
                    self.__addImages(image)
                if image["type"] == "movies":
                    sef.__addMovies(image)
                if image["type"] == "audio":
                    sef.__addAudio(image)
                if image["type"] == "soudtrack":
                    sef.__addSoundtrack(image)

            bpy.context.scene.frame_end = self.__frameEnd 
            self.__addSubitlesBackground(self.__frameStart, self.__frameEnd)
            self.__addBackground(self.__frameStart, self.__frameEnd)

if __name__ == "__main__":
    ani = AnimationBuilder()
    ani.run()
