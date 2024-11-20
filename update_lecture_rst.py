import pandas as pd
import os
import json

courses = ["eos240", "eos408", "eos423"]

for c in courses:
    prefix = f"source/{c}-public/Lectures/"

    slides = [s for s in os.listdir(prefix) if 'slides.html' in s]
    slides.sort()
    raw = [f"{s.split('.slides')[0]}.ipynb" for s in slides]

    a = json.load(open(f'{prefix}{raw[0]}',))
    long_title = a['cells'][0]['source'][0]

    lectures = ""
    for s in slides:
        lectures += f"""{s.split('.slides')[0]}.rst
   """
        
    lecture_index = f"""Lecture slides
==========================

.. toctree::
   :maxdepth: 1

   {lectures}
"""

    with open(f"{prefix.split('Lectures/')[0]}/lectures.rst", "w+") as f:
            f.writelines(lecture_index)

    for i in range(len(slides)):
        a = json.load(open(f'{prefix}{raw[i]}',))
        long_title = a['cells'][0]['source'][0]
        slide_file=slides[i]
        s = slide_file.split('.slides')[0]
        
        slide_page = f"""{long_title}
=====================================================   

Link for full screen web viewing
------------------------------------------
Spacebar to advance, shift+spacebar to go backwards, escape for overview.

`{long_title} <../_static/{slide_file}>`_


PDF download
------------------------

:download:`{long_title} <Lectures/pdf_slides/{s}.pdf>`
"""
        with open(f"{prefix.split('Lectures/')[0]}/{s}.rst", "w+") as f:
            f.writelines(slide_page)




    