from PIL import ImageTk ,Image
from io import BytesIO, BufferedReader

def veiw_image(filename,new=90):
        image = Image.open(filename)
        # print(image)
        width , height = image.size
        aspect_ratio = width / height
        new_width = new
        new_height = int(new_width / aspect_ratio)
        resized_imag = image.resize((new_width,new_height))

        photo = ImageTk.PhotoImage(resized_imag)
        return photo




def convert_image_buffer(image_path):
        image = Image.open(image_path)
        buffer = BytesIO()
        image.save(buffer, format="JPEG")
        image_data = buffer.getvalue()
        return image_data