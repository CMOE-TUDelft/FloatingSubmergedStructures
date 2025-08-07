# Mp3 Software Guidelines

This chapter provides a guideline on how to use the Mp3 software. 

## How to install Mp3
Step 1: If you have downloaded Mp3 from the USB to your computer, open the software. You are starting a new configuration, so the page should be empty. First, load a script. This script is used to read the green box (which records the forces from the sensors). Click ‘Scripts’ and then ‘Start Script’. 

<img width="500" height="126" alt="image" src="https://github.com/user-attachments/assets/f2a6a101-108c-4041-8563-d76120e51fef" />

Check the number the green box you are using. In this case, we use box 11.

<img width="500" height="317" alt="image" src="https://github.com/user-attachments/assets/b4421a5d-56e2-4c86-9ed4-372610a6a567" />

Then, add a page by right-clicking. You will see your page appear in the bottom right corner. 

<img width="182" height="103" alt="image" src="https://github.com/user-attachments/assets/7b01ddbe-6ac2-4b56-88f7-515e756bbf96" />
<img width="310" height="103" alt="image" src="https://github.com/user-attachments/assets/ced15f0a-c117-4a0a-9768-dd084f50020a" />

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

<img width="500" height="373" alt="image" src="https://github.com/user-attachments/assets/fd6d3267-f646-453d-9161-92b4a3165986" />

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

Step 1: Right-click on the channel you want to calibrate and choose 'Set Zero'.

<img width="300" height="246" alt="image" src="https://github.com/user-attachments/assets/fc73c200-3b41-4b8b-92cf-f16714258193" />

Step 2: Click 'Tools' and then 'Calibrate'.

<img width="500" height="162" alt="image" src="https://github.com/user-attachments/assets/49d8011b-79fe-4096-87d5-c47cfb33d56a" />

Step 3: Choose your channel.

<img width="500" height="515" alt="image" src="https://github.com/user-attachments/assets/643eccc7-0acc-43c8-8342-c9179bcb2835" />

Step 4: Add a calibration point to this channel, here an example of a weight of 1 N is used, click 'Add Point'.\
_If you use for example a weight of 50g for the first calibration, note that you need to change the units to Newtons (F = m * g)_

<img width="500" height="507" alt="image" src="https://github.com/user-attachments/assets/688eaf87-a1db-4905-b34e-acf9a31256a5" />  

Step 5: If you have added your 3 reference points, click 'Set Channel'. The following note will appear.

<img width="500" height="512" alt="image" src="https://github.com/user-attachments/assets/4fbac58b-4ca6-4cf3-862b-6ccb71b17839" />  

Click 'Ok'and then click 'Ready'. Repeat this process for all the sensors you plan to use. If you safe your configuration, Mp3 will remember the calibration factors, so the next time you work with the experiment, you won't need to calibrate again. 

## How to record with Mp3
If you want to record the forcing  from each sensor, follow the steps below. 

Step 1: Set your channels to zero. 

<img width="300" height="194" alt="image" src="https://github.com/user-attachments/assets/8e6166c2-5f2a-48c4-9b88-4085a481c734" />

Step 2: Click 'Start New'.

<img width="500" height="95" alt="image" src="https://github.com/user-attachments/assets/bdecbb41-dfe5-4b7e-811e-059f028c6099" />

Step 3: Click 'New Profile'. _This step only needs to be done once, after that, you just need to select your profile._ 

<img width="500" height="277" alt="image" src="https://github.com/user-attachments/assets/e7f78be2-d7c4-4dc8-8389-a42291f16e5f" />

Step 4: Select all channels for which you want to generate output. 

<img width="500" height="759" alt="image" src="https://github.com/user-attachments/assets/eb2d9f76-f44e-4b70-8831-a4ad24a46087" />

Step 5: Select the profile and click 'Ready'. 

<img width="500" height="253" alt="image" src="https://github.com/user-attachments/assets/7a56fc5e-22c5-462a-bf35-aca362d30253" />

Step 6: Name your file and click 'Start'. 

<img width="300" height="465" alt="image" src="https://github.com/user-attachments/assets/859c57ea-7fbb-4727-96ca-d13ac2d05eae" />

Step 7: Stop recording. 

<img width="500" height="150" alt="image" src="https://github.com/user-attachments/assets/8251a5d7-7470-4ea0-848a-1b98b6086bcd" />

Step 8: Export and safe your datafile.

<img width="500" height="170" alt="image" src="https://github.com/user-attachments/assets/71ebea5d-b081-47a7-ac61-f7740db4030f" />



