# Driver_Drowsiness_Detection_System
<hr></hr>

## Introduction

In this project we aim to develop a prototype drowsiness detection system. This system works by monitoring the eyes of the driver and sounding an alarm when he/she is  feeling drowsy.
<hr></hr>

## How?
<ul>
<li>Monitor the blinking of eyes of the user</li>
<li>If there is a long delay in blinking then the alarm will alert the user</ul>
</ul>
<hr></hr>

## Technologies Used

<ul>
<li>OpenCV for video capturing</li>
<li>Dlib for face recognition library for computing eye aspect ratio</li>
<li>Python as a coding language</li>
<li>Sqlite3 for database</li>
</ul>
<hr></hr>

## Methodology

we have the eye regions, we can compute the eye aspect ratio to determine if the eyes are closed:
The eye aspect ratio is instead a much more elegant solution that involves a very simple calculation based on the ratio of distances between facial landmarks of the eyes.
Now we check if the aspect ratio value is less than 0.25 (0.25 was chosen as a base case after some tests). If it is less an alarm is	 	 	 	
sounded and user is warned and the data record of that user with timestamp saved in database.
<hr></hr>

## Programming Environment (soft-&Hardware)

### Software requirements

<ul>
<li>Python - pyLibraries,Numpy,Scipy,Playsound,Dlib,Imutils, openCV, etc.</li>
<li>Database - Sqlite3</li>
<li>OPERATING SYSTEM - Windows or Ubuntu</li>
</ul>

### Hardware Requirements Specification 
 <li>Laptop with basic hardware.,Webcam</li>
 <hr></hr>
 
 

