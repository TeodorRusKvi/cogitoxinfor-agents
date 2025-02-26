<!-- TODO: CHANGE ALL INSTANCES OF "TEMPLATE-README" IN ENTIRE PROJECT TO YOUR PROJECT TITLE-->
# Cogito x Infor vår 2025 - Agenter 


<div align="center">

![GitHub Workflow Status (with event)](https://img.shields.io/github/actions/workflow/status/CogitoNTNU/TEMPLATE-README/ci.yml)
![GitHub top language](https://img.shields.io/github/languages/top/CogitoNTNU/TEMPLATE-README)
![GitHub language count](https://img.shields.io/github/languages/count/CogitoNTNU/TEMPLATE-README)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Project Version](https://img.shields.io/badge/version-0.0.1-blue)](https://img.shields.io/badge/version-0.0.1-blue)
![Cogito Infor Presentation (1)](https://github.com/user-attachments/assets/59dab0e7-83b3-4817-bd34-ead92445ce33)

</div>



<details> 
<summary><b>📋 Table of contents </b></summary>

- [TEMPLATE-README](#template-readme)
  - [Description](#description)
  - [Getting started](#getting-started)
    - [Prerequisites](#prerequisites)
  - [Usage](#usage)
  - [Testing](#testing)
  - [Team](#team)
    - [License](#license)

</details>

## Description 
<!-- TODO: Provide a brief overview of what this project does and its key features. Please add pictures or videos of the application -->


## Getting started
<!-- TODO: In this Section you describe how to install this project in its intended environment.(i.e. how to get it to run)  
-->


### Configuration

# Create a virtual environment
```bash
python -m venv venv
```

# Activate the environment
Mac
```bash
source venv/bin/activate
```

Windows
```bash
venv\Scripts\activate
```

```bash
venv\Scripts\Activate.ps1
Set-ExecutionPolicy Unrestricted -Scope Process
```

# Install requirements

If you dont have pip installed. Go to [this link](https://pip.pypa.io/en/stable/installation/#)
```bash
pip install -r requrements.txt
```
```bash
pip install browser-use
```

Install playwright
```bash
playwright install
```

Create a `.env` file in the root directory of the project and add the following environment variables:

```bash
OPENAI_API_KEY=""
ANTHROPIC_API_KEY=
DEEPSEEK_API_KEY= ""
# Set to false to disable anonymized telemetry
ANONYMIZED_TELEMETRY=true
BROWSER_USE_LOGGING_LEVEL=info
```


-->

### Prerequisites
<!-- TODO: In this section you put what is needed for the program to run.
For example: OS version, programs, libraries, etc.  

-->
- Ensure that git is installed on your machine. [Download Git](https://git-scm.com/downloads)



## Usage
To run the project, run the following command from the root directory of the project:
```bash
python3 main.py
```
<!-- TODO: Instructions on how to run the project and use its features. -->

## Testing
To run the test suite, run the following command from the root directory of the project:
```bash

```

## Team
This project would not have been possible without the hard work and dedication of all of the contributors. Thank you for the time and effort you have put into making this project a reality.


<table align="center">
    <tr>
        <!--
        <td align="center">
            <a href="https://github.com/NAME_OF_MEMBER">
              <img src="https://github.com/NAME_OF_MEMBER.png?size=100" width="100px;" alt="NAME OF MEMBER"/><br />
              <sub><b>NAME OF MEMBER</b></sub>
            </a>
        </td>
        -->
    </tr>
</table>

![Group picture](docs/img/team.png)


### License
------
Distributed under the MIT License. See `LICENSE` for more information.
