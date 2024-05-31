# Copyright (C) 2023-2024 Matthew Scroggs and Garth N. Wells
#
# This file is part of Basix (https://www.fenicsproject.org)
#
# SPDX-License-Identifier:    MIT
"""Functions for handling Sobolev spaces."""

from basix._basixcpp import SobolevSpace
from basix._basixcpp import sobolev_space_intersection as _ssi

__all__ = ["intersection", "string_to_sobolev_space"]


def intersection(spaces: list[SobolevSpace]) -> SobolevSpace:
    """Compute the intersection of a list of Sobolev spaces.

    Args:
        spaces: List of Sobolev spaces.

    Returns:
        Intersection of the Sobolev spaces.
    """
    space = spaces[0]
    for s in spaces[1:]:
        space = _ssi(space, s)
    return SobolevSpace[space.name]


def string_to_sobolev_space(space: str) -> SobolevSpace:
    """Convert a string to a Basix SobolevSpace.

    Args:
        space: Name of the space.

    Returns:
        Cell type.
    """
    return SobolevSpace[space]
