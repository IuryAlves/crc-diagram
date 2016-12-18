# How to contribute to CRCDiagram

1. [Contributing Guide](#contributing)
2. [Running tests](#running_tests)

## Running tests <a name='contributing'></a>

### First of all, thanks for contributing :tada: :tada: :tada:

#### **Did you find a bug?**

* **Ensure the bug was not already reported** by searching on GitHub under [Issues](https://github.com/IuryAlves/CRCDiagram/issues).

* If unable to find an open issue addressing the problem, [open a new one](https://github.com/IuryAlves/CRCDiagram/issues/new). Be sure to include a **title and clear description**, as much relevant information as possible, and a **code sample** or an **executable test case** demonstrating the expected behavior that is not occurring.


#### **Did you write a patch that fixes a bug?**

* Open a new GitHub pull request with the patch.

* Ensure the PR description clearly describes the problem and solution. Include the relevant issue number if applicable.

* Make sure that the tests are passing. You can see the builds  [here](https://travis-ci.org/IuryAlves/CRCDiagram)

#### **Do you intend to add a new feature or change an existing one?**

* Suggest your change by creating a issue with the ```enhancement``` label.

#### **Do you fix the bug, but don't know how to write tests?**

* No problem. Submit a pull request and someone will help you writing the tests.



## Running tests <a name='running_tests'></a>

    pip install -r requirements/develop.txt
    python tests
    flake8 .



