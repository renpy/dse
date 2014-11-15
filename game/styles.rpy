# This file contains styles for the day planner.
# Modify this file to change the alignment and placement of the day planner choices

# Place the day planner.
style dp_frame:
    ypos 120
    yanchor 0.0
    xalign 0.5
    
# Spacing betweeen the choices and the done button.    
style dp_vbox:
    box_spacing 20

# Spacing between the choice columns.
style dp_hbox:
    box_spacing 20
    
# Center the choices.    
style dp_choice:
    xalign 0.5

# Center the label of each choice.
style dp_label:
    xalign 0.5

# Center the label of each choice.
style dp_label_text:
    text_align 0.5
    
# Make each choice button the same size, and centered.
style dp_choice_button:
    size_group dp_choice
    xalign 0.5
    
style dp_choice_text:
    xalign 0.5
    
# Center the done button.
style dp_done_button:
    xalign 0.5

# Put a margin on the stats frame.
style stats_frame:
    xmargin 10
    ymargin 5
    
# Space between the label and the stats.
style stats_vbox:
    box_first_spacing 10
    
# Put blank space around each stat name, and right-justify.
style stat_label:
    xminimum 140
    xalign 1.0
    xmargin 5
    
# Put blank space around each stat value, and right-justify.
style stat_value_label:
    xminimum 100
    xalign 1.0
    
# Center the stat bar vertically.
style stat_bar:
    yalign 0.5