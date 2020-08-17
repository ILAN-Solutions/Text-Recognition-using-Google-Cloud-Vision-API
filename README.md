# A Complete Guide to Text Recognition using Google Cloud Vision API

<p align="center">
  <img src="https://github.com/ILAN-Solutions/Text-Recognition-using-Google-Cloud-Vision-API/blob/master/Images/img0.png">
</p>

Vision AI is a cloud-based service offered by Google. It employs Machine Learning algorithms to analyze images. While users can make use of AutoML Vision to analyze images using custom datasets, in this article,we will be focussing on Vision API, which uses pre-trained ML models to analyze images. Vision API can be used for text recognition, face detection, object detection, etc. We&#39;ll be using the ImageAnnotator Client to extract Text from Images with Python Programming Language.

#### Enabling Vision API and creating Credentials in Google Cloud console

Step 1: Open Google Cloud console

![](https://github.com/ILAN-Solutions/Text-Recognition-using-Google-Cloud-Vision-API/blob/master/Images/img1.png)

Upon Logging into [Google Cloud Console](https://console.cloud.google.com/), you would arrive at a similar screen. Your console acts as a homepage from where you can create projects, monitor your project activities, etc.

Step 2: Create a New Project

![](https://github.com/ILAN-Solutions/Text-Recognition-using-Google-Cloud-Vision-API/blob/master/Images/img2.png)

Click on the &#39;Select a project&#39; drop-down option to show the list of all projects you&#39;ve created. To create a new project, Click on the &#39;New Project&#39; option.

![](https://github.com/ILAN-Solutions/Text-Recognition-using-Google-Cloud-Vision-API/blob/master/Images/img3.png)

Type in your project name and click on the &#39;Create&#39; button to create your first project. For this article, I&#39;ve given the name of the project as &#39;VisionAPI&#39;, but feel free to choose the project name as per your wish.

Once you&#39;ve successfully created your project, click on the &#39;Select a project&#39; drop-down button and click on your project. This would redirect you to a similar page

![](https://github.com/ILAN-Solutions/Text-Recognition-using-Google-Cloud-Vision-API/blob/master/Images/img4.png)

Step 3: Enable Vision API

In the &#39;Search products and resources&#39; box, type &#39;Cloud Vision API&#39;. Click on the &#39;Enable&#39; option.

![](https://github.com/ILAN-Solutions/Text-Recognition-using-Google-Cloud-Vision-API/blob/master/Images/img5.png)

Step 4: Creating Credentials

![](https://github.com/ILAN-Solutions/Text-Recognition-using-Google-Cloud-Vision-API/blob/master/Images/img6.png)

In order to use Vision API, we have to create credentials which inturn would generate a key using which we can send requests to Vision API for processing.

![](https://github.com/ILAN-Solutions/Text-Recognition-using-Google-Cloud-Vision-API/blob/master/Images/img7.png)

Clicking on the &#39;Create Credentials&#39; button would trigger a drop-down option. Click on &#39;Service account&#39; when this happens.

![](https://github.com/ILAN-Solutions/Text-Recognition-using-Google-Cloud-Vision-API/blob/master/Images/img8.png)

Type your choice of &#39;Service account name&#39; and &#39;Service account description&#39; and click on the &#39;Create&#39; button.

![](https://github.com/ILAN-Solutions/Text-Recognition-using-Google-Cloud-Vision-API/blob/master/Images/img9.png)

In this next step, under &#39;Role&#39;, select &#39;Project -\&gt; Owner&#39; to obtain full access to all the resources. Proceed to the next section by clicking on &#39;Continue&#39;. Skip the next step as it is an optional step, and click on the &#39;Done&#39; button to create the credentials.

Step 5: Adding a Key for the service

Under the &#39;Service Accounts&#39; section, click on the name of your project, and that would take you to the next page where-in you can add a Key for the service.

![](https://github.com/ILAN-Solutions/Text-Recognition-using-Google-Cloud-Vision-API/blob/master/Images/img10.png)

![](https://github.com/ILAN-Solutions/Text-Recognition-using-Google-Cloud-Vision-API/blob/master/Images/img11.png)

![](https://github.com/ILAN-Solutions/Text-Recognition-using-Google-Cloud-Vision-API/blob/master/Images/img12.png)

Click on the &#39;Add Key&#39; button, and then on the &#39;Create New Key&#39; button. Choose the format as &#39;JSON&#39;, and click on &#39;Create&#39;.Save the file on your computer. This file is essential when we call the service.

#### Making Call Requests and Performing text recognition using Python language

Step 1: Installing required Python Libraries.

This particular Python code requires the following libraries which might require separate installations :

1. Google Cloud Vision
2. Pandas

To install Google Cloud Vision library, open your Scripts folder inside your Python folder using Command Prompt. 
For ex. `$ cd C:\Python27\Scripts`

And then, type &#39;`$ pip install google-cloud-vision`&#39; to install the library.

Once this installation is completed, install Pandas library using the command &#39;pip install Pandas&#39;.

Step 2: Open the folder containing the Images and the Key file using your Python IDE of choice and Type in the following code: ![](https://github.com/ILAN-Solutions/Text-Recognition-using-Google-Cloud-Vision-API/blob/master/Images/img13.png)

In the line 5 of the code, add the name of your Key file in the &#39;r&quot;(...)&#39; region. For ex., the 5th line of code for my Key file looks like this

![](https://github.com/ILAN-Solutions/Text-Recognition-using-Google-Cloud-Vision-API/blob/master/Images/img14.png)

In the line 9 of the code, choose the path for your Image from which you would want to extract the Text. For ex., the 9th line of my code looks like this

![](https://github.com/ILAN-Solutions/Text-Recognition-using-Google-Cloud-Vision-API/blob/master/Images/img15.png)

Run the code, and You would have successfully extracted the Text from the fed Image.

References :

1. [https://cloud.google.com/vision/docs/ocr](https://cloud.google.com/vision/docs/ocr)
2. [https://cloud.google.com/vision/pricing](https://cloud.google.com/vision/pricing)
