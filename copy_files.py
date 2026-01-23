

#copy from static in vote34 to static in info34

import shutil,os

static_vote34 = "/home/info34/vote34/mysite/static"
static_info34 = "/home/info34/mysite/static"

list_files = os.listdir(static_vote34)

for a,file in enumerate(list_files):

    src =os.path.join(static_vote34,file)
    dst =os.path.join(static_info34,file)

    print(src)
    print(dst)

    shutil.copy(src, dst)