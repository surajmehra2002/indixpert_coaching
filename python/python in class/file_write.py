path = r"S:\document pdf\text_file.txt"

data="""Learn. Build. Collaborate.
Learn from experts, build groundbreaking solutions, and collaborate on exciting projects. Discover a world of new possibilities with us!
"""
with open(path,"w") as object:
    object.write(data)
    print("The file is updated/created")