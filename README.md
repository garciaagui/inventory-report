<a name="readme-top"></a>

<h1 align="center">Inventory Report 📦</h1>

> [🇧🇷 Clique aqui para acessar a versão em português.](README_pt-br.md)

## Summary

<ol>
  <li><a href="#description">Description</a></li>
  <li><a href="#technologies">Technologies</a></li>
  <li><a href="#features">Features</a></li>
  <li><a href="#how-to-run">How to Run</a></li>
  <li><a href="#about-trybe">About Trybe</a></li>
  <li><a href="#contact">Contact</a></li>
</ol>

## Description

**30th project** of the [Trybe][trybe-site-url] Web Development course.

The Inventory Report is a [Python][python-url] project focused on generating simple and complete inventory reports from data stored in CSV, JSON, and XML files. In order to create an efficient and scalable system, Object-Oriented Programming concepts were applied, as well as design patterns such as Adapter, Strategy and Iterator.

> ℹ️ I wrote tests for the functions implemented by Trybe. These tests can be found in the `tests` subdirectories.

<br/>

## Technologies

The project was developed in [Python][python-url]. The tests were written using [Pytest][pytest-url] and code quality was ensured using the [Flake8][flake8-url] linter.

[![Python][python-badge]][python-url] [![Pytest][pytest-badge]][pytest-url] [![Flake8][flake8-badge]][flake8-url]

<br/>

## Features

<ul>
  <li>Import data from CSV, JSON, and XML files.</li>
  <li>Generate simple and complete reports based on the imported data.</li>
</ul>

<br/>

## How to Run

To run the project locally, follow the steps below.

1. Clone the repository.

```
git clone git@github.com:garciaagui/inventory-report.git
```

2. Navigate to the root of the project.

```
cd inventory-report/
```

3. Create the virtual environment.

```
python3 -m venv .venv
```

4. Activate the virtual environment.

```
source .venv/bin/activate
```

-   Note that at the beginning of the terminal line there will be `(.venv)`, as in the example below.

```
(.venv) gui@gui-desktop:~/Trybe/inventory-report$
```

-   To deactivate the virtual environment, run the command `deactivate`. Remember to activate it again when you return to the project.

5. Install dependencies in the virtual environment.

```
python3 -m pip install -r dev-requirements.txt
```

6. Run the command below to enable report generator.

```
pip install .
```

7. Now, it's possible to generate the reports using the command pattern below.

```
inventory_report <input_file_path> <report_type>
```

-   Example:

```
inventory_report inventory_report/data/inventory.csv simple

```

-   Accepted values for `report_type`: simple, complete, colored.

<details>
  <summary><strong> ℹ️ For additional instructions, click here.</strong></summary><br />

-   🧪 To run **all** tests, execute the command below.

```
python3 -m pytest
```

-   🧪 To run only one test file, follow the example below.

```
python3 -m pytest tests/product/test_product.py
```

-   🧪 To run only one specific test, follow the example below.

```
python3 -m pytest -k test_create_product_sucessfully
```

-   If you wish to manually test directly in the modules where the functions were implemented, follow the example below.

```
python3 -m inventory_report.reports.simple_report
```

</details>

<br/>

## About Trybe

_"[Trybe][trybe-site-url] is a future school for anyone who wants to improve their lives and build a successful career in technology, where the person only pays when they get a good job."_

_"The program features over 1,500 hours of online classes covering introduction to software development, front-end, back-end, computer science, software engineering, agile methodologies, and behavioral skills."_

<br/>

## Contact

Project developed by **Guilherme Garcia**. Below are my social networks and means of contact. 🤘

[![Gmail][gmail-badge]][gmail-url]
[![Linkedin][linkedin-badge]][linkedin-url]
[![GitHub][github-badge]][github-url]
[![Instagram][instagram-badge]][instagram-url]

<p align="right"><a href="#readme-top">Back to top</a></p>

<!-- MARKDOWN LINKS & IMAGES -->

[trybe-site-url]: https://www.betrybe.com/

<!-- STACKS -->

[flake8-url]: https://flake8.pycqa.org/en/latest/
[flake8-badge]: https://img.shields.io/badge/Flake8-000000?style=for-the-badge&logo=flake8&logoColor=white
[pytest-url]: https://docs.pytest.org/en/7.2.x/
[pytest-badge]: https://img.shields.io/badge/-Pytest-0A9EDC?logo=pytest&logoColor=white&style=for-the-badge
[python-url]: https://www.python.org/
[python-badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white

<!-- CONTACT -->

[gmail-badge]: https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white
[gmail-url]: mailto:garciaguig@gmail.com
[linkedin-badge]: https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white
[linkedin-url]: https://www.linkedin.com/in/garciaagui/
[github-badge]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[github-url]: https://github.com/garciaagui
[instagram-badge]: https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white
[instagram-url]: https://www.instagram.com/garciaagui/
