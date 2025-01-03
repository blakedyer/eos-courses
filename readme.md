general workflow:

master goes live on readthedocs
dev branch live and hidden on readthedocs

if you change outline files, the html needs to be updated with a script:
update the html builds of outline files with `python update_outlines.py`

if you add/rename/change lectures:
update the rst structure for lectures with `python update_lecture_rst.py`

to push slides from ipynb to revealjs:
update the slides for all courses with `bash update_slides.sh`



if you add/rename/change labs:
update rst targets from tex with `python update_labtex_to_rst.py`
update the rst structure for labs with `python update_lab_rst.py`

todo:
master script that runs all 5 above

to checkout a file from dev branch (ie pull the file with committed changes over to master):
commit on dev
go to master, then:
git checkout origin/dev -- testing.txt
where testing.txt is the filepath

try this approach for updating lecture slides from dev to master