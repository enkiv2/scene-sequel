# scene-sequel
Caper novel generator


    Usage: scene-sequel.py [[paramname param] ...]
    
    Parameters:
    	world			Filename for world file (pickle format)
    	startingPoint		Name of initial state. (default: 'go about it in the obvious way')
    	endGoal			Name of initial goal state. This begins as the sole member of the goal pool, and when the current state is the endGoal we stop navigating the world. (default 'steal them jewels')
    	MAX			Maximum recursion depth during planning (default: 5)
    	successWeight		Base likelihood for succeeding at a state transition.
    	complicationWeight	Base likelihood for accumulating complications in the goal pool when attempting a state transition.


Currently, the world editor isn't finished. If you want to create your own world, write a structure similar to the world hard-coded into scene-sequel.py into a new python file and then write the pickled version of that structure to a file.

