Description of application
=====================
The application allows you to store documents and all versions of the each document in database.
The new version of document will appears as soon as you update existing
document. There is a page, where you may look all versions of document that have been updated and also there is a page
where you may look at current version and first version of updated document.


Initial setup
+++++++++++++


#. Install PyCharm to use as IDE
#. Install prerequisites::

    apt update
    apt install git

#. if you have not configured it globally configure git::

    git config user.name 'Firstname Lastname'
    git config user.email 'youremail@youremail_domain.com'

#. Fork https://github.com/sergeysharay1987/doc_storage

#. Clone repository::

    git clone git@github.com:sergeysharay1987/doc_storage.git

#. Go to the repository directory::

    cd doc_storage

#. Install the Python build dependencies, as described at `<https://github.com/pyenv/pyenv/wiki#suggested-build-environment>`_.
#. Install pyenv according to `<https://github.com/pyenv/pyenv-installer#installation--update--uninstallation>`_.
#. Install python 3.10.5, using pyenv::

    pyenv install 3.10.5

#. Set a python version 3.10.5 in your directory with project (doc_storage/)::

    pyenv local 3.10.5


   After doing that a python-version file will appears in the directory with project.

#. Install `pip`. ::

    pip install pip==23.1.2

#. Install poetry, according to `<https://python-poetry.org/docs/#installation>`_.



Run
++++

#. Change to the directory, containing manage.py (doc_storage/doc_storage/)::

    cd doc_storage

#. Run server::

    poetry run python -m manage runserver

