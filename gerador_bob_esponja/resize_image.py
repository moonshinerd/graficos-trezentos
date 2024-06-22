## PngResizeTransparency.py
#
## Resize PNG image by keeping the transparency
## thanks to https://stackoverflow.com/users/1453719/nicolas-barbey
#
## Use:
##   - using a reference file to get new sizes:
#        PNG_ResizeKeepTransparency(SourceFile, ResizedFile, RefFile ='YourRefFile.png')
##   - using only the resized width:
#        PNG_ResizeKeepTransparency(SourceFile, ResizedFile, new_width)
##   - using resized width and hight:
#        PNG_ResizeKeepTransparency(SourceFile, ResizedFile, new_width, new_height)
##   - using resample mode: add param resample="NEAREST"/"BILINEAR"/"BICUBIC"/"ANTIALIAS"

from PIL import Image

def PNG_ResizeKeepTransparency(SourceFile, ResizedFile, new_width=0, new_height=0, resample="ANTIALIAS", RefFile =''):
    # needs PIL
    # Inputs:
    #   - SourceFile  = initial PNG file (including the path)
    #   - ResizedFile = resized PNG file (including the path)
    #   - new_width   = resized width in pixels; if you need % plz include it here: [your%] *initial width
    #   - new_height  = resized hight in pixels ; default = 0 = it will be calculated using new_width
    #   - resample = "NEAREST", "BILINEAR", "BICUBIC" and "ANTIALIAS"; default = "ANTIALIAS"
    #   - RefFile  = reference file to get the size for resize; default = ''
    
    img = Image.open(SourceFile) # open PNG image path and name
    img = img.convert("RGBA")    # convert to RGBA channels
    width, height = img.size     # get initial size

    # if there is a reference file to get the new size
    if RefFile != '':
        imgRef = Image.open(RefFile)
        new_width, new_height = imgRef.size
    else:
        # if we use only the new_width to resize in proportion the new_height
        # if you want % of resize please use it into new_width (?% * initial width)
        if new_height == 0:
            new_height = new_width*width/height

    # split image by channels (bands) and resize by channels
    img.load()
    bands = img.split()
    # resample mode
    if resample=="NEAREST":
        resample = Image.NEAREST
    else:
        if resample=="BILINEAR":
            resample = Image.BILINEAR
        else:
            if resample=="BICUBIC":
                resample = Image.BICUBIC
            else:
                if resample=="ANTIALIAS":
                    resample = Image.ANTIALIAS
    bands = [b.resize((new_width, new_height), resample) for b in bands]
    # merge the channels after individual resize
    img = Image.merge('RGBA', bands)
    # save the image
    img.save(ResizedFile)
    return

#######################################################

if __name__ == "__main__":
    sFile = './autumn-png-leaf.png'
    # resize using new width value (new height is calculated by keeping image aspect)
    PNG_ResizeKeepTransparency(sFile, sFile[:-4]+'_resized.png', 400)
    # resize using a reference file to get the new image dimension 
    PNG_ResizeKeepTransparency(sFile, sFile[:-4]+'_resized.png', RefFile = 'autumn-png-leaf_starry-night-van-gogh_fchollet_10.png')