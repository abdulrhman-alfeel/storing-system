import sys
import os
# import subprocess
# from wand.api import library
# import wand.color
# import wand.image
def on_KeyPress(vaule,e):
    # print(vaule.get())
    try:
        v = int(vaule.get())
    except ValueError:
        # key = ("a","s","d","f","g","h","j","k","l",";","'","q","w","e","r","t","y","u","i","o","p","[","]","z","x","c","v","b","n","m",",",".","/")
        vi = vaule.get()
        vaule.delete(0,"end")
        vaule.insert(0,vi[:-1])

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path,relative_path)



# def svg_to_png(svg_path, png_path):
#     # call the rsvg-convert command-line tool
#     # with the input svg file and the output png file
#     # subprocess.run(['rsvg-convert', '-o', png_path, svg_path])


#     with wand.image.Image() as image:
#         with wand.color.Color('transparent') as background_color:
#             library.MagickSetBackgroundColor(image.wand, 
#                                             background_color.resource) 
#         image.read(blob=svg_path.read(), format="svg")
#         png_image = image.make_blob("png32")

#     with open(png_path, "wb") as out:
#         out.write(png_image)