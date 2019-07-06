Pymtodo
=================

=================
Table of contents
=================

- `Description`_

- `Installing`_

- `Quick start`_

  #. `Authorizing`_

  #. `Get lists and tasks`_

  #. `Create lists and tasks`_

  #. `Delete lists and tasks`_

- `Documentation`_

- `Disclaimer`_

- `License`_

============
Description
============

Pymtodo is an unofficial Microsoft To-Do python library which allows managing your tasks. It can help you to optimize 
your workflow and create long lists (for example, if you read books and like to check it in your To-Do list).

============
Installing
============

For now, you can install pymtodo from our repo:

.. code:: shell

	$ git clone https://github.com/efiminem/pymtodo.git
        $ pip install pymtodo

============
Quick start
============

-------------------
Authorizing
-------------------

Pymtodo is very easy to use. First, you need to authorize in the To-Do system:

.. code:: python

	from pymtodo import ToDoConnection
	from getpass import getpass
	
	a = ToDoConnection()
	a.connect(email = 'johndoe@gmail.com', password = getpass())

-------------------
Get lists and tasks
-------------------

In order to get all your lists you can just type:

.. code:: python

	a.lists

To get the tasks for the particular list, you can write:

.. code:: python

	a.lists[0].tasks

-------------------
Create lists and tasks
-------------------

You can create lists by

.. code:: python

	a.create_list("New list")

and new tasks can be created in particluar list:

.. code:: python

	a.lists[0].create_task("New task")

-------------------
Delete lists and tasks
-------------------

You can delete your lists and tasks by the delete method:

.. code:: python

	a.lists[0].delete()
	a.lists[0].tasks[0].delete()

============
Documentation
============

Detailed documentation will be available soon.

============
Disclaimer
============

Pymtodo is an unofficial, open source, third-party, free app and is not affiliated in any way with Microsoft.

============
License
============

Pymtodo is distributed under the MIT `license
<https://github.com/efiminem/pymtodo/LICENSE>`_.
