Overview:

- I did not implement 6.5 and 6.6.

- Some error handling for inputs are not implemented. 
    So program simply exists with error -1

- My web visualization only works for 1 client at a time 
    (or one client per functionality).
    Non-pretty solution that allows some kind of 
    multi-user:
        only deleting the oldest 1000 (or 10000.. 
        depends on expected throughput) files 
        (in temperature_CO2_plotter.py)
        or not deleting files at all.

- I am sure, that things could have been done prettier, 
    (specially the pandas part) but I implemented it 
    before the lecture on pandas ;)

- 6.4. “takes as input an upper/lower threshold, 
    and generates a bar chart of the CO2 emissions 
    of all countries with per capita emissions 
    above/below that threshold”
		
    I understand it like this that we should
    plot all that are either above upper or below 
    lower threshold. If something different was asked
    then the task should have been rephrased 
    in my opinion. (I mapped upper&above and lower&below)

