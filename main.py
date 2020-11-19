# test jenkins auto build

import time
import os
import pytest

localtime = time.asctime( time.localtime(time.time()) )
print(localtime)
work_runner = []
work_runner.append("-s")


case_mark = None
s = "-m={}".format(case_mark)
print(s)

if case_mark:
    work_runner.append("-m=%s" % case_mark)
# path_list = ['-v']
# for i in path_list:
#     work_runner.append(i)

work_runner.append("--alluredir")
work_runner.append("report")
print(work_runner)
pytest.main(work_runner)
print(os.path.abspath(__file__))