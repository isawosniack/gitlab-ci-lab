.. _git:

===================
Git Tips and Tricks
===================

To avoid typing the passphrase all the time when pushing changes:

1. Start a new bash terminal
2. Start the ssh-agent and execute it's output as shell code in order to set the evenironment variables ``SSH_AUTH_SOCK`` and ``SSH_AGENT_PID``
3. Load your private SSH key to the ssh-agent::

    eval "$(ssh-agent -s)"
    ssh-add ~/.ssh/id_ed25519

4. Test if no passphrase is required for::

    ssh -T git@github.com
