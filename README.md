# AI4ER Project Generation Cookiecutter
This cookiecutter provides a quick and easy way to create new projects for most environmental data science research projects. 

The current version of the ai4er-cookiecutter allows you to automatically set up:
1. A useful folderstructure for notebooks, source code, documentation, etc.
2. Automatically create a symlink to your data folder for easy and unified data access.
3. Automatically initialize as github repo and link to an existing (empty!) repository on github.com
4. Automatically create a new conda environment for your project and store it in the projects `/env` subdirectory. 

## Prerequisites
Please make sure that you have a working version of `python` (>= 3.0) and `cookiecutter` (>=1.7) installed.
To install cookiecutter, simply use 

```pip install --user cookiecutter```
 or 
```conda install cookiecutter```

For more information on the installation of cookiecutter, see [here](https://cookiecutter.readthedocs.io/en/1.7.2/installation.html).

## Usage
To use this cookiecutter, you simply type the following into your command line (Note: `cookiecutter` must be installed as prerequisite).
> ```cookiecutter https://github.com/ai4er-cdt/ai4er-cookiecutter.git``` 

The cookiecutter will then automatically prompt you to set project names, etc.

## Questions
For any questions, please contact [Simon Mathis](mailto:svm34@cam.ac.uk).

