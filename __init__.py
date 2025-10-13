"""
PyTree - A simple and intuitive Python library for creating and manipulating tree data structures.

This package provides TreeNode and Tree classes for building hierarchical data structures,
along with utilities for visualization, serialization, and manipulation.
"""

from .pytree import TreeNode, Tree, draw_tree

__version__ = "1.0.0"
__author__ = "Zhenning Zhao"
__email__ = "znzhao@utexas.edu"

__all__ = ["TreeNode", "Tree", "draw_tree"]