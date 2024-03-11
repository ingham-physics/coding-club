# Building and maintaining software in (and out of the Clinic)

This tutorial aims to provide information on setting up an appropriate environment on their machines/servers for Python data science development.

## Prerequisites

### VSCode
Visual Studio Code is a Interactive Development Environment (IDE) that provides an environment where developers can build and maintain their code. For more info on the features it provides, please visit this [link](https://code.visualstudio.com/).

#### Installing VSC
- Navigate to https://code.visualstudio.com/, and download the appropriate version for your machine.

### Python installationnnnn
- Python can be downloaded here: https://www.python.org/downloads/
- For MacBooks, the tool [Homebrew](https://brew.sh/) is useful can be used to download software onto the MacOS:
    * ```brew install python```

> *Note*: for Windows, [Git Bash](https://git-scm.com/downloads) is highly advised as the guide can be followed using that terminal (either in VSC Git Bash terminals or a standlone Git Bash terminal), as the commands in this guide will work.

### Virtual environments 
Virtual environments offer a solution to managing different Python projects efficiently. This is particularily useful when different version sof Python installations or Python packages need to be tracked for different projects.

- To create a virtual environment named `.venv`:
    * ```python3 -m venv .venv```

> *Note*: please ensure that venv is installed. If the above command does not work, run ```python3 -m pip install --user virtualenv```.

- To activate your `.venv`:
    * Mac/Linux:    ```source .venv/bin/activate/```
    * Windows:          ```.venv\Scripts\Activate.bat```

### Pyenv
Installing different versions of Python can be managed easily using [Pyenv](https://github.com/pyenv/pyenv).

- To install pyenv from GitHub repo: 

    * ```curl -s -S -L https://raw.githubusercontent.com/pyenv/pyenv-installer/master/bin/pyenv-installer | bash ```

- Setup your bash profile so that pyenv is identified every time you open a new shell session: 

    * ```echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc```
    * ```echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc```
    * ```echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc```
    * ```exec "$SHELL"```

### Git/GitHub
Git is a version control tool that can be used to mantain versions of your code and track change history and code collboration efficiently. GitHub is a hosting platform that Git can interface with and host code on.

- To install Git:
    * Mac:      ```brew install git```
    * Windows:  download through this link, https://git-scm.com/download/windows

- Access GitHub [here](https://github.com/), create an account and explore creating your first repository on there. GitHub has many helpful tutorials that you can find [here](https://docs.github.com/en/get-started).

- Once you have create your GitHub account, on your machine
    * Configure with appropriate local user name and email:
        * ```git config --global user.name "YOUR FULL NAME"``` (eg. ```git config --global user.name "John Doe"```)
        * ```git config --global user.email YOUR EMAIL ADDRESS``` (eg. ```git config --global user.email johndoe@example.com```)

- VSC also has a very useful Git extension that you should utilise when developing your code. Here is a [guide](https://code.visualstudio.com/docs/sourcecontrol/overview) on it.

## Data science

Please follow the attached Jupyter notebook.

## Contact
Daniel Al Mouiee: https://www.linkedin.com/in/m-daniel-almouiee/
