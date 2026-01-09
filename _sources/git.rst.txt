.. _git:

=========
Git Setup
=========

To avoid typing the passphrase all the time wehn pusching changes::

    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519

Test ssh connection without interactive shell (check if ssh key works)::

    ssh -T git@gith
