### This is an example of tests for MOOC course about data analyse.

It covers task 1 in topic 2 lesson 6 about for loop usage.

Because there is no info about how user input code and user output parsed I made few assumptions and created tests based on them.

First is that user code is collected with `inspect.getsourcelines`
Second the code which is created by user is executed and piped it into the file to get the output.

That is why there are two simple helper bash scripts:
- generate_user_output.sh will execute user code and save it into `user_output.txt` file, there are 2 options: it can generate correct output with `--correct` or `-c` flag
or incorrect with `--incorrect` or `-i` flag
- generate_correct_output.sh will execute correct code and save it into correct_output.txt file

These files are used in fixtures to parse the data and execute tests.
That is why there is added a flag to pytest runner to emulate which solution type we test, `--solution-type=correct` or `--solution-type=incorrect`.

So example of test execution is very simple:
for correct solution tests execution:
  * `generate_correct_output.sh`
  * `generate_user_output.sh --correct`
  * `py.test`
  
for incorrect solution tests execution:
  * `generate_correct_output.sh`
  * `generate_user_output.sh --incorrect`
  * `py.test --solution-type=incorrect`

Notice: there is a fixture called `erase_user_output` which will erase user output at the end of test run, so if you need to debug change `autouse` flag to `False`
