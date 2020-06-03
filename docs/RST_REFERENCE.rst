***
RST
***
``easy_install docutils``

``pip install docutils``

Sacado de:

1. en_minutos_
2. y principalmente de: sourcefog_

.. _en_minutos: https://learnxinyminutes.com/docs/rst/

.. _sourcefog: http://docutils.sourceforge.net/docs/user/rst/quickref.html
.. Lines starting with two dots are special commands. But if no command can be found, the line is considered as a comment

*emphasis*

**strong emphasis**

`interpreted text`

``inline literal``

reference_

.. _reference: referencia sencilla


|substitution reference|

.. |substitution reference| image:: https://img.shields.io/pypi/v/ansible.svg
   :target: http://elpais.com


footnote reference [1]_

.. [1] Número 1

citation reference [CIT2008]_

.. [CIT2008] A citation
   (as often used in journals).


A standalone hyperlink.
http://docutils.sf.net/


Escaping
========
Raw RST
-------
*escape* ``with`` "\"
 \*escape* \``with`` "\\"

Python String
-------------
r"""\*escape* \`with` "\\""""
 """\\*escape* \\`with` "\\\\""""
 """\*escape* \`with` "\\""""

Section Structure
------------------
=====
Title
=====
Subtitle
--------
Titles are underlined (or over-
and underlined) with a printing
nonalphanumeric 7-bit ASCII
character. Recommended choices
are "``= - ` : ' " ~ ^ _ * + # < >``".
The underline/overline must be at
least as long as the title text.

A lone top-level (sub)section
is lifted up to be the document's
(sub)title.

=========================================================
Main titles are written using equals signs over and under
=========================================================

Note that there must be as many equals signs as title characters.

Title are underlined with equals signs too
==========================================

Bullet Lists
------------
Bullet lists:

- This is item 1
- This is item 2

- Bullets are "-", "*" or "+".
  Continuing text must be aligned
  after the bullet and whitespace.

Note that a blank line is required
before the first item and after the
last, but is optional between items.

Enumerated Lists
----------------

Enumerated lists:

3. This is the first item
4. This is the second item
5. Enumerators are arabic numbers,
   single letters, or roman numerals
6. List items should be sequentially
   numbered, but need not start at 1
   (although not all formatters will
   honour the first index).
#. This item is auto-enumerated

Definition Lists
----------------
Definition lists:

what
  Definition lists associate a term with
  a definition.

how
  The term is a one-line phrase, and the
  definition is one or more paragraphs or
  body elements, indented relative to the
  term. Blank lines are not allowed
  between term and definition.

Field Lists
----------------
:Authors:
    Tony J. (Tibs) Ibbs,
    David Goodger

    (and sundry other good-natured folks)

:Version: 1.0 of 2001/08/08
:Dedication: To my father.

Option Lists
----------------
-a            command-line option "a"
-b file       options can have arguments
              and long descriptions
--long        options can be long also
--input=file  long options can also have
              arguments
/V            DOS/VMS-style options too


Literal Blocks
--------------
A paragraph containing only two colons
indicates that the following indented
or quoted text is a literal block.

::

  Whitespace, newlines, blank lines, and
  all kinds of markup (like *this* or
  \this) is preserved by literal blocks.

  The paragraph containing only '::'
  will be omitted from the result.

The ``::`` may be tacked onto the very
end of any paragraph. The ``::`` will be
omitted if it is preceded by whitespace.
The ``::`` will be converted to a single
colon if preceded by text, like this::

    It's very convenient to use this form.

Literal blocks end when text returns to
the preceding paragraph's indentation.
This means that something like this
is possible::

            We start here
        and continue here
    and end here.

Per-line quoting can also be used on
unindented literal blocks::

    > Useful for quotes from email and
    > for Haskell literate programming.




Line Blocks
-----------
| Line blocks are useful for addresses,
| verse, and adornment-free lists.
|
| Each new line begins with a
| vertical bar ("|").
|     Line breaks and initial indents
|     are preserved.
| Continuation lines are wrapped
  portions of long lines; they begin
  with spaces in place of vertical bars.

Bock Quotes
-----------
Block quotes are just:

    Indented paragraphs,

        and they may nest.

Doctest Blocks
--------------
Doctest blocks are interactive
Python sessions. They begin with
"``>>>``" and end with a blank line.

>>> print("This is a doctest block.")
This is a doctest block.

Tables
------
Grid table:

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

Simple table:

=====  =====  ======
   Inputs     Output
------------  ------
  A      B    A or B
=====  =====  ======
False  False  False
True   False  True
False  True   True
True   True   True
=====  =====  ======

Transitions
-----------
A transition marker is a horizontal line
of 4 or more repeated punctuation
characters.

------------

A transition should not begin or end a
section or document, nor should two
transitions be immediately adjacent.

Explicit Markup
===============
Footnotes
---------
Footnote references, like [5]_.
Note that footnotes may get
rearranged, e.g., to the bottom of
the "page".

.. [5] A numerical footnote. Note
   there's no colon after the ``]``.

Autonumbered footnotes are
possible, like using [#]_ and [#]_.

.. [#] This is the first one.
.. [#] This is the second one.

They may be assigned 'autonumber
labels' - for instance,
[#fourth]_ and [#third]_.

.. [#third] a.k.a. third_

.. [#fourth] a.k.a. fourth_

Auto-symbol footnotes are also
possible, like this: [*]_ and [*]_.

.. [*] This is the first one.
.. [*] This is the second one.

Citations
---------
Citation references, like [CIT2002]_.
Note that citations may get
rearranged, e.g., to the bottom of
the "page".

.. [CIT2002] A citation
   (as often used in journals).

Citation labels contain alphanumerics,
underlines, hyphens and fullstops.
Case is not significant.

Given a citation like [this]_, one
can also refer to it like this_.

.. [this] here.




Subtitles with dashes
---------------------

You can put text in *italic* or in **bold**, you can "mark" text as code with double backquote ``print()``.

Lists are similar to Markdown, but a little more involved.

Remember to line up list symbols (like - or \*) with the left edge of the previous text block, and remember to use blank lines to separate new lists from parent lists:

- First item
- Second item

  - Sub item

- Third item

or

* First item
* Second item

  * Sub item

* Third item

Tables are really easy to write:

=========== ========
Country     Capital
=========== ========
France      Paris
Japan       Tokyo
=========== ========

More complex tables can be done easily (merged columns and/or rows) but I suggest you to read the complete doc for this :)

There are multiple ways to make links:

- By typing a full comprehensible URL : https://github.com/ (will be automatically converted to a link)
- By making a more Markdown-like link: `Github <https://github.com/>`_ .

.. _Github: https://github.com/


``rst2html myfile.rst output.html``

Hyperlink Targets
=================

External Hyperlinks Targets
---------------------------
External hyperlinks, like Python_.

.. _Python: http://www.python.org/

Internal Hyperlinks Targets
---------------------------
Internal crossreferences, like example_.

.. _example:

This is an example crossreference target.

Indirect Hyperlinks Targets
---------------------------
Python3_ is `my favourite
programming language`__.

.. _Python3: http://www.python.org/

__ Python_

Implicit Hyperlinks Targets
---------------------------
Titles are targets, too
=======================
Implict references, like `Titles are
targets, too`_.

Directives
----------
For instance:

.. image:: images/https://img.shields.io/badge/code%20of%20conduct-Ansible-silver.svg


Substitution References and Definitions
---------------------------------------
The |biohazard| symbol must be used on containers used to dispose of medical waste.

.. |biohazard| image:: https://img.shields.io/badge/docs-latest-brightgreen.svg

Comments
--------
.. This text will not be shown
   (but, for instance, in HTML might be
   rendered as an HTML comment)


An "empty comment" does not
consume following blocks.
(An empty comment is ".." with
blank lines before and after.)

..

        So this block is not "lost",
        despite its indentation.


|PyPI version| |Docs badge| |Chat badge| |Build Status| |Code Of Conduct| |Mailing Lists| |License|

License
=======

GNU General Public License v3.0

See `COPYING <COPYING>`_ to see the full text.

.. |PyPI version| image:: https://img.shields.io/pypi/v/ansible.svg
   :target: https://pypi.org/project/ansible
.. |Docs badge| image:: https://img.shields.io/badge/docs-latest-brightgreen.svg
   :target: https://docs.ansible.com/ansible/latest/
.. |Build Status| image:: https://api.shippable.com/projects/573f79d02a8192902e20e34b/badge?branch=devel
   :target: https://app.shippable.com/projects/573f79d02a8192902e20e34b
.. |Chat badge| image:: https://img.shields.io/badge/chat-IRC-brightgreen.svg
   :target: https://docs.ansible.com/ansible/latest/community/communication.html
.. |Code Of Conduct| image:: https://img.shields.io/badge/code%20of%20conduct-Ansible-silver.svg
   :target: https://docs.ansible.com/ansible/latest/community/code_of_conduct.html
   :alt: Ansible Code of Conduct
.. |Mailing Lists| image:: https://img.shields.io/badge/mailing%20lists-Ansible-orange.svg
   :target: https://docs.ansible.com/ansible/latest/community/communication.html#mailing-list-information
   :alt: Ansible mailing lists
.. |License| image:: https://img.shields.io/badge/license-GPL%20v3.0-brightgreen.svg
   :target: COPYING
   :alt: Repository License