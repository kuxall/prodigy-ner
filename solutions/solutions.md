### Problem 1 ###
**DLL load failed: The specific module could not be found. (VSCODE) #15183  or
ImportError: DLL load failed while importing numpy_ops: The specified module could not be found.**

    This error message indicates that there is a problem with the installation of the numpy package in Python. The specific problem is that the numpy_ops dynamic link library (DLL) is missing, which is preventing the package from being imported. This can happen if the package is not installed correctly, or if a dependency is missing. To fix this issue, you should try reinstalling numpy, making sure that all dependencies are met, and ensure that you are using the correct version of numpy for your version of Python.

    Steps carried to solve this problem :

        1. Install conda by downloading the Anaconda distribution from the official website (https://www.anaconda.com/    products/distribution/) and following the installation instructions.

        2. Open the Conda in an integrated terminal of Vscode.
        3. Create a Virtual Env thorugh Conda:
                conda create --name .venv

        4. Activate the virtual environment by typing:
                conda activate .venv

        5.Verify that the virtual environment is active by checking the prefix in the command prompt, it should change from 
            (base) to (.venv)   

        6. Once the virtual environment is active, you can install packages using the conda install command. For example, to
           install numpy, you can type:
            
            a. if pip is installed on machine:
                    install all the freezed requirements using pip through following command:
                        pip install -r requirements.txt i.e. requirements.txt is a file 

            b. if numpy is to install using conda then:
                    conda install numpy



