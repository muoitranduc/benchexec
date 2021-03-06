"""
BenchExec is a framework for reliable benchmarking.
This file is part of BenchExec.

Copyright (C) 2015  Daniel Dietsch
All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
import os

import benchexec.util as util
import benchexec.tools.template
import benchexec.result as result

class Tool(benchexec.tools.template.BaseTool):

    def executable(self):
        return util.find_executable('Ultimate.py')

    def version(self, executable):
        return self._version_from_tool(executable)

    def cmdline(self, bin, options, tasks, spec, rlimits):
        return [bin] + [spec] + tasks + options 

    def name(self):
        return 'ULTIMATE Kojak'

    def determine_result(self, returncode, returnsignal, output, isTimeout):
        status = result.RESULT_UNKNOWN
        for line in output:
            if line.startswith('FALSE'):
                status = result.RESULT_FALSE_REACH
            elif line.startswith('TRUE'):
                status = result.RESULT_TRUE_PROP
            elif (returnsignal == 9):
                status = 'TIMEOUT'
        return status
