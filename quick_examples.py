#!/usr/bin/env python3
"""
PyTree Quick Start Examples

A concise demonstration of the most important features of the pytree module.
Perfect for getting started quickly.

Run: python quick_examples.py
"""

from pytree import TreeNode, Tree, draw_tree
import json
import tempfile
import os


def quick_start_example():
    """Quick start guide - most common operations."""
    print("PyTree Quick Start Guide")
    print("=" * 40)
    
    # 1. Create a simple tree
    print("\n1. Creating a simple tree:")
    root = TreeNode("Company", "Acme Corp")
    engineering = TreeNode("Engineering", "Tech Team")
    marketing = TreeNode("Marketing", "Growth Team")
    
    root.add_child(engineering)
    root.add_child(marketing)
    
    # Add sub-teams
    backend = TreeNode("Backend", "Server Development")
    frontend = TreeNode("Frontend", "UI Development")
    engineering.add_child(backend)
    engineering.add_child(frontend)
    
    print("Tree structure:")
    draw_tree(root)
    
    # 2. Use Tree class for operations
    print("\n2. Using Tree class for operations:")
    company_tree = Tree(root)
    
    # Add new department
    hr = TreeNode("HR", "Human Resources")
    company_tree.insert("Company", hr)
    
    # Modify existing content
    company_tree.alter("Backend", "Backend & DevOps")
    
    print("Updated tree:")
    draw_tree(company_tree.root)
    
    # 3. Get statistics
    print(f"\n3. Tree statistics:")
    print(f"   Depth: {company_tree.max_depth()} levels")
    print(f"   Width: {company_tree.max_width()} max nodes at one level")
    
    # 4. Search operations
    print(f"\n4. Finding nodes:")
    eng_dept = company_tree.get("Engineering")
    if eng_dept:
        print(f"   Found Engineering department with {len(eng_dept.root.children)} teams")
        draw_tree(eng_dept.root)
    
    # 5. JSON serialization
    print(f"\n5. JSON serialization:")
    temp_file = "temp_tree.json"
    try:
        company_tree.save_json(temp_file)
        loaded_tree = Tree.load_json(temp_file)
        print(f"   Saved and loaded successfully!")
        print(f"   Loaded tree has {len(loaded_tree.root.children)} top-level departments")
    finally:
        if os.path.exists(temp_file):
            os.unlink(temp_file)


def dictionary_content_example():
    """Show how dictionary content works with draw_tree."""
    print("\n" + "=" * 40)
    print("Dictionary Content Example")
    print("=" * 40)
    
    # Create nodes with dictionary content
    root = TreeNode("Languages", {"definition": "Programming Languages"})
    
    python = TreeNode("Python", {
        "definition": "High-level programming language",
        "year": 1991,
        "creator": "Guido van Rossum",
        "typing": "dynamic"
    })
    
    javascript = TreeNode("JavaScript", {
        "definition": "Web programming language", 
        "year": 1995,
        "creator": "Brendan Eich",
        "typing": "dynamic"
    })
    
    # Node without 'definition' key
    java = TreeNode("Java", {
        "year": 1995,
        "creator": "James Gosling",
        "typing": "static"
    })
    
    root.add_child(python)
    root.add_child(javascript)
    root.add_child(java)
    
    print("Dictionary content with 'definition' key shows nicely:")
    draw_tree(root)
    
    print(f"\nFull Python data: {python.content}")
    
    # Demonstrate custom key
    print("\n" + "-" * 40)
    print("Custom Key Example")
    print("-" * 40)
    
    # Create nodes with custom keys
    tools_root = TreeNode("DevTools", {"name": "Development Tools"})
    
    editor = TreeNode("VSCode", {
        "name": "Visual Studio Code",
        "type": "Editor",
        "company": "Microsoft"
    })
    
    browser = TreeNode("Chrome", {
        "name": "Google Chrome", 
        "type": "Browser",
        "company": "Google"
    })
    
    tools_root.add_child(editor)
    tools_root.add_child(browser)
    
    print("Using 'name' as key:")
    draw_tree(tools_root, key="name")
    
    print("\nUsing 'company' as key:")
    draw_tree(tools_root, key="company")


def real_world_menu_example():
    """Real-world example: Application menu system."""
    print("\n" + "=" * 40)
    print("Real World Example: Menu System")
    print("=" * 40)
    
    # Create a menu system
    main_menu = TreeNode("MainMenu", {"definition": "Application Menu"})
    
    # Top-level menus
    file_menu = TreeNode("File", {"definition": "File Operations"})
    edit_menu = TreeNode("Edit", {"definition": "Edit Operations"})
    view_menu = TreeNode("View", {"definition": "View Options"})
    help_menu = TreeNode("Help", {"definition": "Help & About"})
    
    # File submenu
    new_item = TreeNode("New", {"definition": "Create new document", "shortcut": "Ctrl+N"})
    open_item = TreeNode("Open", {"definition": "Open existing document", "shortcut": "Ctrl+O"})
    save_item = TreeNode("Save", {"definition": "Save document", "shortcut": "Ctrl+S"})
    exit_item = TreeNode("Exit", {"definition": "Exit application", "shortcut": "Alt+F4"})
    
    # Build menu structure
    main_menu.add_child(file_menu)
    main_menu.add_child(edit_menu)
    main_menu.add_child(view_menu)
    main_menu.add_child(help_menu)
    
    file_menu.add_child(new_item)
    file_menu.add_child(open_item)
    file_menu.add_child(save_item)
    file_menu.add_child(exit_item)
    
    print("Application menu structure:")
    draw_tree(main_menu)
    
    # Work with the menu as a Tree
    menu_system = Tree(main_menu)
    
    # Find specific menu items
    save_option = main_menu.get_subtree("Save")
    if save_option:
        print(f"\nFound Save option: {save_option.content['definition']}")
        print(f"Keyboard shortcut: {save_option.content['shortcut']}")
    
    # Add a new menu item
    print(f"\nAdding 'Recent Files' to File menu:")
    recent_files = TreeNode("Recent", {"definition": "Recently opened files"})
    menu_system.insert("File", recent_files)
    
    # Show just the File menu
    file_subtree = menu_system.get("File")
    if file_subtree:
        print("Updated File menu:")
        draw_tree(file_subtree.root)


def tree_modification_example():
    """Show various ways to modify trees."""
    print("\n" + "=" * 40)
    print("Tree Modification Example")
    print("=" * 40)
    
    # Create initial team structure
    team = TreeNode("DevTeam", "Software Development Team")
    alice = TreeNode("Alice", "Team Lead")
    bob = TreeNode("Bob", "Senior Dev")
    charlie = TreeNode("Charlie", "Junior Dev")
    
    team.add_child(alice)
    team.add_child(bob)
    team.add_child(charlie)
    
    print("Initial team:")
    draw_tree(team)
    
    # Using TreeNode methods directly
    print("\n1. Remove Charlie (using TreeNode.remove_child):")
    team.remove_child("Charlie")
    draw_tree(team)
    
    # Add new members
    print("\n2. Add new team members:")
    diana = TreeNode("Diana", "DevOps Engineer")
    eve = TreeNode("Eve", "QA Engineer")
    team.add_child(diana)
    team.add_child(eve)
    draw_tree(team)
    
    # Using Tree class methods
    print("\n3. Using Tree class for modifications:")
    dev_team = Tree(team)
    
    # Add intern under Alice
    intern = TreeNode("Frank", "Software Engineering Intern")
    dev_team.insert("Alice", intern)
    
    # Update job titles
    dev_team.alter("Alice", "Engineering Manager")
    dev_team.alter("Bob", "Principal Engineer")
    
    print("Final team structure:")
    draw_tree(dev_team.root)
    
    print(f"\nTeam statistics:")
    print(f"- Team depth: {dev_team.max_depth()} levels")
    print(f"- Max team size at one level: {dev_team.max_width()} people")


if __name__ == "__main__":
    print("PyTree - Quick Examples")
    print("These examples show the most important features of pytree.")
    print("For comprehensive examples, see examples.py")
    
    quick_start_example()
    dictionary_content_example()
    real_world_menu_example()
    tree_modification_example()
    
    print("\n" + "=" * 40)
    print("Quick Examples Complete!")
    print("=" * 40)
    print("Next steps:")
    print("- Run 'examples.py' for comprehensive demonstrations")
    print("- Check the README.md for detailed documentation")
    print("- Run the test suite with 'python -m unittest test_pytree.py'")