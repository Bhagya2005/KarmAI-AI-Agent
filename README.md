
# KarmAI 

**KarmAI** is a multi AI agent system designed to control a computer based on user queries. The system uses a hierarchical agent structure to break down complex tasks into simpler actions handled by specialized agents.

## Architecture

- **Master Agent**  
  The central controller that interprets user queries and delegates tasks to the subordinate agents. It coordinates the overall workflow and ensures that each task is executed in the proper sequence.
  
- **Subordinate Agents**  
  These agents perform the actual operations on the computer:
  - **Keyboardagent**  
    Handles all keyboard-related tasks, including typing text and executing hotkeys.
  - **Vision Mouse Agent**  
    Manages mouse operations and screen analysis. It has two main methods:
    **Pytesseract OCR**: Detects and locates text on the screen by returning its (x, y) coordinates, enabling precise mouse navigation.
    **Vision Language Model (e.g., llama 3.2 90B vision)**: Verifies that the executed actions are accurately reflected on the screen, adding an extra layer of confirmation.


https://github.com/user-attachments/assets/837c882c-9690-4767-8c3c-ad4e705b7bcd



## Summary

KarmAI leverages a master-subordinate architecture to efficiently manage and execute computer control tasks. With its dual-method screen analysis and dedicated agents for keyboard and mouse control, the system is designed for accuracy and ease of use.
