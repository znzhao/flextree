# FlexTree JSON UI - Clipboard System Implementation

## Overview
The FlexTree JSON UI now includes a comprehensive clipboard system that allows users to cut, copy, and paste tree nodes with full support for deep copying and automatic name collision resolution.

## Features Implemented

### 1. Clipboard Operations
- **Cut (Ctrl+X)**: Removes node from tree and places it in clipboard for moving
- **Copy (Ctrl+C)**: Creates deep copy of node and places it in clipboard
- **Paste (Ctrl+V)**: Inserts clipboard contents into selected target node
- **Delete (Del)**: Permanently removes selected node from tree

### 2. Deep Copy System
- Creates complete deep copies of TreeNode objects including all children
- Uses recursive copying to preserve entire subtree structure
- Preserves all content data using Python's `copy.deepcopy()`

### 3. Name Collision Resolution
- Automatically checks for name conflicts when pasting
- Appends "(1)", "(2)", etc. to resolve naming conflicts
- Checks uniqueness across entire tree, not just immediate siblings
- Ensures all pasted nodes have unique names

### 4. User Interface Integration
- **Keyboard Shortcuts**: Standard Ctrl+X, Ctrl+C, Ctrl+V, Del
- **Menu Integration**: Edit menu with clipboard operations
- **Context Menu**: Right-click menu on tree nodes
- **Status Bar**: Shows current clipboard state and contents

### 5. Enhanced Context Menu
- Cut, Copy, Paste, Delete operations
- Expand/Collapse subtree operations
- Dynamic menu based on node state (e.g., no delete for root)

### 6. Clipboard State Management
- Maintains clipboard buffer until new cut/copy operation
- Distinguishes between cut and copy modes
- Clears clipboard after cut operation is completed
- Visual feedback in status bar showing clipboard contents

### 7. Safety Features
- Prevents cutting/deleting root node
- Confirmation dialog for delete operations
- Error handling with user-friendly messages
- Validation of selected nodes before operations

## Usage Instructions

### Basic Operations
1. **To Copy a Node**:
   - Select the node in the tree view
   - Press Ctrl+C or right-click and select "Copy"
   - Status bar will show "Copied: 'NodeName'"

2. **To Cut a Node**:
   - Select the node in the tree view
   - Press Ctrl+X or right-click and select "Cut" 
   - Status bar will show "Cut: 'NodeName'"

3. **To Paste a Node**:
   - Select the target parent node
   - Press Ctrl+V or right-click and select "Paste"
   - Node will be added as child with unique name

4. **To Delete a Node**:
   - Select the node to delete
   - Press Del or right-click and select "Delete"
   - Confirm deletion in dialog box

### Advanced Features
- **Name Resolution**: If pasting "Sales Team" into a node that already has "Sales Team", it becomes "Sales Team (1)"
- **Deep Structure**: Copying a node copies all its children and their content
- **Cut Behavior**: After cutting, original node remains until successful paste
- **Status Tracking**: Status bar shows current clipboard state

## Technical Implementation

### Key Classes Modified
- **FlexTreeUI**: Main clipboard logic, keyboard bindings, menu integration
- **TreeViewerPanel**: Context menu, selection handling
- **Status Bar**: Added clipboard state display

### Key Methods Added
- `_cut_node()`: Cut selected node to clipboard
- `_copy_node()`: Copy selected node to clipboard  
- `_paste_node()`: Paste clipboard contents to selected location
- `_delete_node()`: Delete selected node from tree
- `_deep_copy_node()`: Create deep copy of TreeNode
- `_get_unique_name()`: Generate unique names for pasted nodes
- `_setup_clipboard_bindings()`: Configure keyboard shortcuts
- `_create_status_bar()`: Create status bar UI

### Clipboard Data Structure
```python
self.clipboard = [TreeNode, ...]  # List of copied/cut nodes
self.clipboard_mode = 'cut' | 'copy'  # Operation mode
```

## Example Scenarios

### Scenario 1: Copying Department Structure
1. Select "Engineering" department node
2. Press Ctrl+C to copy
3. Select "Company" root node  
4. Press Ctrl+V to paste
5. Result: "Engineering (1)" appears with all sub-teams copied

### Scenario 2: Moving Team Between Departments
1. Select "Backend Team" under Engineering
2. Press Ctrl+X to cut
3. Select "Sales" department
4. Press Ctrl+V to paste
5. Result: Backend Team moves to Sales, original removed

### Scenario 3: Handling Name Conflicts
1. Copy "Sales Team 1" 
2. Paste into same Sales department
3. Result: Creates "Sales Team 1 (1)" automatically
4. Paste again: Creates "Sales Team 1 (2)"

## Error Handling
- Invalid selections show warning messages
- Failed operations display error dialogs
- Clipboard validation prevents invalid states
- Graceful handling of edge cases (root node operations, empty selections)

This implementation provides a robust, user-friendly clipboard system that enhances the FlexTree JSON UI with professional-grade editing capabilities.