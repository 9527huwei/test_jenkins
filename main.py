# test jenkins auto build

import time
import pytest

localtime = time.asctime( time.localtime(time.time()) )
print(localtime)
work_runner = []
work_runner.append("-s")
work_runner.append("--alluredir")
work_runner.append("report")
pytest.main(work_runner)