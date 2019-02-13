    This repository includes work accessing and analyzing the  Metropolitan Museum of Art Open Access Dataset, available at https://github.com/metmuseum/openaccess/.
    
    The flask app metApp is meant to provide a snapshop of the data.  Run the app with

    >>python metApp.py

    and the app loads on your local computer at http://localhost:5000/ (it will also tell you in the terminal the site location).  From here there are several options in drop-down boxes.  Select Department, starting and ending year range, and number of entries to display and press submit.  A pandas dataframe with the Met object information will load with these selections.  Other drop down selections can be easily added.  A unit testing file, test_metApp.py, is also included but is currently under development.

    The notebook MetDataAnalysis.ipynb contains the data checks and analysis on the dataset.  This can be opened the typical way with

    >>jupyter notebook MetDataAnalysis.ipynb