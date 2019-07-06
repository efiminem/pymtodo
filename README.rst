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

Pymtodo is an unofficial Microsoft To-Do python library wich allows managing your tasks. It can help you to optimize 
your workflow and create long list (for example, if you read books and like to check it in your To-Do list).

============
Installing
============

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

============
Documentation
============

Detailed documentation is yet to come.

============
Disclaimer
============

Pymtodo is an unofficial, open source, third-party, free app and is not affiliated in any way with Microsoft.

============
License
============

`MIT <https://github.com/efiminem/pymtodo/LICENSE>`
