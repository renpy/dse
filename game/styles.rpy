# This file contains styles for the day planner.
# Modify this file to change the alignment and placement of the day planner choices,
# as well as other font and appearance options.

# Place the day planner.
style dayplanner_frame:
    background None
    xalign 0.5
    yalign 0.0
    
style dp_frame:
    ypos 200
    yanchor 0.0
    xalign 0.5
    
# Spacing betweeen the choices and the done button.    
style dp_vbox:
    spacing 20
    
# Vertical spacing between choices
style dp_choice_vbox is dp_vbox:
    spacing 0

# Spacing between the choice columns.
style dp_hbox:
    spacing 20
    
# Center the label of each choice.
style dp_label is label:
    xalign 0.5

# Center the label of each choice.
style dp_label_text:
    text_align 0.5
    
# Make each choice button the same size, and centered.
style dp_button is button:
    size_group dp_choice
    xalign 0.5
    
style dp_button_text:
    xalign 0.5

style dp_choice_text:
    xalign 0.5
    
# Center the done button.
style dp_done_button:
    xalign 0.5
