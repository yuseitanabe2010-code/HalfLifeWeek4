My project this week is a display that shows you live data about my computer. It shows different statistic such as cpu and gpu temperature, usage percentage, along with ram usage. I made it because I really like computers and I'm very interested in them. I even bought the individual parts for my computer and built it myself.

Basically, it uses a built in feature of the computer that tracks data like this, which is then monitored and sent to the raspberry pi. It is then transferred to the display and it shows up there. This is repeated multiple times a second, so it is a live tracker and constantly changes.

I had to write two pieces of code because you need to retrieve the data on the computer, then send it to the raspberry pi which then sends it to the display.

<img width="1228" height="625" alt="pccode" src="https://github.com/user-attachments/assets/bef897c6-c6e8-45cb-acf9-0be04463ed1f" />
This is the code on the computer side. It constantly monitors the stats on there.

<img width="1231" height="514" alt="picocode" src="https://github.com/user-attachments/assets/9556f964-2388-4332-8458-476b8948a632" />
The raspberry pi recieves this data, then breaks it up into individual lines, then prints it on the display.

<img width="847" height="854" alt="betterwiring" src="https://github.com/user-attachments/assets/15d96a8a-eb39-4315-a6a8-d481ec146292" />
This is what the schematic looks like. There aren't amny connections, as it was quite simple.

<img width="363" height="671" alt="pcb" src="https://github.com/user-attachments/assets/807f3a26-e945-419b-ab52-e0090093da56" />
this is the pcb with the corresponding footprints that I assinged to the parts. There is also a copper fill plate on the back to deal with the pins that need to be grounded.

<img width="803" height="558" alt="3d" src="https://github.com/user-attachments/assets/6781fdee-fc2a-4176-a927-46723dcbcee0" />
This is the 3d render, so this is what it will look like when it's finished, plus the actual display.
