#################################
####   Homework 2 - 2/8/22   ####
####    Valentina Alaasam    ####


### documenting steps to upload HW1 to github online repository

cd Desktop
mkdir DataScience2022   # Making directory on my computer desktop
cd DataScience2022     
git init                # intitialize this folder as a repo
git checkout -b main    # change to 'main' branch
cp ../HW1_VJA.docx .    # copy homework from desktop (one level up) to current directory  
git add HW1_VJA.docx    # adding hw1 to 'staging area', not yet committed
git commit -m "Submitting hw1 to github" #committing and commenting on addition

### create corresponding folder on github webpage
### use code and url provided to connect the two 
git remote add origin https://github.com/valaasam/DataScience2022.git 
git push -u origin main


### commit and push HW2 writeup
nano HW2_VJA.docx  # added this file and saved it
git add HW2_VJA.docx
git commit -m "Adding HW2 text file - writeup"
git push -u origin main







