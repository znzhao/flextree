# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2025-11-12

### Added
- **ENHANCED**: ActionMemorySystem for comprehensive undo/redo operations across all tree modifications
- Advanced Find and Replace functionality with dialog interface and search result navigation
- Complete node renaming capabilities with direct inline editing in Overview tab
- Support for complex nested structure editing (dictionaries within dictionaries, lists within lists)
- Context menus for both tree viewer and content editor with comprehensive operation options
- Keyboard shortcuts for common operations (Find, Replace, Edit Mode, Tab Navigation)
- Content type auto-detection with appropriate display modes (text vs. table)
- Support for editing list columns with rename and delete operations
- Nested table expansion for viewing deeply nested data structures
- Dialog-based value editing for complex JSON content with format validation
- Status bar displaying clipboard state and action information
- Window title updates reflecting current file and unsaved changes indicator
- Action description system for undo history tracking
- Create content type dialog for initializing new content (text, dict, list of dicts, null)
- Preserve expansion state and selection when refreshing tree after modifications
- Robust error handling with user-friendly error messages throughout UI operations

### Enhanced
- TreeViewerPanel with improved context menus and expand/collapse all functionality
- InfoViewerPanel with tabbed interface for Overview, Content, and Children information
- Content editing workflow with modal dialogs and validation
- File operations with proper unsaved changes detection and user prompts
- Node information display with complete path, depth, width, and subtree statistics
- Table display for dictionaries and lists of dictionaries with inline cell editing
- Edit mode toggle with keyboard shortcut (Ctrl+E) and visual UI feedback
- Tab navigation with Ctrl+Tab and Ctrl+Shift+Tab for quick switching
- Save/Cancel workflow with original content preservation for safe editing
- Children tab displays comprehensive statistics for each child node

### Fixed
- Shortcut handling improvements in UI interactions
- State preservation during undo/redo operations
- Content editing with proper validation and error recovery
- Node selection persistence after tree modifications
- Memory management in nested structure editing

## [0.2.1] - 2025-11-06

### Enhanced
- Fix the shortcut problems for the UI.

## [0.2.0] - 2025-11-02

### Added
- **NEW**: FlexTree JSON UI - A comprehensive graphical interface for viewing and exploring tree structures
- Interactive tree navigation with expandable/collapsible nodes
- Detailed node information viewer with tabbed interface (Overview, Content, Children)
- Advanced content editing capabilities with support for text, dictionaries, and lists
- Table view for dictionaries and lists of dictionaries with inline editing
- Complete clipboard operations (cut, copy, paste, delete) with context menus
- Undo/redo system with 20-step action history
- Save/Save As functionality with unsaved changes tracking
- Find and replace operations across node names and content
- Automatic tab switching to Content tab when entering edit mode
- Window title updates with filename and unsaved changes indicator (*)
- Comprehensive keyboard shortcuts and right-click context menus

### Enhanced
- Tree viewer with expand/collapse all functionality
- Node renaming with uniqueness validation
- Content type detection and appropriate display formatting
- File operations with proper unsaved changes handling
- Status bar showing clipboard and action information

## [0.1.8] - 2025-11-01

### Added
- **NEW**: Copy and Deep Copy functionality for TreeNode and Tree classes
- `TreeNode.copy()`: Create shallow copy of node without children or parent relationships
- `TreeNode.deepcopy()`: Create deep copy of node with entire subtree and independent content
- `Tree.copy()`: Create shallow copy of tree (root node only, no children)
- `Tree.deepcopy()`: Create deep copy of entire tree structure with full independence
- Comprehensive test coverage for all copy operations in `test_flextree.py`
- Copy examples and demonstrations in `examples.py`

### Enhanced
- Added `import copy` module support for deep copying functionality
- Deep copy ensures complete independence of content and structure
- Shallow copy provides fast duplication with shared content references
- Perfect for template systems, backup creation, and safe experimentation
- Full backward compatibility maintained with existing code

### Documentation
- Updated README.md with comprehensive copy operations section
- Added API documentation for new copy methods
- Enhanced examples with practical copy use cases
- Updated version to 0.1.8 in project metadata

## [0.1.7] - 2025-10-31

### Added
- **NEW**: FlexTree JSON UI - A complete graphical user interface
- TreeViewerPanel class for interactive tree structure display
- InfoViewerPanel class for detailed node information viewing
- FlexTreeUI main class with resizable left/right panels
- Support for JSON file loading and saving through GUI
- Comprehensive node information display (overview, content, statistics, children)
- Sample tree creation function for demonstration
- Menu system with File, View, and Help menus
- Expandable/collapsible tree navigation
- Real-time node selection and information updates

### Enhanced
- JSON import/export functionality integrated with GUI
- Tree visualization with interactive exploration
- Node statistics and content analysis tools

## [0.1.6] - 2025-10-14

### Changed
- Cleaned up package imports in `__init__.py`
- Removed `quick_examples` from imports to streamline API
- Updated `__all__` list to include only core exports: `["TreeNode", "Tree", "draw_tree", "examples"]`
- Maintained backward compatibility with all existing features
- Prepared for future enhancements and optimizations
- Consolidated changelog documentation

### Documentation
- Added dedicated CHANGELOG.md file
- Improved version tracking and release documentation
- Simplified changelog entries for better readability

## [0.1.5] - 2024-XX-XX

### Added
- Pythonic getitem functionality for Tree objects
- Comprehensive test coverage for count and getitem operations
- Enhanced examples with copy-paste ready CODE/OUTPUT format

### Changed
- Updated TreeNode behavior: removed getitem support (use Tree objects instead)
- Refined Tree getitem to support string-only lists for multiple selection

### Documentation
- Improved documentation with comprehensive getitem usage guide
- Updated package documentation and README with getitem introduction

## [0.1.4] - 2024-XX-XX

### Added
- count() methods to TreeNode and Tree classes
- Enhanced tree statistics functionality

### Documentation
- Updated examples and documentation

## [0.1.3] - 2024-XX-XX

### Changed
- Package name changed to "Flex Tree"
- Improved package structure and imports

### Added
- quick_examples and examples functions to public API

## [0.1.2] - 2024-XX-XX

### Fixed
- Bug fixes and improvements

### Enhanced
- Enhanced tree manipulation methods

## [0.1.1] - 2024-XX-XX

### Documentation
- Minor updates and documentation improvements

## [0.1.0] - 2024-XX-XX

### Added
- Initial release
- Basic tree node and tree operations
- JSON serialization support
- Tree visualization
- Comprehensive test suite

### Features
- TreeNode class for individual nodes
- Tree class for complete tree structures
- draw_tree function for ASCII visualization
- Support for storing any Python object as node content
- Search operations by name or index
- Tree statistics (depth, width, node count)