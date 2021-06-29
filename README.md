# bulk-pdf-to-jpg-converter
Convert a folder of pdf files to jpg image files

<h3>How to use</h3>
Once everything is setup, simply place the script in the folder containing the pdf files and run the script.<br>
The script will start converting all the pdf files in the folder it's placed in. Once all pdf files has been converted the script will create a new folder called "converted", and put the image files in it.

<h3>Needed for this to work</h3>

- Python (I used version 3.9),
- pdf2image (python library)
- Poppler (<a target="_blank" href="https://poppler.freedesktop.org/" >What is Poppler?</a>)

<h3>How to install what's needed</h3>
<h4>pdf2image</h4>Install this with the command below in the CMD (Windows)

```pip install pdf2image```
<br>
<h4>Poppler</h4>
Download a built version of poppler here <a target="_blank" href="https://github.com/oschwartz10612/poppler-windows/releases/tag/v21.03.0" >https://github.com/oschwartz10612/poppler-windows/releases/tag/v21.03.0</a> download the Release zip archieve, unpack, and place the unpacked folder somewhere convenient (consider it an installed software).<br>
Setup PATH to poppler's bin folder.
