import os

#User prompt to get the following information
name = input("What is the name of the project?\n\n")
desc = input("Describe the project in a few sentences\n\n")
installation = input("How do you install this project?\n\n")
usage = input("Describe how to use this project?\n\n")
license = input("What license is this project under?\n\n")
contributing = input("Are there any guidelines for contributing to this project?\n")

#Generate the readme.md file
with open("README.md", "w") as f:
    #Project name
    f.write("# " + name + "\n\n")

    #Project description
    f.write("\n## Description \n" + desc + "\n\n")

    #Installation instructions
    f.write("\n## Installation \n" + installation + "\n\n")

    #Usage instructions
    f.write("\n## Usage \n" + usage + "\n\n")

    #License
    f.write("\n## License \n" + license + "\n\n")

    #ReadME Generation
    f.write("This ReadME file was created by MakeME, an open source readME file generator manufactured with OpenAI\n\n\n")


print("README.md has been generated in the current directory.")