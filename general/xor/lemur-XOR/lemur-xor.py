from PIL import Image
import numpy as np

flag_image = Image.open("flag.png")
lemur_image = Image.open("lemur.png")

flag_np = np.array(flag_image)
lemur_np = np.array(lemur_image)

new_image_np = np.bitwise_xor(flag_np, lemur_np)
new_image = Image.fromarray(new_image_np)

# Save or display the new image
new_image.save('xor_image.png')
new_image.show()