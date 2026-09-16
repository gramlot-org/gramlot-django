.. image:: _static/gramlot-logo.png
   :alt: Gramlot logo
   :width: 120px

Gramlot Django
==============

Python-first Gramlot interfaces hosted by Django, with Django ORM integration.
This documentation describes an **experimental POC** under review and consolidation.
These previews evaluate APIs and design choices. Described behavior is intended;
bugs and unfinished cases may exist.
Examples use ``gramlot-poc`` and will evolve with Gramlot.

Start with :doc:`010-github-preview` to install the POC, :doc:`015-quickstart` for your
first page, or :doc:`030-architecture` for the server and database boundaries.

`Browse the source code <https://github.com/gramlot-org/gramlot-django/tree/main/src/gramlot_django>`_
· `Concise documentation for LLMs <https://github.com/gramlot-org/gramlot-django/tree/main/docs_llm>`_

.. toctree::
   :maxdepth: 1
   :caption: Start here

   005-overview
   010-github-preview
   015-quickstart
   020-polls-demo
   025-bakery-demo

.. toctree::
   :maxdepth: 1
   :caption: Integration

   030-architecture
   035-django
   040-admin-spa
   045-inspector

.. toctree::
   :maxdepth: 1
   :caption: Contributing

   050-getting-started
   055-documentation
   060-readthedocs
   065-release

.. toctree::
   :maxdepth: 1
   :caption: POC development records

   070-migration
   075-distribution-plan
   080-distribution-contract-assessment
   085-candidate-verification
