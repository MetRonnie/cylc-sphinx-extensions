# -----------------------------------------------------------------------------
# THIS FILE IS PART OF THE CYLC SUITE ENGINE.
# Copyright (C) 2008-2019 NIWA & British Crown (Met Office) & Contributors.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------
"""Directives for use in practical exercises.

.. rubric:: Example

.. code-block:: rst

    .. practical::

       Some instructions here.

       .. spoiler:: warning

          Hidden text which will display with class ``warning``.

.. practical::

   Some instructions here.

   .. spoiler:: warning

      Hidden text which will display with class ``warning``.

"""


__all__ = [
    'Practical',
    'PracticalExtension',
    'Spoiler',
    'setup'
]


from cylc.sphinx_ext.practical.admonitions import (
    Practical,
    PracticalExtension,
    Spoiler
)


__version__ = '1.0.0'


def setup(app):
    """Sphinx setup function."""
    from cylc.sphinx_ext import register_static
    app.add_directive('practical', Practical)
    app.add_directive('practical-extension', PracticalExtension)
    app.add_directive('spoiler', Spoiler)
    app.add_javascript('js/spoiler.js')  # self-hiding node.
    register_static(app, __name__)
    return {'version': __version__, 'parallel_read_safe': True}
