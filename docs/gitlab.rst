.. _gitlab:

=========
GitLab CI
=========

Overall Information
===================

This project was frist created in GitHub and later imported to GitLab. 
Why? Because GitHub Pages requires an existing GitHub repo :)

How to keep multi-repos up-to-date:

- Use GitLab as origin and add the github repo as secondary (github) remote::

    git remote -v
    git remote add github git@github.com:<USERNAME>/<REPO>.git

- Add *github* as remote to origin::

    git remote set-url --add --push origin git@github.com:<USERNAME>/<REPO>.git
    git remote set-url --add --push origin git@gitlab.com:<USERNAME>/<REPO>.git

Important to know:

- The GitHub author email address must be the same as the GitLab email address.
- When importing the project for the first time, you probably will have to authenticate with the GitHub page.

GitLab Project Setup
====================

1. Access your GitLab account and create a new `project/repository`
2. Select the `Import project` option and import it from GitHub
3. The repository can be mirrored from GitHub
4. Set the following CI/CD variables under `Settings - CI/CD - Variables - Add variable`::

    Key: GITHUB_REPO
    Value: <USERNAME>/<REPO>
    GITHUB_TOKEN
    Value: <here you have to create a developer token for your GitHub account>

GitLab CI Pipeline
==================