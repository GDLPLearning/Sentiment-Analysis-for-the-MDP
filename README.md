# Sentiment analysis in Twitter for the Medellin Development Plan

*Project repository - 'Sentiment Analysis in Twitter for the Medellin Development Plan' by group 247 of the 6th cohort of DS4A Colombia.*


![Sentiment-Analysis-for-the-MDP](https://socialify.git.ci/GDLPLearning/Sentiment-Analysis-for-the-MDP/image?description=1&font=Raleway&forks=1&issues=1&language=1&name=1&owner=1&pattern=Plus&pulls=1&stargazers=1&theme=Light)
https://socialify.git.ci/
## Add shields io badges
Shields.io
## Project Description

### Business problem and solution approach
The Medellín Development Plan (MDP) 2020 - 2023 is the local government proposal that seeks to guarantee comprehensive 
attention to the needs of Medellín's citizens, care for vulnerable populations, economic reactivation, the construction 
of a sustainable city and the generation of opportunities based on a major educational transformation.
In other words, it is a promise of public policies by the mayor's office in order to improve the welfare of the people 
they represent by trying to meet the needs that afflict them. But are these in tune with the proposals presented in the 
city's development plan? This is what this project will try to answer, for which it will divide the analysis into two 
components:

1. Is the MDP aligned with the needs expressed by the population?

    * In this first component, the main problems expressed by the inhabitants of Medellin prior to the entry into force 
      of the MDP will be identified and it will check if these are part of the development plan.
    * To solve this question a text analysis of information extracted will be performed from Twitter (needs) and MDP 
      (proposals) to check if there is any relationship between them.
    

2. What is the perception of citizens in relation to MDP programs and projects during the government's term?
    * The response of the citizens of Medellin in relation to this topic will be analyzed through a sentiment analysis based on the perception exposed by the inhabitants on Twitter in relation to these projects and programs of the MDP.


## Table of Contents 


## Project Demo

## Project Screenshots

## How to Install and Run the Project


In order to enjoy this project we must have at our disposal all the material it contains. 
For this reason, we have a repository in github where you will be able to know all the 
structure of the project and complementary material.

### Get the repository

There are two easy ways to download the entire contents of the repository, just do one of the two:

- Create a directory where you want to save the project, after that, enter the following link [Sentiment-Analysis-for-the-MDP](https://github.com/GDLPLearning/Sentiment-Analysis-for-the-MDP)
On GitHub.com, navigate to the main page of the repository, and click the `code` button and then `Download ZIP`.

- Set the path where you want to place the proyect, Open Git Bash there and then enter the following lines of code:


```
mkdir folder_project_name  # You can give any name to your folder

# Change the current working directory to the location where you want the cloned directory. 
cd folder_project_name  

git clone https://github.com/GDLPLearning/Sentiment-Analysis-for-the-MDP.git
```

### Create your virtual environment 

To avoid incompatibilities between libraries and future errors when executing the project, we recommend isolating your work 
environment by creating a virtual environment, in this section we will use Anaconda, however, if you master another way to 
create virtual environments (e.g.`venv`) feel free to do so. 

1. Download the Anaconda installer at the following link [Anaconda](https://www.anaconda.com/products/distribution), once you have 
you have chosen the distribution that fits your operating system or your preference.
2. Once downloaded, run the installer and follow the recommended installation process.
3. Open the anaconda prompt.
4. Make sure you have the latest version of conda installed with the command `conda update conda`.
5. To view the list of available python versions type the command `conda search “^python$”`.
9. To create the virtual environment type `conda create -n envname python=x.x anaconda` and replace `envname`with the name that you want to assign to your environment and replace `x.x` with the version of python you want to use, we recommend using python 3.8 version or lower than 3.9 `python=3.8.13`.
10. To see the list of all the available environments use command `conda info -e`.
11. To activate the virtual environment, enter the given command and replace your given environment name with envname `conda activate envname`.
12. Once the environment is activated, go to the path where you downloaded the project and set the path there.
13. The repository contains a text file `requirements.txt` containing all the packages and libraries as well as their versions necessary for the proper execution of the project. To install them type `pip install -r requirements.txt`.
14. If your virtual environment is enabled you can install additional packages using `pip install package` or `conda install package` replace package with the name of the package to install.
14. To close the virtual environment type `conda deactivate`. Remember to re-activate it every time you want to interact with the project. 
15. If you no longer require a virtual environment. Delete it using the following command and replace your environment name with envname `conda remove -n envname -all`.

### Enjoy it!
After downloading all the project materials and having your virtual environment ready, it's time to enjoy it. We provide multiple resources to be able to understand, replicate and extend the project at your own pace, here is a list of the main elements you have at your disposal:

- **Presentation:** Approximately 10-minute video covering the most important points of the project, presented in a visually attractive way and suitable for all audiences.
- **Datafolio:** PDF file containing a summary of the entire project, at a glance you can learn about the key points of the project and its methodology. 
- **Report**: PDF file with a larger extension containing the report derived from the whole project development, the problem, the data sets, the exploratory analysis, the model and more are contained here, it contains visualizations and technical details.
- **Codebase:** Python files organized in folders describing each section of the project can be used to replicate the project, as a basis for extending it or for developing your own projects. 
- **Notebooks:** Jupyter notebook files inspired by Fundamental Methodology for Data Science proposed by John B. Rollins, each of them includes theory, code and visualizations to follow the project step by step.
- **Dashboard:** Application built in Dash that allows the user to interact with the visualizations generated throughout the project, while reviewing the key points in a more interactive way.
- **Documentation:** Documentation built in Read The Docs using Mkdocs, contains comments on all sections of the project so that the user understands the technical details of the libraries, modules and packages used. 

## How to Use the Project
You can also make use of visual aids by including materials like screenshots to show examples of the running project and also the structure and design principles used in your project.

Also if your project will require authentication like passwords or usernames, this is a good section to include the credentials.


## Technologies used

## Tests

## Documentation 

## Credits
If you worked on the project as a team or an organization, list your collaborators/team members. You should also include links to their GitHub profiles and social media too.

Also, if you followed tutorials or referenced a certain material that might help the user to build that particular project, include links to those here as well.


## License
https://choosealicense.com/


## Contribution Guidelines

https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors

## Support

If you are having issues, please let us know. We have a mailing list located at: project@google-groups.com

Project Organization
------------

    ├─ LICENSE
    ├── Makefile            <- Makefile with commands like `make data` or `make train`
    ├── README.md           <- The top-level README for developers using this project.
    ├── data
    │    ├── external       <- Data from third party sources. 
    │    ├── final          <- Data after training the model
    │    ├── interim        <- Intermediate data that has been transformed.
    │    ├── processed      <- The final, canonical data sets for modeling.
    │    └── raw            <- The original, immutable data dump.
    │
    ├── docs                <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models              <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks           <- Jupyter notebooks. Naming convention is a number (for ordering),
    │    │                       the creator's initials, and a short `-` delimited description, e.g.
    │    │                       `1.0-jqp-initial-data-exploration`.
    │    │
    │    ├── exploratoy     <- Contains initial explorations
    │    └── reports        <- More polished work that can be exported as html to the reports directory.
    │
    ├── references          <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports             <- Generated analysis as HTML, PDF, LaTeX, etc.
    │    └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt    <- The requirements file for reproducing the analysis environment, e.g.
    │                          generated with `pip freeze > requirements.txt`
    │
    ├── setup.py            <- Makes project pip installable (pip install -e .) so src can be imported
    ├── src                 <- Source code for use in this project.
    │   ├── __init__.py     <- Makes src a Python module
    │   │
    │   ├── data            <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features        <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models          <- Scripts to train models and then use trained models to make
    │   │   │                  predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization   <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    ├── tests               <-  Store tests
    ├── __init__.py         <-  Make tests a Python module 
    ├── test_process.py     <-  Test functions for process.py
    ├── test_train_model.py <-  Test functions for train_model.py
    │
    └── tox.ini             <-  Tox file with settings for running tox; see tox.readthedocs.io


--------


