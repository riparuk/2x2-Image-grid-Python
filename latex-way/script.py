import os
import sys

def generate_latex(title, images_folder, output_filename):
    #dont using . if it is current directory
    blank_path = 'blank.png'

    # List all image files in the folder
    image_files = [f for f in os.listdir(images_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Create the LaTeX document
    latex_code = r"""
\documentclass{article}
\usepackage[margin=0cm, top=0cm, bottom=0cm, outer=0cm, inner=0cm, portrait, a4paper]{geometry}
\pagestyle{empty}

\usepackage{graphicx}
\usepackage{subfig}
\usepackage{titling}

% Remove space before and after the title
\pretitle{\begin{center}\LARGE\bfseries}
\posttitle{\par\end{center}}

% Remove space before and after the author
\preauthor{}
\postauthor{}

% Remove space before and after the date
% \predate{}
% \postdate{}

"""

    latex_code += f"\\title{{{title}}}"

    latex_code += r"""
\author{}
\date{}

\begin{document}

% Adjust left and right margins specifically for the title
\newgeometry{left=2cm, right=2cm}

"""


    # Split image files into groups of 4
    image_groups = [image_files[i:i+4] for i in range(0, len(image_files), 4)]

    
    count = 0
    # Add figure environments for each group
    for i, image_group in enumerate(image_groups):

        # Add blank image_grup kurang dari 2
        while len(image_group) < 4:
            image_group.append(blank_path)

        latex_code += "\\begin{figure}\n"

        if i == 0:
            latex_code += r"""
\maketitle
\vspace*{-10pt}
\thispagestyle{empty} % Remove page numbers
"""

        latex_code += r"""
\captionsetup[subfigure]{labelformat=empty}
\captionsetup{labelformat=empty}
\centering\hfill
"""

        # Add subfloats for each image in the group
        for y, image_file in enumerate(image_group):
            if image_file == blank_path:
                latex_code += f" \\subfloat[][]{{\\includegraphics[width=0.4\\textwidth, height=8cm]{{{blank_path}}}}}"
            else:
                latex_code += f" \\subfloat[][]{{\\includegraphics[width=0.4\\textwidth, height=8cm]{{{images_folder}/{image_file}}}}}"
            count += 1
            if (y + 1) % 2 == 0:
                latex_code += "\\hfill\\null\\\\\n\\hfill\n"
            else:
                latex_code += "\\hspace{0.5cm}\n"

        # End the figure environment
        # latex_code += r"\hfill\null"
        latex_code += "\\end{figure}\n\n"

    # Restore the original geometry settings
    latex_code += r"\restoregeometry"
    latex_code += r"\end{document}"

    # Write the LaTeX code to the output file
    with open(output_filename, 'w') as f:
        f.write(latex_code)

    print("Total Img : ", count)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <title> <images_folder> <output_filename>")
        sys.exit(1)

    title, images_folder, output_filename = sys.argv[1], sys.argv[2], sys.argv[3]
    generate_latex(title, images_folder, output_filename)
