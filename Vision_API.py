import os, io
from google.cloud import vision
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"VisionAPIKey.json"

client = vision.ImageAnnotatorClient()

image_path = r'C:\Python27\Image9.JPG'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

text_file = open("Image9.txt","w+")
# construct an image instance
image = vision.types.Image(content=content)

# annotate Image Response
response = client.text_detection(image=image)  # returns TextAnnotation
df = pd.DataFrame(columns=['locale', 'description'])

texts = response.text_annotations
for text in texts:
    df = df.append(
        dict(
            locale=text.locale,
            description=text.description.encode('utf-8')
        ),
        ignore_index=True
    )
text_file.write(df['description'][0])
text_file.close() 


