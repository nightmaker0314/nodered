[{"id":"7e864dbb.3440d4","type":"rpi-gpio in","z":"941da61f.fb4a18","name":"BUTTON","pin":"11","intype":"up","debounce":"25","read":true,"x":60,"y":100,"wires":[["c67e09fb.5c26a8"]]},{"id":"6a098918.acb938","type":"debug","z":"941da61f.fb4a18","name":"","active":false,"console":"false","complete":"payload","x":590,"y":340,"wires":[]},{"id":"c67e09fb.5c26a8","type":"switch","z":"941da61f.fb4a18","name":"if input is 1","property":"payload","propertyType":"msg","rules":[{"t":"eq","v":"1","vt":"str"},{"t":"else"}],"checkall":"true","outputs":2,"x":190,"y":180,"wires":[["5a6d56.607962ac"],["3e6b732b.9c922c"]]},{"id":"5a6d56.607962ac","type":"change","z":"941da61f.fb4a18","name":"change to 0","rules":[{"t":"set","p":"payload","pt":"msg","to":"0","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":390,"y":160,"wires":[["90a3ee67.92e6c","6a098918.acb938"]]},{"id":"3e6b732b.9c922c","type":"change","z":"941da61f.fb4a18","name":"change  1","rules":[{"t":"set","p":"payload","pt":"msg","to":"1","tot":"str"}],"action":"","property":"","from":"","to":"","reg":false,"x":240,"y":340,"wires":[["90a3ee67.92e6c","6a098918.acb938"]]},{"id":"90a3ee67.92e6c","type":"rpi-gpio out","z":"941da61f.fb4a18","name":"LED","pin":"33","set":"","level":"0","freq":"","out":"out","x":590,"y":420,"wires":[]}]
