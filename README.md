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
