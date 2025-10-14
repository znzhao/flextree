"""
Simple PyTree - A simple and intuitive Python library for creating and manipulating tree data structures.

This package provides TreeNode and Tree classes for building hierarchical data structures,
along with utilities for visualization, serialization, and manipulation.
"""

from .pytree import TreeNode, Tree, draw_tree
from .quick_examples import quick_examples
from .examples import examples

__version__ = "0.1.5"
__author__ = "Zhenning Zhao"
__email__ = "znzhaopersonal@gmail.com"

__all__ = ["TreeNode", "Tree", "draw_tree", "quick_examples", "examples"]