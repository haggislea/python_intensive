# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 10:19:53 2018

@author: leann
"""

####  Command Line with Git and Python

When working on files you can use command line to save direct to GitHub, 
If ou have not made a repository on GitHub, do so.

The open up bash, finding your file by navgting your computer you are using, by typing-  cd
and where the foler or file is located ie. the desktop = cd desktop, then wherever your files is, carry on typing where the file location.

to create e new python file you will type:
    
    touch my_new_python_file.py (name of file)

the new file will be in there ready to use!

to navigte within command line


maing new directories you can use  -  mkdir and then the name of your new direcory/folder

typing pwd, tyes out the location of wher eyou are currently within command line.
typing:
    cd ..
takes you back wards, to the location before
typing just cd:
    this takes you back to the entire beginning, ie.e beginning fresh.
    you can make a clone of your github repostiroy by using:
        git clone(in here you tpye the https://filename of your github location you want to clone)
        a folder will be created
        
        to chek it is there type:
            ls, this means list
            and you will see a lsit of all files and folders within this location point

now once you are workign with your folder/files.
you can add direct to git like this:
    
    git add .
    
    this adds to a holding area stage 
    
    if you type in :
        git status:
            you will see the files/folders are green, this means they are ready to comit to git hub, if they are red it means they are not or have not been added to this area.
            
            if green:
    you can then type:
        git commit -m""      within the brackets write wht you ahve done, be explicit here.  as if you are working with others they will need to know also!!
        you can then push to git by typing:
            
            git push
            
            do double check via git hub it is receiving your pushes.

To pull code, type in pull (this should be done at the beginning of the day so you are working on so if workign in a group you are all using the latest version.)
                            type in:
                                git pull
                                to update your local directory so you can continue working
                