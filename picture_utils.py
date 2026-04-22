from PIL import Image
from PIL import ImageDraw, ImageFont
from config import shablon_picture_matrix, path_to_shablon, path_to_prozrschniy_shablon

def set_wish_list_image_name(text,path_to_save):
    shablon = Image.open(path_to_shablon)
    font = ImageFont.truetype("Fonts/three.ttf",size=60)
    draw = ImageDraw.Draw(shablon)
    centre = text.center(21)

    if len(text)%2==0:
        draw.text((-57, 80), centre, font=font, fill=(0,0,0))
    else:
        draw.text((-33, 80), centre, font=font, fill=(0,0,0))

    shablon.save(path_to_save)


def crop_to_rectangle(source_picture_path, result_picture_path):

    image = Image.open(source_picture_path)
    # Отрезаем один пуксель чтобы правильно сделать квдарат
    if image.height%2==0 and image.width%2!=0 or image.height%2!=0 and image.width%2==0:
        coordinates = (0,0, image.width, image.height-1)
        image = image.crop(coordinates)

    # Если горизонтальная картинка то обрезаем с боков
    # Если вертикальная картинка, то обрещаем снизу
    if image.width>image.height:
        raznoct = (image.width-image.height)/2
        coordinates = (raznoct, 0, image.width-raznoct, image.height)
        cropped = image.crop(coordinates)
        cropped.save(result_picture_path)
        print(cropped.width)
        print(cropped.height)

    else:
        raznoct = (image.height-image.width)
        coordinates = (0, 0, image.width, image.height-raznoct)
        cropped = image.crop(coordinates)
        cropped.save(result_picture_path)
        print(cropped.width)
        print(cropped.height)


def paste_picture_to_wishlist(path_to_picture,number,path_to_wishlist):
    wishlist = Image.open(path_to_wishlist)
    image = Image.open(path_to_picture)
    prozrschniy_shablon =  Image.open(path_to_prozrschniy_shablon)
    qwer = image.resize((194,194))

    wishlist.paste(qwer,shablon_picture_matrix[number])
    qwer = Image.alpha_composite(wishlist,prozrschniy_shablon)
    
    font = ImageFont.truetype("Fonts/three.ttf",size=30)
    draw = ImageDraw.Draw(qwer)
    draw.text(shablon_picture_matrix[number], str(number), font=font, fill=(255,255,255), stroke_fill=(0,0,0), stroke_width=2)
    qwer.save(path_to_wishlist)


















# f"users_minifigures_photos/6964533009/обязянка/4.png"