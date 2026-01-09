.. _gitlab:

=========
GitLab CI
=========

This project was frist created in GitHub and later imported to GitLab. Why? Because GitHub Pages requires an existing GitHub repo.

A few considerations:

- The GitHub author email address must be the same as the GitLab email address.
- When importing the project for the first time, you probably will have to authenticate with the GitHub page.

1. Access your GitLab account and create a new `project/repository`
2. Select the `Import project` option and import it from GitHub
3. The repository can be mirrored from GitHub
4. Set the following CI/CD variables under `Settings - CI/CD - Variables - Add variable`::

    Key: GITHUB_REPO
    Value: isawosniack/gitlab-ci-lab
    GITHUB_TOKEN
    Value: <here you have to create a developer token for your GitHub account>