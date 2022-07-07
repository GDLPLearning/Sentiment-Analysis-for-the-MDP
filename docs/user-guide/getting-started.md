

In order to enjoy this project we must have at our disposal all the material it contains. 
For this reason, we have a repository in github where you will be able to know all the 
structure of the project and complementary material.

## Get the repository

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

## Create your virtual environment 

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

## Enjoy it!
After downloading all the project materials and having your virtual environment ready, it's time to enjoy it. We provide multiple resources to be able to understand, replicate and extend the project at your own pace, here is a list of the main elements you have at your disposal:

- **Presentation:** Approximately 10-minute video covering the most important points of the project, presented in a visually attractive way and suitable for all audiences.
- **Datafolio:** PDF file containing a summary of the entire project, at a glance you can learn about the key points of the project and its methodology. 
- **Report**: PDF file with a larger extension containing the report derived from the whole project development, the problem, the data sets, the exploratory analysis, the model and more are contained here, it contains visualizations and technical details.
- **Codebase:** Python files organized in folders describing each section of the project can be used to replicate the project, as a basis for extending it or for developing your own projects. 
- **Notebooks:** Jupyter notebook files inspired by Fundamental Methodology for Data Science proposed by John B. Rollins, each of them includes theory, code and visualizations to follow the project step by step.
- **Dashboard:** Application built in Dash that allows the user to interact with the visualizations generated throughout the project, while reviewing the key points in a more interactive way.
- **Documentation:** Documentation built in Read The Docs using Mkdocs, contains comments on all sections of the project so that the user understands the technical details of the libraries, modules and packages used. 