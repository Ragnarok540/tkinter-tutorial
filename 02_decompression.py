import tarfile

with tarfile.open("./reviews.tar.xz", mode='r:xz') as f:
    f.extractall()
