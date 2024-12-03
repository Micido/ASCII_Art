from PIL import Image
import os

charcter_reference : dict = {
    0 : Image.open("Others/Space.png").convert("RGBA"),
    1 : Image.open("Others/Dot.png").convert("RGBA"),
    2 : Image.open("Others/DotD.png").convert("RGBA"),
    3 : Image.open("Others/c.png").convert("RGBA"),
    4 : Image.open("Others/o.png").convert("RGBA"),
    5 : Image.open("Others/P.png").convert("RGBA"),
    6 : Image.open("Others/0.png").convert("RGBA"),
    7 : Image.open("Others/QM.png").convert("RGBA"),
    8 : Image.open("Others/@.png").convert("RGBA"),
    9 : Image.open("Others/#.png").convert("RGBA"),
    10 : Image.open("Others/Full.png").convert("RGBA")
}

CHAR_SIZE :int = 8
"""
NEEDED
"""
INPUT_FOLDER :str = "Input"
OUTPUT_FOLDER :str = "Output"
USED_FOLDER :str = "Used" """If None file will be left in the INPUT_FOLDER"""

def Transform(Img :Image.Image) -> Image:
    ascii = Image.new('RGB', Img.size, (0, 0, 0))
    for x in range(ascii.width//CHAR_SIZE):
            for y in range(ascii.height//CHAR_SIZE):
                rgb = Img.getpixel((CHAR_SIZE*x+(CHAR_SIZE//2), CHAR_SIZE*y+(CHAR_SIZE//2)))
                PixelBrightness = ((rgb[0]*0.3) + (rgb[1]*0.59) + (rgb[2]*0.11))
                character = charcter_reference[(PixelBrightness*10)//255]
                ascii.paste(character, (x*CHAR_SIZE, y*CHAR_SIZE), character)
    return ascii

def Transform_all(Images:list, show:bool = False) -> list: # add input, output, used as parameter
    if Images == []:
        print('No images to transform.')
        return
    i = 0
    for name in Images:
        CurrentImage : Image.Image = Image.open(f"Input/name")
        AsciiVer : Image.Image = Transform(CurrentImage)
        
        AsciiVer.save(f"{OUTPUT_FOLDER}/{name.split(".")[0]}_Ascii.png")
        
        i += 1
        
        if show:
            AsciiVer.show()
        
        if USED_FOLDER:
            os.rename(f"{INPUT_FOLDER}/{name}", f"/{name}")
        
        print(f"|{"-"*((20*i)//len(Images))}{"~"*(20-((20*i)//len(Images)))}|{(i*100)//len(Images)}%")
    print("All images transformed.")
    return

if __name__ == "__main__":
    Input_List :list = [f for f in os.listdir("Input")]
    Transform_all(Input_List)