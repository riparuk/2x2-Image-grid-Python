from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

# Name of pdf output file
pdf_file = 'foto_grid.pdf'

# Ukuran foto yang ingin digunakan
photo_width = 3.5 * inch
photo_height = 5 * inch

#reduce width and height to get space between images
photo_width_ori = photo_width-5
photo_height_ori = photo_height-5

#path folder that contains the images that you want to grid, if in current dir just type the name
folder = 'images'
#get list of images file in the folder
photo_files = os.listdir(folder)

for i in range(len(photo_files)):
    photo_files[i] = folder +'/'+ photo_files[i]
    
# Canvas initialization to create a new PDF with A4 paper size
pdf_canvas = canvas.Canvas(pdf_file, pagesize=A4)

# grid width and height
grid_width = photo_width * 2
grid_height = photo_height * 2

# Calculate the margin on each side of the PDF page
left_margin = (A4[0] - grid_width) / 2
bottom_margin = (A4[1] - grid_height) / 2

for i, img in enumerate(photo_files):
    i%=4
    if i<=1:
        i = abs(i+2)
    else:
        i = abs(i-2)
    x_offset = (i % 2) * photo_width + left_margin
    y_offset = (i // 2) * photo_height + bottom_margin 
    pdf_canvas.drawImage(img, x_offset, y_offset, width=photo_width_ori, height=photo_height_ori)
    if i==1:
        pdf_canvas.showPage() # to add new Page in the pdf

# save and close pdf file
pdf_canvas.save()
