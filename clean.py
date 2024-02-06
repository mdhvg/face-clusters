import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Directory structure required:
# imgs/
#   - person1/
#       - image1.jpg
#       - image2.jpg
#   - person2/
#       - image1.jpg
#       - image2.jpg
# but output should also be:
# imgs/
#   - person1/ (or directory name that actually contains images)
#       - image1.jpg
#       - image2.jpg
#   - person2/ (or directory name that actually contains images)
#       - image1.jpg
#       - image2.jpg
# this is because the directory name is used as the label for the images


IMGDIR = "imgs"

for file in os.listdir(IMGDIR):
    if not os.path.isdir(os.path.join(IMGDIR, file)):
        os.makedirs(os.path.join(IMGDIR, "loose"), exist_ok=True)
        os.rename(os.path.join(IMGDIR, file), os.path.join(IMGDIR, "loose", file))

for subdir in os.listdir(IMGDIR):
    print(subdir)
    if os.path.isdir(os.path.join(IMGDIR, subdir)):
        for subsubdir in os.listdir(os.path.join(IMGDIR, subdir)):
            print(subsubdir)
            if os.path.isdir(os.path.join(IMGDIR, subdir, subsubdir)):
                for file in os.listdir(os.path.join(IMGDIR, subdir, subsubdir)):
                    os.makedirs(os.path.join(IMGDIR, subsubdir), exist_ok=True)
                    os.rename(
                        os.path.join(IMGDIR, subdir, subsubdir, file),
                        os.path.join(IMGDIR, subsubdir, file),
                    )
        os.rmdir(os.path.join(IMGDIR, subdir, subsubdir))
    os.rmdir(os.path.join(IMGDIR, subdir))

os.makedirs("useless", exist_ok=True)

for dir in os.listdir(IMGDIR):
    for file in os.listdir(f"{IMGDIR}/{dir}"):
        if not file.endswith(".jpg") or not file.endswith(".png"):
            os.rename(f"{IMGDIR}/{dir}/{file}", f"useless/{file}")
