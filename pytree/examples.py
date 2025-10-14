#!/usr/bin/env python3
"""
PyTree Usage Examples

This file demonstrates comprehensive usage of all classes and functions
in the pytree module. It serves as both documentation and a practical
guide for users.

Run this file to see all features in action:
    python examples.py
"""

import json
import tempfile
import os
from pytree import TreeNode, Tree, draw_tree

def example_basic_treenode_operations():
    """Demonstrate basic TreeNode operations."""
    print("=" * 60)
    print("BASIC TREENODE OPERATIONS")
    print("=" * 60)
    
    # Create nodes
    print("1. Creating TreeNodes:")
    print("   CODE:")
    print('   root = TreeNode("Company", "Acme Corporation")')
    print('   engineering = TreeNode("Engineering", "Technology Department")')
    print('   marketing = TreeNode("Marketing", "Marketing Department")')
    print()
    
    root = TreeNode("Company", "Acme Corporation")
    print(f"   OUTPUT: Root node: {root}")
    
    engineering = TreeNode("Engineering", "Technology Department")
    marketing = TreeNode("Marketing", "Marketing Department")
    print(f"   OUTPUT: Child nodes created: {engineering.name}, {marketing.name}")
    
    # Add children
    print("\n2. Adding children:")
    print("   CODE:")
    print("   root.add_child(engineering)")
    print("   root.add_child(marketing)")
    print()
    
    root.add_child(engineering)
    root.add_child(marketing)
    print(f"   OUTPUT: Root now has {len(root.children)} children")
    print(f"   OUTPUT: Engineering parent: {engineering.parent.name if engineering.parent else 'None'}")
    
    # Get children
    print("\n3. Getting children:")
    print("   CODE:")
    print("   first_child = root.get_child(0)  # By index")
    print('   eng_child = root.get_child("Engineering")  # By name')
    print()
    
    first_child = root.get_child(0)  # By index
    eng_child = root.get_child("Engineering")  # By name
    print(f"   OUTPUT: First child by index: {first_child.name if first_child else 'None'}")
    print(f"   OUTPUT: Engineering child by name: {eng_child.name if eng_child else 'None'}")
    
    # Add more nested structure
    print("\n4. Adding nested structure:")
    print("   CODE:")
    print('   backend = TreeNode("Backend", "Server Development")')
    print('   frontend = TreeNode("Frontend", "UI Development")')
    print("   engineering.add_child(backend)")
    print("   engineering.add_child(frontend)")
    print()
    
    backend = TreeNode("Backend", "Server Development")
    frontend = TreeNode("Frontend", "UI Development")
    engineering.add_child(backend)
    engineering.add_child(frontend)
    
    print("OUTPUT: Tree structure so far:")
    draw_tree(root)
    
    print(f"\n5. Node statistics:")
    print("   CODE:")
    print("   root.max_depth()")
    print("   root.max_width()")
    print("   root.count()")
    print("   engineering.max_depth()")
    print("   engineering.count()")
    print()
    print(f"   OUTPUT: Root max depth: {root.max_depth()}")
    print(f"   OUTPUT: Root max width: {root.max_width()}")  
    print(f"   OUTPUT: Root node count: {root.count()}")
    print(f"   OUTPUT: Engineering max depth: {engineering.max_depth()}")
    print(f"   OUTPUT: Engineering node count: {engineering.count()}")


def example_treenode_content_operations():
    """Demonstrate TreeNode content operations."""
    print("\n" + "=" * 60)
    print("TREENODE CONTENT OPERATIONS")
    print("=" * 60)
    
    # Different content types
    print("1. Different content types:")
    print("   CODE:")
    print('   # String content')
    print('   string_node = TreeNode("StringNode", "Simple string content")')
    print()
    print('   # Dictionary content')
    print('   dict_content = {')
    print('       "definition": "A programming language",')
    print('       "type": "interpreted",')
    print('       "year": 1991,')
    print('       "features": ["dynamic typing", "garbage collection"]')
    print('   }')
    print('   dict_node = TreeNode("Python", dict_content)')
    print()
    
    # String content
    string_node = TreeNode("StringNode", "Simple string content")
    
    # Dictionary content
    dict_content = {
        "definition": "A programming language",
        "type": "interpreted",
        "year": 1991,
        "features": ["dynamic typing", "garbage collection"]
    }
    dict_node = TreeNode("Python", dict_content)
    print('   # List content')
    print('   list_node = TreeNode("Technologies", ["Python", "JavaScript", "Docker", "AWS"])')
    print()
    print('   # Numeric content')
    print('   numeric_node = TreeNode("ProjectCount", 42)')
    print()
    print('   # None content')
    print('   none_node = TreeNode("EmptyNode", None)')
    print()
    
    # List content
    list_node = TreeNode("Technologies", ["Python", "JavaScript", "Docker", "AWS"])
    
    # Numeric content
    numeric_node = TreeNode("ProjectCount", 42)
    
    # None content
    none_node = TreeNode("EmptyNode", None)
    
    print(f"   OUTPUT: String content: {string_node.content}")
    print(f"   OUTPUT: Dict content keys: {list(dict_node.content.keys())}")
    print(f"   OUTPUT: List content length: {len(list_node.content)}")
    print(f"   OUTPUT: Numeric content: {numeric_node.content}")
    print(f"   OUTPUT: None content: {none_node.content}")
    
    # Modify content
    print("\n2. Modifying content:")
    string_node.set_content("Updated string content")
    dict_node.set_content({"definition": "Updated definition", "new_field": "added"})
    print(f"   Updated string: {string_node.content}")
    print(f"   Updated dict: {dict_node.content}")
    
    # Build a tree with different content types
    root = TreeNode("ContentDemo", "Root with various content types")
    root.add_child(string_node)
    root.add_child(dict_node)
    root.add_child(list_node)
    root.add_child(numeric_node)
    root.add_child(none_node)
    
    print("\n3. Tree with different content types:")
    draw_tree(root)
    
    print("\n4. Node summaries:")
    print(dict_node.summary())

def example_getitem_operations():
    """Demonstrate getitem operations (indexing, slicing) for Tree objects."""
    print("\n" + "=" * 60)
    print("GETITEM OPERATIONS (INDEXING & SLICING)")
    print("=" * 60)
    
    # Build a tree for demonstration
    print("1. Setting up a sample tree:")
    print("   CODE:")
    print('   root = TreeNode("Company", "Tech Company")')
    print('   engineering = TreeNode("Engineering", "Tech Department")')
    print('   marketing = TreeNode("Marketing", "Growth Department")') 
    print('   sales = TreeNode("Sales", "Revenue Department")')
    print('   support = TreeNode("Support", "Customer Service")')
    print()
    print('   root.add_child(engineering)')
    print('   root.add_child(marketing)')
    print('   root.add_child(sales)')
    print('   root.add_child(support)')
    print()
    print('   # Add sub-departments')
    print('   backend = TreeNode("Backend", "Server Development")')
    print('   frontend = TreeNode("Frontend", "UI Development")')
    print('   engineering.add_child(backend)')
    print('   engineering.add_child(frontend)')
    print()
    
    root = TreeNode("Company", "Tech Company")
    engineering = TreeNode("Engineering", "Tech Department")
    marketing = TreeNode("Marketing", "Growth Department")
    sales = TreeNode("Sales", "Revenue Department")
    support = TreeNode("Support", "Customer Service")
    
    root.add_child(engineering)
    root.add_child(marketing)
    root.add_child(sales)
    root.add_child(support)
    
    backend = TreeNode("Backend", "Server Development")
    frontend = TreeNode("Frontend", "UI Development")
    engineering.add_child(backend)
    engineering.add_child(frontend)
    
    print("OUTPUT: Tree structure:")
    draw_tree(root)
    
    # Create Tree object for getitem operations
    print("\n2. Create Tree object for getitem operations:")
    print("   CODE:")
    print('   # TreeNode objects do not support getitem - need Tree object')
    print('   company_tree = Tree(root)')
    print('   # Access child by name (returns Tree object)')
    print('   eng_dept = company_tree["Engineering"]')
    print('   print(f"Found department: {eng_dept.name if eng_dept else None}")')
    print()
    print('   # Access child by index (returns TreeNode)')
    print('   first_dept = root[0]')
    print('   print(f"First department: {first_dept.name if first_dept else None}")')
    print()
    print('   # Access multiple children by slice (returns list of TreeNode)')
    print('   middle_depts = root[1:3]')
    print('   print(f"Middle departments: {[d.name for d in middle_depts]}")')
    print()
    print('   # Access multiple children by list (returns list of TreeNode)')
    print('   selected_depts = root[["Engineering", 2, "Support"]]')
    print('   print(f"Selected departments: {[d.name for d in selected_depts]}")')
    print()
    
    # Note: TreeNode objects do not support getitem operations
    # Use Tree objects for getitem functionality instead
    print("   OUTPUT: TreeNode objects do not support getitem - use Tree objects instead")
    
    # Direct TreeNode access using children list
    print("   Alternative - Direct TreeNode access:")
    print(f"   First department (by index): {root.children[0].name if root.children else 'None'}")
    
    # Find by name using helper method or loop
    eng_dept = None
    for child in root.children:
        if child.name == "Engineering":
            eng_dept = child
            break
    print(f"   Engineering department (by name): {eng_dept.name if eng_dept else 'None'}")
    
    # Tree class getitem examples
    print("\n3. Tree class getitem operations:")
    print("   CODE:")
    print('   company_tree = Tree(root)')
    print('   # Access subtree by name (returns Tree or None)')
    print('   eng_subtree = company_tree["Engineering"]')
    print('   print(f"Engineering subtree: {eng_subtree.root.name if eng_subtree else None}")')
    print()
    print('   # Multiple selection by string list (returns List[Tree])')
    print('   selected_depts = company_tree[["Engineering", "Marketing"]]')
    print('   print(f"Selected departments: {[t.root.name for t in selected_depts]}")')
    print()
    
    company_tree = Tree(root)
    
    # Access subtree by name (returns Tree or None)
    eng_subtree = company_tree["Engineering"]
    if eng_subtree:
        print(f"   OUTPUT: Engineering subtree: {eng_subtree.root.name}")
    else:
        print("   OUTPUT: Engineering subtree: None")
    
    # Multiple selection by string list (returns List[Tree])
    selected_depts = company_tree[["Engineering", "Marketing"]]
    if selected_depts:
        print(f"   OUTPUT: Selected departments: {[t.root.name for t in selected_depts]}")
    else:
        print("   OUTPUT: Selected departments: []")
    
    print("\n4. Advanced getitem usage:")
    print("   CODE:")
    print('   # Chain getitem operations')
    print('   eng_subtree = company_tree["Engineering"]')
    print('   if eng_subtree:')
    print('       print("Engineering subtree found - can navigate further")')
    print('       print("Tree getitem only supports single access or string-only lists")')
    print('   else:')
    print('       print("Engineering subtree not found")')
    print()
    
    # Chain getitem operations
    if eng_subtree:
        # Note: Tree getitem only supports string-only lists for multiple selection
        print("   OUTPUT: Engineering subtree found - can navigate further")
        print("   Tree getitem only supports single access or string-only lists")
    else:
        print("   OUTPUT: Engineering subtree not found")
    
    print("\n5. Summary of getitem features:")
    print("   - TreeNode objects do NOT support getitem operations")
    print("   - Tree[key] returns Tree objects (single) or List[Tree]")
    print("   - Support for string keys (by name)")
    print("   - Support for string-only lists: tree[['name1', 'name2']]")
    print("   - For other access patterns, use TreeNode.children directly")
    print("   - Makes tree navigation pythonic while maintaining type safety!")


def example_treenode_search_operations():
    """Demonstrate TreeNode search and traversal operations."""
    print("\n" + "=" * 60)
    print("TREENODE SEARCH OPERATIONS")
    print("=" * 60)
    
    # Build a deeper tree for searching
    root = TreeNode("Root", "Top level")
    
    # Level 1
    branch1 = TreeNode("Branch1", "First branch")
    branch2 = TreeNode("Branch2", "Second branch")
    root.add_child(branch1)
    root.add_child(branch2)
    
    # Level 2
    leaf1 = TreeNode("Leaf1", "First leaf")
    leaf2 = TreeNode("Leaf2", "Second leaf")
    leaf3 = TreeNode("Leaf3", "Third leaf")
    branch1.add_child(leaf1)
    branch1.add_child(leaf2)
    branch2.add_child(leaf3)
    
    # Level 3
    deep_node = TreeNode("DeepNode", "Deeply nested")
    leaf2.add_child(deep_node)
    
    print("1. Tree structure for searching:")
    draw_tree(root)
    
    print("\n2. Finding nodes with get_subtree:")
    found_branch = root.get_subtree("Branch2")
    found_leaf = root.get_subtree("Leaf2")
    found_deep = root.get_subtree("DeepNode")
    not_found = root.get_subtree("NonExistent")
    
    print(f"   Found Branch2: {found_branch.name if found_branch else 'Not found'}")
    print(f"   Found Leaf2: {found_leaf.name if found_leaf else 'Not found'}")
    print(f"   Found DeepNode: {found_deep.name if found_deep else 'Not found'}")
    print(f"   Found NonExistent: {not_found.name if not_found else 'Not found'}")
    
    print("\n3. Drawing subtrees:")
    if found_branch:
        print("   Branch2 subtree:")
        draw_tree(found_branch, "   ")


def example_treenode_modification_operations():
    """Demonstrate TreeNode modification operations."""
    print("\n" + "=" * 60)
    print("TREENODE MODIFICATION OPERATIONS")
    print("=" * 60)
    
    # Create initial tree
    root = TreeNode("Team", "Development Team")
    alice = TreeNode("Alice", "Team Lead")
    bob = TreeNode("Bob", "Senior Developer")
    charlie = TreeNode("Charlie", "Junior Developer")
    
    root.add_child(alice)
    root.add_child(bob)
    root.add_child(charlie)
    
    print("1. Initial team structure:")
    draw_tree(root)
    
    # Remove by node object
    print("\n2. Remove Charlie (by node object):")
    root.remove_child(charlie)
    draw_tree(root)
    
    # Add new members
    print("\n3. Add new team members:")
    diana = TreeNode("Diana", "DevOps Engineer")
    eve = TreeNode("Eve", "UI/UX Designer")
    root.add_child(diana)
    root.add_child(eve)
    draw_tree(root)
    
    # Remove by name
    print("\n4. Remove Diana (by name):")
    root.remove_child("Diana")
    draw_tree(root)
    
    # Remove by index
    print("\n5. Remove first person (by index):")
    print(f"   Removing: {root.children[0].name}")
    root.remove_child(0)
    draw_tree(root)


def example_treenode_serialization():
    """Demonstrate TreeNode serialization (to_dict/from_dict)."""
    print("\n" + "=" * 60)
    print("TREENODE SERIALIZATION")
    print("=" * 60)
    
    # Create a complex tree
    root = TreeNode("Project", {"name": "PyTree", "version": "1.0.0"})
    
    src = TreeNode("src", {"definition": "Source code directory", "type": "folder"})
    tests = TreeNode("tests", {"definition": "Test files", "type": "folder"})
    docs = TreeNode("docs", {"definition": "Documentation", "type": "folder"})
    
    main_py = TreeNode("main.py", {"definition": "Main Python file", "lines": 150})
    utils_py = TreeNode("utils.py", {"definition": "Utility functions", "lines": 75})
    
    root.add_child(src)
    root.add_child(tests)
    root.add_child(docs)
    src.add_child(main_py)
    src.add_child(utils_py)
    
    print("1. Original tree:")
    draw_tree(root)
    
    # Convert to dictionary
    print("\n2. Converting to dictionary:")
    tree_dict = root.to_dict()
    print("Dictionary structure:")
    print(json.dumps(tree_dict, indent=2))
    
    # Create from dictionary
    print("\n3. Recreating from dictionary:")
    reconstructed = TreeNode.from_dict(tree_dict)
    print("Reconstructed tree:")
    draw_tree(reconstructed)
    
    # Verify they're equivalent
    print(f"\n4. Verification:")
    print(f"   Original root name: {root.name}")
    print(f"   Reconstructed root name: {reconstructed.name}")
    print(f"   Original children count: {len(root.children)}")
    print(f"   Reconstructed children count: {len(reconstructed.children)}")
    print(f"   Original max depth: {root.max_depth()}")
    print(f"   Reconstructed max depth: {reconstructed.max_depth()}")


def example_tree_class_operations():
    """Demonstrate Tree class operations."""
    print("\n" + "=" * 60)
    print("TREE CLASS OPERATIONS")
    print("=" * 60)
    
    # Create initial tree structure
    print("1. Initial tree creation:")
    print("   CODE:")
    print('   root = TreeNode("Company", "Tech Startup")')
    print('   tree = Tree(root)')
    print()
    
    root = TreeNode("Company", "Tech Startup")
    tree = Tree(root)
    
    print("OUTPUT: Initial tree (just root):")
    draw_tree(tree.root)
    
    # Insert operations
    print("\n2. Inserting departments:")
    print("   CODE:")
    print('   engineering = TreeNode("Engineering", "Product Development")')
    print('   marketing = TreeNode("Marketing", "Growth & Marketing")')
    print('   sales = TreeNode("Sales", "Revenue Generation")')
    print()
    print('   tree.insert("Company", engineering)')
    print('   tree.insert("Company", marketing)')
    print('   tree.insert("Company", sales)')
    print()
    
    engineering = TreeNode("Engineering", "Product Development")
    marketing = TreeNode("Marketing", "Growth & Marketing")
    sales = TreeNode("Sales", "Revenue Generation")
    
    tree.insert("Company", engineering)
    tree.insert("Company", marketing)
    tree.insert("Company", sales)

    print("OUTPUT:")
    draw_tree(tree.root)
    
    # Insert sub-departments
    print("\n3. Adding sub-departments:")
    backend = TreeNode("Backend", "Server Development")
    frontend = TreeNode("Frontend", "Client Development")
    qa = TreeNode("QA", "Quality Assurance")
    
    tree.insert("Engineering", backend)
    tree.insert("Engineering", frontend)
    tree.insert("Engineering", qa)
    draw_tree(tree.root)
    
    # Alter operations
    print("\n4. Updating department descriptions:")
    tree.alter("Backend", "Backend & Infrastructure")
    tree.alter("QA", "Quality Assurance & Testing")
    draw_tree(tree.root)
    
    # Get subtrees
    print("\n5. Getting Engineering subtree:")
    eng_subtree = tree.get("Engineering")
    if eng_subtree:
        print("Engineering department structure:")
        draw_tree(eng_subtree.root)
    
    # Get by index
    print("\n6. Getting first department by index:")
    first_dept = tree.get(0)
    if first_dept:
        print(f"First department: {first_dept.root.name}")
        draw_tree(first_dept.root)
    
    # Delete operations
    print("\n7. Removing QA department:")
    tree.delete("QA")
    draw_tree(tree.root)
    
    # Tree statistics
    print(f"\n8. Tree statistics:")
    print("   CODE:")
    print("   tree.max_depth()")
    print("   tree.max_width()")
    print("   tree.count()")
    print()
    print(f"   OUTPUT: Max depth: {tree.max_depth()}")
    print(f"   OUTPUT: Max width: {tree.max_width()}")
    print(f"   OUTPUT: Node count: {tree.count()}")
    print(f"   OUTPUT: Tree representation: {tree}")
    
    print(f"\n9. Tree summary:")
    print(tree.summary())


def example_tree_json_operations():
    """Demonstrate Tree JSON serialization operations."""
    print("\n" + "=" * 60)
    print("TREE JSON OPERATIONS")
    print("=" * 60)
    
    # Create a knowledge tree
    root = TreeNode("Programming", {"definition": "Software Development Knowledge"})
    tree = Tree(root)
    
    # Languages
    languages = TreeNode("Languages", {"definition": "Programming Languages"})
    python_node = TreeNode("Python", {
        "definition": "High-level programming language",
        "year": 1991,
        "creator": "Guido van Rossum"
    })
    javascript_node = TreeNode("JavaScript", {
        "definition": "Web programming language", 
        "year": 1995,
        "creator": "Brendan Eich"
    })
    
    # Concepts
    concepts = TreeNode("Concepts", {"definition": "Programming Concepts"})
    oop = TreeNode("OOP", {"definition": "Object-Oriented Programming"})
    fp = TreeNode("FP", {"definition": "Functional Programming"})
    
    # Build tree
    tree.insert("Programming", languages)
    tree.insert("Programming", concepts)
    tree.insert("Languages", python_node)
    tree.insert("Languages", javascript_node)
    tree.insert("Concepts", oop)
    tree.insert("Concepts", fp)
    
    print("1. Knowledge tree structure:")
    draw_tree(tree.root)
    
    # Save to JSON
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        temp_file = f.name
    
    try:
        print(f"\n2. Saving to JSON file: {temp_file}")
        tree.save_json(temp_file)
        
        # Show JSON content
        with open(temp_file, 'r') as f:
            json_content = f.read()
        print("JSON content (first 300 chars):")
        print(json_content[:300] + "..." if len(json_content) > 300 else json_content)
        
        # Load from JSON
        print(f"\n3. Loading from JSON file:")
        loaded_tree = Tree.load_json(temp_file)
        print("Loaded tree structure:")
        draw_tree(loaded_tree.root)
        
        # Verify equivalence
        print(f"\n4. Verification:")
        print(f"   Original depth: {tree.max_depth()}, Loaded depth: {loaded_tree.max_depth()}")
        print(f"   Original width: {tree.max_width()}, Loaded width: {loaded_tree.max_width()}")
        print(f"   Root content match: {tree.root.content == loaded_tree.root.content}")
        
    finally:
        # Clean up
        if os.path.exists(temp_file):
            os.unlink(temp_file)


def example_draw_tree_function():
    """Demonstrate all draw_tree function capabilities."""
    print("\n" + "=" * 60)
    print("DRAW_TREE FUNCTION DEMONSTRATIONS")
    print("=" * 60)
    
    # Create a tree with various content types
    root = TreeNode("MixedContent", "Tree with various content types")
    
    # String content
    string_node = TreeNode("StringNode", "Simple string")
    
    # Dictionary with 'definition' key (special handling)
    dict_def_node = TreeNode("DictDef", {
        "definition": "Dictionary with definition key",
        "other": "This won't be shown",
        "more": "Neither will this"
    })
    
    # Dictionary without 'definition' key
    dict_normal_node = TreeNode("DictNormal", {
        "key1": "value1",
        "key2": "value2"
    })
    
    # Complex nested content
    complex_node = TreeNode("Complex", {
        "definition": "Complex nested structure",
        "details": {
            "nested": True,
            "level": "deep"
        }
    })
    
    # Build tree
    root.add_child(string_node)
    root.add_child(dict_def_node)
    root.add_child(dict_normal_node)
    root.add_child(complex_node)
    
    # Add children to show nesting
    child1 = TreeNode("Child1", "First child")
    child2 = TreeNode("Child2", {"definition": "Second child with definition"})
    grandchild = TreeNode("GrandChild", "Deeply nested")
    
    string_node.add_child(child1)
    string_node.add_child(child2)
    child1.add_child(grandchild)
    
    print("1. Complete tree showing different content handling:")
    draw_tree(root)
    
    print("\n2. Drawing subtree from StringNode:")
    draw_tree(string_node)
    
    print("\n3. Drawing just the complex node:")
    draw_tree(complex_node)
    
    # Demonstrate custom definition key
    print("\n4. Custom definition key demonstration:")
    custom_root = TreeNode("Products", "Product catalog")
    
    # Create nodes with custom dictionary keys
    product1 = TreeNode("Laptop", {
        "name": "Gaming Laptop",
        "price": "$1299",
        "category": "Electronics"
    })
    
    product2 = TreeNode("Mouse", {
        "name": "Wireless Mouse", 
        "price": "$29",
        "category": "Accessories"
    })
    
    product3 = TreeNode("Book", {
        "title": "Python Programming",
        "author": "John Doe",
        "price": "$39"
    })
    
    custom_root.add_child(product1)
    custom_root.add_child(product2)
    custom_root.add_child(product3)
    
    print("Using 'name' key:")
    draw_tree(custom_root, key="name")

    print("\nUsing 'title' key (note: only Book has this key):")
    draw_tree(custom_root, key="title")

    print("\nUsing 'price' key:")
    draw_tree(custom_root, key="price")
    
    # Demonstrate TreeNode.draw() method with custom key
    print("\n5. Using TreeNode.draw() method with custom key:")
    tech_node = TreeNode("Technology", {"label": "Tech Stack", "type": "category"})
    python_node = TreeNode("Python", {"label": "Programming Language", "version": "3.9"})
    docker_node = TreeNode("Docker", {"label": "Containerization", "version": "20.10"})
    
    tech_node.add_child(python_node)
    tech_node.add_child(docker_node)
    
    tech_node.draw(key="label")
    
    # Demonstrate Unicode characters
    print("\n6. Unicode characters used by draw_tree:")
    print("   ├── : Intermediate child connector")
    print("   └── : Last child connector") 
    print("   │   : Vertical continuation line")
    print("       : Padding for last child")


def example_real_world_scenarios():
    """Demonstrate real-world usage scenarios."""
    print("\n" + "=" * 60)
    print("REAL-WORLD USAGE SCENARIOS")
    print("=" * 60)
    
    # Scenario 1: File system representation
    print("1. File System Representation:")
    fs_root = TreeNode("project", {"definition": "Project root directory"})
    src = TreeNode("src", {"definition": "Source code", "type": "directory"})
    tests = TreeNode("tests", {"definition": "Test files", "type": "directory"})
    
    main_py = TreeNode("main.py", {"definition": "Main application", "size": "2.1KB"})
    utils_py = TreeNode("utils.py", {"definition": "Utility functions", "size": "1.5KB"})
    test_main = TreeNode("test_main.py", {"definition": "Main tests", "size": "3.2KB"})
    
    fs_root.add_child(src)
    fs_root.add_child(tests)
    src.add_child(main_py)
    src.add_child(utils_py)
    tests.add_child(test_main)
    
    draw_tree(fs_root)
    
    # Scenario 2: Decision tree
    print("\n2. Decision Tree for Weather Activities:")
    weather_root = TreeNode("Weather", {"definition": "What should I do today?"})
    
    sunny = TreeNode("Sunny", {"definition": "Go to the beach"})
    rainy = TreeNode("Rainy", {"definition": "Stay inside and code"})
    cloudy = TreeNode("Cloudy", {"definition": "Perfect for hiking"})
    snowy = TreeNode("Snowy", {"definition": "Build a snowman!"})
    
    weather_root.add_child(sunny)
    weather_root.add_child(rainy)
    weather_root.add_child(cloudy)
    weather_root.add_child(snowy)
    
    draw_tree(weather_root)
    
    # Scenario 3: Menu system
    print("\n3. Application Menu System:")
    menu_root = TreeNode("MainMenu", {"definition": "Application Main Menu"})
    
    file_menu = TreeNode("File", {"definition": "File operations"})
    edit_menu = TreeNode("Edit", {"definition": "Edit operations"})
    help_menu = TreeNode("Help", {"definition": "Help and about"})
    
    # File submenu
    new_file = TreeNode("New", {"definition": "Create new file"})
    open_file = TreeNode("Open", {"definition": "Open existing file"})
    save_file = TreeNode("Save", {"definition": "Save current file"})
    
    # Edit submenu
    cut = TreeNode("Cut", {"definition": "Cut selection"})
    copy = TreeNode("Copy", {"definition": "Copy selection"})
    paste = TreeNode("Paste", {"definition": "Paste from clipboard"})
    
    menu_root.add_child(file_menu)
    menu_root.add_child(edit_menu)
    menu_root.add_child(help_menu)
    
    file_menu.add_child(new_file)
    file_menu.add_child(open_file)
    file_menu.add_child(save_file)
    
    edit_menu.add_child(cut)
    edit_menu.add_child(copy)
    edit_menu.add_child(paste)
    
    draw_tree(menu_root)
    
    # Working with the menu tree
    menu_tree = Tree(menu_root)
    print(f"\n   Menu system statistics:")
    print(f"   - Maximum depth: {menu_tree.max_depth()} levels")
    print(f"   - Maximum width: {menu_tree.max_width()} items")
    
    # Find specific menu item
    copy_item = menu_root.get_subtree("Copy")
    if copy_item:
        print(f"   - Found menu item: {copy_item.content['definition']}")


def examples():
    """Run all examples."""
    print("PyTree Library - Comprehensive Usage Examples")
    print("This file demonstrates all features of the pytree module.")
    print("=" * 60)
    print("COPY & PASTE READY CODE EXAMPLES")
    print("=" * 60)
    print("Each example shows both the CODE you can copy/paste")
    print("and the expected OUTPUT when you run it.\n")
    
    # Run all example functions
    example_basic_treenode_operations()
    example_treenode_content_operations()
    example_getitem_operations()
    example_treenode_search_operations()
    example_treenode_modification_operations()
    example_treenode_serialization()
    example_tree_class_operations()
    example_tree_json_operations()
    example_draw_tree_function()
    example_real_world_scenarios()
    
    print("\n" + "=" * 60)
    print("ALL EXAMPLES COMPLETED!")
    print("=" * 60)
    print("HOW TO USE THESE EXAMPLES:")
    print("1. Copy the CODE sections from any example above")
    print("2. Paste into your Python script or interactive session")
    print("3. Make sure to import: from pytree import TreeNode, Tree, draw_tree")
    print("4. Run and see the same OUTPUT as shown")
    print("\nKey takeaways:")
    print("- TreeNode: Individual nodes with content and relationships")
    print("- Tree: Complete tree structure with high-level operations")
    print("- draw_tree: Beautiful ASCII visualization")
    print("- JSON serialization: Save and load tree structures")
    print("- Flexible content: Store any Python object in nodes")
    print("- Search operations: Find nodes by name anywhere in the tree")
    print("\nQuick start: Try running quick_examples() for a shorter demo!")


if __name__ == "__main__":
    examples()