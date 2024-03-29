Overview
========

Welcome to Astronomer! This project was generated after you ran 'astro dev init' using the Astronomer CLI. This readme describes the contents of the project, as well as how to run Apache Airflow on your local machine.

Project Contents
================

Your Astro project contains the following files and folders:

- dags: This folder contains the Python files for your Airflow DAGs. By default, this directory includes an example DAG that runs every 30 minutes and simply prints the current date. It also includes an empty 'my_custom_function' that you can fill out to execute Python code.
- Dockerfile: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
- include: This folder contains any additional files that you want to include as part of your project. It is empty by default.
- packages.txt: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
- requirements.txt: Install Python packages needed for your project by adding them to this file. It is empty by default.
- plugins: Add custom or community plugins for your project to this file. It is empty by default.
- airflow_settings.yaml: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.

Deploy Your Project Locally
===========================

1. Start Airflow on your local machine by running 'astro dev start'.

This command will spin up 3 Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Webserver: The Airflow component responsible for rendering the Airflow UI
- Scheduler: The Airflow component responsible for monitoring and triggering tasks

2. Verify that all 3 Docker containers were created by running 'docker ps'.

Note: Running 'astro dev start' will start your project with the Airflow  exposed at port 8080 and Postgres exposed at port 5432. If you already have either of those ports allocated, you can either stop your existing Docker containers or change the port.

3. Access the Airflow UI for your local Airflow project. To do so, go to http://localhost:8080/ and log in with 'admin' for both your Username and Password.

You should also be able to access your Postgres Database at 'localhost:5432/postgres'.

Deploy Your Project to Astronomer
=================================

If you have an Astronomer account, pushing code to a Deployment on Astronomer is simple. For deploying instructions, refer to Astronomer documentation: https://docs.astronomer.io/cloud/deploy-code/

Contact
=======

The Astronomer CLI is maintained with love by the Astronomer team. To report a bug or suggest a change, reach out to our support team: https://support.astronomer.io/


## Deploy non-production airflow

Although this is the non-standard way to deploy Airflow, this is purely for prototype purposes to show the value add of Airflow

1. Create an ubuntu instance on AWS. Instances settings:
    * Instance type: `t3a.xlarge` or better.
    * Volume space: 1TB or greater
    * Security group. More information on [AWS VPN user guide](https://sagebionetworks.jira.com/wiki/spaces/IT/pages/1705246745/AWS+Client+VPN+User+Guide).
        * Inbound
            * 22 (SSH) TCP 52.44.61.21/32
            * 5432 (Postgres) TCP 52.44.61.21/32
            * 8080 (Custom TCP) TCP 52.44.61.21/32
        * outbound
            * All Traffic
1. Follow instructions [here](https://docs.docker.com/engine/install/ubuntu/) to install `docker-ce`
1. Deploying Airflow
    1. Using `docker-compose.yaml` - Instructions for Running Airflow in Docker on the [Airflow site](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).
    1. Follow instructions above using the `astro` cli.

## License

This repository is licensed under the [Apache License 2.0](LICENSE).

Copyright 2022 Sage Bionetworks
