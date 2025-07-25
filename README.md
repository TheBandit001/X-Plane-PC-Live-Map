# X-Plane-PC-Live-Map
View your flight on another PC Map
Windows, Python
For X-plane
You can view your plane on a live map on another Windows PC Computer with your browser.
Most people use there cell phone or tablet.  I couldn't find a PC app for this that was Free,   so here it is.
Run x-plane on PC 1.  
On PC1, go into your Xplane settings > Data Output (General Data Output)
Make sure to checkmark under Network via UDP (3 Speeds, 17 Pitch, Roll & Headings, 20 Lattitude, longitude & Altitude)
Network configuration, checkmark Send network data output
IP Address (Enter the ip address of your PC2 computer)
Port 49002
Click "Done"

PC 2,  copy the files in the main directory c:\xplane_live_map
In directory c:\xplane_live_map, click on START.BAT
(You might need to install Python on your PC 2)
3 Terminal windows will open and your browser localhost:8000 
You should see your plane on the map.

Enjoy!

I will try to add more features in the future.
