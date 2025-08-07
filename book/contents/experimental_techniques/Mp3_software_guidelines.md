# Mp3 Software Guidelines

This chapter provides a guideline on how to use the Mp3 software. 

## How to install Mp3
Step 1: If you have downloaded Mp3 from the USB to your computer, open the software. You are starting a new configuration, so the page should be empty. First, load a script. This script is used to read the green box (which records the forces from the sensors). Click ‘Scripts’ and then ‘Start Script’. 

<img width="500" height="126" alt="image" src="https://github.com/user-attachments/assets/f2a6a101-108c-4041-8563-d76120e51fef" />

Check the number the green box you are using. In this case, we use box 11.

<img width="500" height="317" alt="image" src="https://github.com/user-attachments/assets/b4421a5d-56e2-4c86-9ed4-372610a6a567" />

Then, add a page by right-clicking. You will see your page appear in the bottom right corner. 

<img width="176" height="100" alt="image" src="https://github.com/user-attachments/assets/7b01ddbe-6ac2-4b56-88f7-515e756bbf96" />
<img width="277" height="100" alt="image" src="https://github.com/user-attachments/assets/ced15f0a-c117-4a0a-9768-dd084f50020a" />

Step 2: In your script (open in Finder), check if the number of the green box corresponds to the number the script is loading, in this case it is 11. Also, check the number of the page. 

<img width="500" height="451" alt="image" src="https://github.com/user-attachments/assets/c1d8dab7-5d60-4def-9219-373ee36996c4" />

_If you use more green boxes because you are running the experiment with more sensors, you can add additional scripts. Make sure to change the box number. You can also change the number of the first channel under 'firstchannel' in each script to avoid overlapping channel numbers._

Step 3: Add channels to your script by clicking on 'Settings'. 

<img width="500" height="123" alt="image" src="https://github.com/user-attachments/assets/836fb851-dcaf-459a-abfe-a12882875f95" />

A setup dialog will appear. Click on 'Add Channels'. 

<img width="300" height="269" alt="image" src="https://github.com/user-attachments/assets/4b8c5130-2123-48ab-83ee-f04fd9029587" />

Choose as many channels as you want, it is better to add too many channels than too few. Also, check in the setup dialog if your script is loaded under 'Scripts'. Click 'Ok'. 

<img width="500" height="360" alt="image" src="https://github.com/user-attachments/assets/1c6ef77e-4190-4637-8cd1-d9905b02574e" />

Then click the 'Channels' tab in the setup dialog and right-click a channel. Here you can change the settings of your channel. Make sure 'Median' is selected to filter the output. 

<img width="500" height="297" alt="image" src="https://github.com/user-attachments/assets/3b5899eb-2261-411d-b60f-3c3542eb17f8" />

Step 4: Click and drag your mouse to create a toolbar. You will see the following options appear. Create a 'Num View' and click on 'A Largelist Type'. 

<img width="200" height="261" alt="image" src="https://github.com/user-attachments/assets/d8c97322-1e58-48c8-823f-21870037e112" />

Add to the Num View the channels you want to monitor for forcing. Righ-click and select 'Properties'. Then choose the channels you want to display. In this case, we select channels 000 to 003. Choose ‘Filtered’ and click ‘Ok’.  

<img width="300" height="224" alt="image" src="https://github.com/user-attachments/assets/fd6d3267-f646-453d-9161-92b4a3165986" />

Step 5: Drag your mouse again and add a 'Graph View'. Right-click and select 'Properties. Here you can adjust the X and Y scales and select which channels to display in your graph. 

<img width="500" height="394" alt="image" src="https://github.com/user-attachments/assets/91970c3a-3782-472c-b896-9fd2574b1166" />

_Under the tab 'Scope Overall Settings', you can select 'Use Time Format' and 'Time Absolute'. This displays the current time on your graph. It can be helpful if you want to record the forcing from multiple sensors separtely, as it allows you to easily compare the forcing at specific times._

Step 6: If you safe your configuration, you won't need to repeat all these steps next time. 

<img width="500" height="259" alt="image" src="https://github.com/user-attachments/assets/72c82577-3d2a-4b1c-9672-5844dcf067d5" />


## How to use Mp3
If everything is sep up on your computer, you only need to use the table shown in the figure below to read the forcing. Note that in Mp3, the channels are numbered starting from 0, so sensor 1 correspond to channel 0. 

<img width="300" height="279" alt="image" src="https://github.com/user-attachments/assets/edb7a780-1d2d-486c-80f9-b455e2a6c36e" />


## How to calibrate the sensors with Mp3
To calibrate the sensors, follow these steps. At least three reference points are used to obtain a reliable calibration. 

Step 1: click right on the channel you want to calibrate and choose 'set zero'

<img width="300" height="246" alt="image" src="https://github.com/user-attachments/assets/fc73c200-3b41-4b8b-92cf-f16714258193" />

Step 2: click 'tools' and then 'calibrate'

<img width="500" height="162" alt="image" src="https://github.com/user-attachments/assets/49d8011b-79fe-4096-87d5-c47cfb33d56a" />

Step 3: choose your channel

<img width="500" height="515" alt="image" src="https://github.com/user-attachments/assets/643eccc7-0acc-43c8-8342-c9179bcb2835" />

Step 4: add a calibration point to this channel, here an example of a weight of 1 N is used, click 'add point'

<img width="500" height="507" alt="image" src="https://github.com/user-attachments/assets/688eaf87-a1db-4905-b34e-acf9a31256a5" />  

Step 5: if you have added your 3 reference points, click 'set channel'. The following note will appear

<img width="500" height="512" alt="image" src="https://github.com/user-attachments/assets/4fbac58b-4ca6-4cf3-862b-6ccb71b17839" />  


Click 'ok'and then click 'ready'. Repeat this process for all the sensors you plan to use. If you safe your configuration, Mp3 will remember the calibration factors, so the next time you work with the experiment, you won't need to calibrate again. 



