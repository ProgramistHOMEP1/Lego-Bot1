from PIL import Image
from PIL import ImageDraw, ImageFont
from config import shablon_picture_matrix, path_to_shablon, path_to_prozrschniy_shablon

# sours_shablon = Image.open("Sistemimages/шаблонО3.png")
# prozrschniy_shablon =  Image.open("Sistemimages/Прозрачный шаблон.png")
# shablon = Image.open("Sistemimages/шаблонО3.png")
# image = Image.open("users_minifigures_photos/6964533009/Любимое/1.png")
# qwer = image.resize((194,194))
# shablon.paste(qwer,(0,1203)) #Верхняя часть для текста равняется 255 пукселей

# image = Image.open("users_minifigures_photos/6964533009/Любимое/6.png")
# qwer = image.resize((194,194))
# shablon.paste(qwer,(0,1201)) #Верхняя часть для текста равняется 255 пукселей

# image = Image.open("users_minifigures_photos/6964533009/Любимое/5.png")
# qwer = image.resize((194,194))
# shablon.paste(qwer,(203,408)) #Верхняя часть для текста равняется 255 пукселей

# image = Image.open("users_minifigures_photos/6964533009/Любимое/4.png")
# qwer = image.resize((194,194))
# shablon.paste(qwer,(203,210)) #Верхняя часть для текста равняется 255 пукселей

# image = Image.open("users_minifigures_photos/6964533009/Любимое/3.png")
# qwer = image.resize((194,194))
# shablon.paste(qwer,(406,210)) #Верхняя часть для текста равняется 255 пукселей

# image = Image.open("users_minifigures_photos/6964533009/Любимое/1.png")
# qwer = image.resize((194,194))
# shablon.paste(qwer,(603,210)) #Верхняя часть для текста равняется 255 пукселей


# image = Image.open("users_minifigures_photos/6964533009/Любимое/0.png")
# qwer = image.resize((194,194))
# shablon.paste(qwer,(801,210)) #Верхняя часть для текста равняется
# # shablon.paste(prozrschniy_shablon,(0,400))
# qwer = Image.alpha_composite(shablon,prozrschniy_shablon)
# qwer.save("rezult.png")


# Обернуть код вставки картинки на шаблон в функцию

# Функция будет принимать Путь до картинки, которую вставлять и номер, на которой вставлять


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



# shablon = Image.open("rezult.png")
# font = ImageFont.truetype("Fonts/three.ttf",size=30)
# draw = ImageDraw.Draw(shablon)

# draw.text(shablon_picture_matrix[2], "2", font=font, fill=(255,255,255), stroke_fill=(0,0,0), stroke_width=2)

# shablon.save("rezult2.png")


# paste_picture_to_wishlist(
#     path_to_picture="users_minifigures_photos/6964533009/Любимое/4.png",
#     number=1,
#     path_to_wishlist="rezult.png"
# )
# paste_picture_to_wishlist(
#     path_to_picture="users_minifigures_photos/6964533009/Любимое/6.png",
#     number=2,
#     path_to_wishlist="rezult.png"
# )
# paste_picture_to_wishlist(
#     path_to_picture="users_minifigures_photos/6964533009/Любимое/3.png",
#     number=3,
#     path_to_wishlist="rezult.png"
# )
paste_picture_to_wishlist(
    path_to_picture="users_minifigures_photos/6964533009/Любимое/5.png",
    number=5,
    path_to_wishlist="rezult.png"
)


# def set_wish_list_image_name(path_to_template,text,path_to_save):
#     shablon = Image.open(path_to_template)
#     font = ImageFont.truetype("Fonts/three.ttf",size=60)
#     draw = ImageDraw.Draw(shablon)
#     centre = text.center(21)

#     if len(text)%2==0:
#         draw.text((-30, 80), centre, font=font, fill=(0,0,0))
#     else:
#         draw.text((0, 80), centre, font=font, fill=(0,0,0))

#     shablon.save(path_to_save)

# set_wish_list_image_name(path_to_template="Sistemimages/шаблон.png",text="Spongebobb",path_to_save="rezult.png")



