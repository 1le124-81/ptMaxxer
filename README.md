When run, it uses a python module (pytautogui) to replicate the inputs usually needed to get microsoft reward points. Currently it runs 35 searches and clicks each item on the daily set. This gives at least 180 points daily (150 points max for searching, at least 30 for daily sets). 

There are also streaks for every day you do the daily set, which give you more points the longer the streak is. I do not know the rate at which the points increase but it is substantial enough that the script needs to be run daily to be effective.

The code itself is relatively primitive, with it just being simple coordinated clicks reliant on the browser being fullscreened on laptop monitor to be effective. The daily set is marginally more advanced. It scrolls down until the cursor hits a color, and that is where the daily set is. While not too elegant, it gets the job done and the stakes for failing aren't that drastic so I just left it be.

Requires pyautogui. display scale set to 150% in this code, probably not compatible with most devices.

Replicates input at a human pace, not overly speedy or effective.

Requires lot of configuration.
