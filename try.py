from PIL import Image, ImageFilter

# Open an image
image = Image.open("momina.jpg")

# Apply a blur filter
blurred_image = image.filter(ImageFilter.BLUR)

# Apply a sharpen filter
sharpened_image = image.filter(ImageFilter.SHARPEN)

# Apply an emboss filter
embossed_image = image.filter(ImageFilter.EMBOSS)

# Apply a smooth filter
smoothed_image = image.filter(ImageFilter.SMOOTH)

# Apply a detail filter
detail_image = image.filter(ImageFilter.DETAIL)

# Apply a contour filter
contour_image = image.filter(ImageFilter.CONTOUR)

# Apply a edge enhance filter
edge_enhance_image = image.filter(ImageFilter.EDGE_ENHANCE)


# Show the filtered images
# blurred_image.show()
edge_enhance_image.show()
# sharpened_image.show()
# contour_image.show()
# detail_image.show()
# embossed_image.show()
# smoothed_image.show()
