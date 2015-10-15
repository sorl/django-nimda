What is it?
===========
A light weight attempt at spicing up the django admin.

Idea
----
We wanted to make the admin look more up-to-date without making sacrifices.
These are the main goals and guidelines:

1. Attractive design
2. Upgrading Django version should cause no problems
3. Drop in replacement, no python coding required
4. Compatible with third-party admin widgets and apps
5. Keep most UX patterns from django admin, diversion should need good motivation
6. Edit css first, templates when css is insufficient
7. Keep it very stable, no fast moves, it must work


Installation
------------
::

    INSTALLED_APPS = (
        ...
        'nimda',
        ...
        'django.contrib.admin',
        ....
    )


Development
-----------
If you want to contriute and develop make sure to edit the scss files in the
root of the project. You then need to compile them to css files, this process
can be automatized using node and gulp. First run ``npm install`` in the
``django-nimda`` directory, then run ``gulp`` to keep a watcher compiling
scss on the fly outputing css to the correct locations. If you want to
compile manually run ``npm build``.
