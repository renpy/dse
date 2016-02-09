# stats.rpy
# Keeps track of and displays the stats for the DSE.
#
# To change styles, add a style block for the element you want
# preceded by "dse_stats_" down below

init -100 python:

    __dse_stats = [ ]

    class __Stat(object):

        def __init__(self, name, var, default, max):
            self.name = name
            self.var = var
            self.default = default
            self.max = max

    def __init_stats():
        for s in __dse_stats:
            setattr(store, s.var, s.default)

    config.start_callbacks.append(__init_stats)
    
    def register_stat(name, var, default, max):
        __dse_stats.append(__Stat(name, var, default, max))

    def normalize_stats():
        for s in __dse_stats:

            v = getattr(store, s.var)

            if v > s.max:
                v = s.max
            if v < 0:
                v = 0

            setattr(store, s.var, v)

    # Whenever a python statement is executed, we will ensure our stats
    # stay within range.
    config.python_callbacks.append(normalize_stats)
                        

# Here you can change the style of any elements in the Stats screen you want.
# Put a margin on the stats frame.
style dse_stats_frame:
    xmargin 10
    ymargin 5
    
# Space between the label and the stats.
style dse_stats_vbox:
    box_first_spacing 20
    
# Put blank space around each stat name, and right-justify.
style dse_stats_label:
    xminimum 140
    xalign 1.0
    xmargin 5
    
# Put blank space around each stat value, and right-justify.
style dse_stats_value_label:
    xminimum 100
    xalign 1.0
    
# Center the stat bar vertically.
style dse_stats_bar:
    yalign 0.5

# Display the stats in a frame.
# name -  display the stat's name
# bar -   display a bar indicating the value of the stat
# value - display the numerical value of the stat
# max -   display the maximum value of the stat
screen display_stats(name=True, bar=True, value=True, max=True):
    $ dse_stat_length = len(__dse_stats)
    frame:
        style_group "dse_stats"        
        yalign 0.0
        xalign 0.5

        vbox:
            yalign 0.0
            xalign 0.5
            label "Statistics" xalign 0.5

            # Depending on what the user chooses to display, calculate how many columns we need
            $ num_columns = 0
            if name:
                $ num_columns+=1
            if bar:
                $ num_columns+=1
            if value or max:
                $ num_columns+=1
                
            # Make a grid with up to 3 columns and as many rows as there are stats.
            grid num_columns dse_stat_length:
                xalign 0.5
                yalign 0.5
                spacing 5
                
                for s in __dse_stats:
                    $ v = getattr(store, s.var)

                    if name:
                        label s.name
                    
                    if bar:
                        bar value v range s.max xmaximum 150 xalign 0.0
                        
                    if value and max:
                        label ("%d/%d" % (v, s.max)) xalign 1.0
                    elif value:
                        label ("%d" % (v,)) xalign 1.0
                    elif max:
                        label ("%d" % (s.max,)) xalign 1.0
