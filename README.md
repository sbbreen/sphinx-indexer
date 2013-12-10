sphinx-indexer
==============

Overview of capabilities:

A customizable indexing framework for a set directory built using sphinx. Compatable with Wordpress for search through the Invicto plugin (not yet tested). 

This indexer is designed for use in situations where total recall of the query is of primary importance. It is specialized for cases in which the issued query may not be an exact match of the entire desired results. The indexer is designed to index terms alongside synonyms, closely matching terms, and manually input related terms so that at retrieval, the user has a better chance at total recall of relevant results. 

The system is built on the Sphinx indexing package. Follow the steps below for installation on a Linux Ubuntu machine, or as documented on the sphinx website for other supported platforms. 


Sphinx can be added from the PPA repository: 

    $ sudo add-apt-repository ppa:builds/sphinxsearch-daily 
    
    $ sudo apt-get update
    
Install/update sphinxsearch package: 

    $ sudo apt-get install sphinxsearch
    
Sphinx searched function can be stopped and started with the following command:

  	$ sudo service sphinxsearch start
  	
This repository is focused on the indexing mecahnisms of the sphinx package. As the sphinx package is large, we have not cloned all of the files into this repository. The files we have worked with come from the build/sphinx/sphinx/util folder of the sphinxsearch paakage. To utilize this project, replace the stemmer.py docstrings.py and tags.py

    $ build/sphinx/sphinx/util

The subdirectory sphinx is the main working module within the sphinx search package. 




