from PIL import Image, ImageDraw

# # Criar um ícone simples de certificado
# icon_size = (256, 256)
# icon = Image.new("RGBA", icon_size, (255, 255, 255, 0))

# draw = ImageDraw.Draw(icon)
# draw.rectangle([64, 64, 192, 192], outline="black", width=4)
# draw.line([64, 96, 192, 96], fill="black", width=4)
# draw.line([64, 128, 192, 128], fill="black", width=4)
# draw.line([64, 160, 192, 160], fill="black", width=4)

# # Salvar o ícone como arquivo .ico
# ico_path = "certificate_icon.ico"
# icon.save(ico_path, format="ICO")

# print(f"Ícone salvo como {ico_path}")

# Abra o arquivo PNG de entrada
input_image = Image.open("static/images/logo_branca.png")

# Salve a imagem como ICO
input_image.save("static/images/icon/logo.ico")
