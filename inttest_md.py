import md
import sys
import os

md.run_md()

if os.path.exists('cu.traj'):
    print("cu.traj exits")
else:
    print("cu.traj does not exist")
    sys.exit(1)
