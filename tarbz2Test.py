import os
import tarfile

def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:bz2") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))

make_tarfile("/tmp/tartest.tar.bz2",  "/Users/wangliang/Study/HotPot/test")
