# Senior-Project
Amyotrophic Lateral Sclerosis (ALS), also known as motor neuron disease, is a disease that does not impair the mental functions of the patient, but gradually loses muscle control. However, the eyelids of the patient do not lose their function for a long time. For this reason, blink communication is a recommended solution for ALS patients. What is desired within the scope of the project is coding around 10 words as blink, resolving the blink message using signal processing techniques and writing on the Raspberry Pi Screen. 

The project detects the amount of blink in spesific time and understand the meaning of blink. For example, ıf there is 4 blinks in 10 seconds, which means the user wants cocounat or 5 times blinking means that user want to have apple.

<b>Library</b> 

<b>1.numpy</b>

<b>2.cv2</b>

<b>3.dlib</b> 

<b>4.time</b>

To understand our project, you can read final report of presentation from https://github.com/btknzn/Senior-Project/blob/master/ELE%20495%20Final%20Report.pdf and also you can read Report-1 and Report-2 for seeing the problem, which ı lived. 

You can download senior project poster from https://github.com/btknzn/Senior-Project/blob/master/SeniorProjectPoster.ppt via cliking wiev rar.

 In this project, we trained landmarks detector via Dlib library and then we counted amount of blink. For traning dataset, it is supposed to download dlib library from https://ibug.doc.ic.ac.uk/resources/facial-point-annotations/ and the code trained model after that the system count calculate whether the eye is or open or not and then the code counts blink amount in ten seconds and offers the desired food via eye blinking communcation.
 
 To better understanding, you could read the final report of presentation mentioned above.
