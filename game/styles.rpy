# This file contains styles for the day planner.
# Modify this file to change the alignment and placement of the day planner choices,
# as well as other font and appearance options.

# Place the day planner.
style dayplanner_window:
    background None
    
style dp_frame:
    ypos 150
    yanchor 0.0
    xalign 0.5
    
# Spacing betweeen the choices and the done button.    
style dp_vbox:
    box_spacing 20

# Spacing between the choice columns.
style dp_hbox:
    box_spacing 20
    
    
# Center the choices.    
style dp_choice is default:
    xalign 0.5

# Center the label of each choice.
style dp_label is label:
    xalign 0.5

# Center the label of each choice.
style dp_label_text:
    text_align 0.5
    
# Make each choice button the same size, and centered.
style dp_choice_button is button:
    size_group dp_choice
    xalign 0.5
    
style dp_choice_button_text is button_text

style dp_choice_text:
    xalign 0.5
    
# Center the done button.
style dp_done_button:
    xalign 0.5
