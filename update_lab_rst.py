import os
courses = ["eos240", "eos423"]
# courses = ["eos423"]

for c in courses:
    prefix = f"source/{c}-public/Labs/"

    labs = [s for s in os.listdir(prefix) if 'Lab' in s]
    # print(labs)
    for lab in labs:
        lab_folder = prefix+lab
        file = open(f"{lab_folder}/lab_title.tex", "r")
        lab_title = file.read()
        lab_filename = lab.replace(' ','_')
         
        lab_rst = f"""{lab_title}
------------------------------------------------ 

Download PDF
*********************
:download:`{lab_title} <{lab_filename}.pdf>`

Introduction
*****************************
.. include:: introduction.rst



"""
        # print(f'writing {lab_folder}/lab.rst')
        with open(f"{lab_folder}/lab.rst", "w+") as f:
            f.writelines(lab_rst)
        




    