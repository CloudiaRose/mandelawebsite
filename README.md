# Mandela Website

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Docker](#docker)
- [Credits](#credits)

## Introduction

Welcome to the Mandela Website, a project dedicated to celebrating the life and legacy of Nelson Mandela. Our platform offers a comprehensive exploration of Mandela's biography, legacy, and inspiring quotes. Users can register and log in to personalize their experience, saving favorite quotes and participating in discussions. Join us in honoring Mandela's enduring impact and vision for peace and equality.

## Features

- User registration
- User login

## Requirements

- Python >= version 3.12
- Docker
- Django==5.0.3
- Sphinx==7.2.6
- virtualenv==20.25.1

## Installation

Clone this repo to your local machine, by running the following command through your terminal

```bash
git clone https://github.com/CloudiaRose/mandela.git
```

Then run the following command to install the Requirements for this project

```bash
pip install -r requirements.txt
```

Start the server

```bash

python manage.py runserver
```

Access the application in your web browser at 'http://127.0.0.1:8000/'.

## Docker

```bash
docker build -t mandela .
docker run -p 8000:8000 mandela-website
```

## Credits

Created by Cloudia
