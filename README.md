# bulk-pdf-to-jpg-converter

<h3>What does it do</h3>
The script will convert all the pdf files in the folder it's placed in to jpg image files. Once all pdf files has been converted the script will create a new folder called "converted", and put the image files in it.

<h3>How to use</h3>
Simply run the script in the folder containing the pdf files.<br>

<h3>Setup (Easy way)</h3>

- If you don't have python you can use `winget install Python.Python.3.11` in CMD or powershell to install python 3.11
- Launch the setup.bat file to install the needed modules for this to work (<a target="_blank" href="https://scoop.sh/" >Scoop</a> is needed for poppler).

<sub>If you do not have scoop installed <a href="https://thomrl.github.io/thomrl/">here's how to install it</a>.</sub>

<h3>Needed for this to work</h3>

- Python (I used version 3.11.2)
- pdf2image (python library)
- Poppler (<a target="_blank" href="https://poppler.freedesktop.org/" >What is Poppler?</a>)


<h3>How to manually install what's needed (The hard way)</h3>
<h4>pdf2image</h4>Install this with the command below in the CMD (Windows)

```pip install pdf2image```
<br>
<h4>Poppler</h4>
Download a built version of poppler here <a target="_blank" href="https://github.com/oschwartz10612/poppler-windows/releases/tag/v21.03.0" >https://github.com/oschwartz10612/poppler-windows/releases/tag/v21.03.0</a> download the Release zip archieve, unpack, and place the unpacked folder somewhere convenient (consider it an installed software).<br>
Setup PATH to poppler's bin folder.






