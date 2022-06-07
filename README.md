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
Provide a step-by-step description of how to get the development environment set and running.

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


