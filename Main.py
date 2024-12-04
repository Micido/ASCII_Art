# MODULES
from PIL import Image
import os

character_reference : dict = {
    0 : Image.open("Character/Space.png").convert("RGBA"),
    1 : Image.open("Character/Dot.png").convert("RGBA"),
    2 : Image.open("Character/DotD.png").convert("RGBA"),
    3 : Image.open("Character/c.png").convert("RGBA"),
    4 : Image.open("Character/o.png").convert("RGBA"),
    5 : Image.open("Character/P.png").convert("RGBA"),
    6 : Image.open("Character/0.png").convert("RGBA"),
    7 : Image.open("Character/QM.png").convert("RGBA"),
    8 : Image.open("Character/@.png").convert("RGBA"),
    9 : Image.open("Character/#.png").convert("RGBA"),
    10 : Image.open("Character/Full.png").convert("RGBA")
}

# FUNCTIONS
def Transform(ImgPath:str) -> Image:
    CHAR_SIZE :int = 8
    Img = Image.open(ImgPath)
    ascii = Image.new('RGB', Img.size, (0, 0, 0))
    for x in range(ascii.width//CHAR_SIZE):
            for y in range(ascii.height//CHAR_SIZE):
                rgb = Img.getpixel((CHAR_SIZE*x+(CHAR_SIZE//2), CHAR_SIZE*y+(CHAR_SIZE//2)))
                
                PixelBrightness = ((rgb[0]*0.3) + (rgb[1]*0.59) + (rgb[2]*0.11))
                
                character = character_reference[(PixelBrightness*10)//255]
                
                ascii.paste(character, (x*CHAR_SIZE, y*CHAR_SIZE), character)
    return ascii


def Transform_all(INPUT_FOLDER:str = "Input", OUTPUT_FOLDER:str = "Output", show:bool = False, USED_FOLDER:str = None) -> list:
    """
    The parameters OUTPUT_FOLDER, INPUT_FOLDER and USED_FOLDER must be the path to a folder.\n
    If show is True all images will be shown right after being transformed.\n
    USED_FOLDER is where the images will be put after being transformed.\n
    If USED_FOLDER is None then image will be left in the provided INPUT_FOLDER.
    """
    Images = [f for f in os.listdir(INPUT_FOLDER)]
    if Images == []:
        print('No images to transform.')
        return
    nbDone = 0
    for name in Images:
        AsciiVer : Image.Image = Transform(f"{INPUT_FOLDER}/{name}")
        
        #AsciiVer.save(f"{OUTPUT_FOLDER}/{name.split(".")[0]}_Ascii.png")
        
        nbDone += 1
        
        if show:
            AsciiVer.show()
        if USED_FOLDER:
            os.rename(f"{INPUT_FOLDER}/{name}", f"/{name}")
        
        print(f"|{"-"*((20*nbDone)//len(Images))}{"~"*(20-((20*nbDone)//len(Images)))}|{(nbDone*100)//len(Images)}%")
    print("All images transformed.")
    return

# TEST
if __name__ == "__main__":
    Transform_all()