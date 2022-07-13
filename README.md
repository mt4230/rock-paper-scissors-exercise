# rock-paper-scissors-exercise
Setup
Repo Setup
Use the GitHub online interface to create a new remote project repository called something like "rock-paper-scissors-exercise". When prompted by the GitHub online interface, let's get in the habit of adding a "README.md" file and a Python-flavored ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. After this process is complete, you should be able to view the repo on GitHub at an address like https://github.com/YOUR_USERNAME/rock-paper-scissors-exercise.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

cd ~/Desktop/rock-paper-scissors-exercise
Use your text editor or the command-line to create a file in that repo called "game.py", and then place the following contents inside:

# this is the "game.py" file...

print("Rock, Paper, Scissors, Shoot!")
Make sure to save Python files like this whenever you're done editing them. After setting up a virtual environment, we will be ready to run this file.

Environment Setup
NOTE: if you want, you could do this exercise in the "base" environment! Otherwise, for more practice, we could use a project-specific environment. And certainly if your app ends up requiring any third-party packages, we'll need to use the project-specific environment.

Create and activate a new project-specific Anaconda virtual environment:

conda create -n my-game-env python=3.8 # (first time only)
conda activate my-game-env
From within the virtual environment, demonstrate your ability to run the Python script from the command-line:

python game.py