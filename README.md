# Google automation lab
The final project in coursera specialization "Google IT automation with Python"

## Task
You'll first need to get the information from the supplier that is currently stored in a Google Drive file. The supplier has sent data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description).

The subdirectory _images_ contain images of various fruits, while the _descriptions_ subdirectory has text files containing the description of each fruit. 

In this section, you will write a Python script named **_changeImage.py_** to process the supplier images. You will be using the PIL library to update all images within _~/supplier-data/images_ directory to the following specifications:
* Size: Change image resolution from 3000x2000 to 600x400 pixel
* Format: Change image format from .TIFF to .JPEG

### Uploading images to web server
You have modified the fruit images through **_changeImage.py_** script. Now, you will have to upload these modified images to the web server that is handling the fruit catalog. To do that, you'll have to use the Python requests module to send the file contents to the _[linux-instance-IP-Address]/upload_ URL.

### Uploading the descriptions
The Django server is already set up to show the fruit catalog for your company.
Write a Python script named **_run.py_** to process the text files (001.txt, 003.txt ...) from the _supplier-data/descriptions_ directory.

The script should turn the data into a JSON dictionary by adding all the required fields, including the image associated with the fruit (image_name), and uploading it to _http://[linux-instance-external-IP]/fruits_ using the Python requests library.

### Generate a PDF report and send it through email
Once the _images_ and _descriptions_ have been uploaded to the fruit store web-server, you will have to generate a PDF file to send to the supplier, indicating that the data was correctly processed. To generate PDF reports, you can use the _ReportLab_ library. The content of the report should look like this:

Processed Update on <Today's date>

name: Apple

weight: 500 lbs

name: Avocado

weight: 200 lbs

...

### Send report through email
Once the PDF is generated, you need to send the email.

Create **_emails.py_** Define _generate_email_ and _send_email_ methods by importing necessary libraries.
Use the following details to pass the parameters to _emails.generate_email()_:

*	**From**: automation@example.com
*	**To**: username@example.com
*	Replace _username_ with the _username_ given in the Connection Details Panel on the right hand side.
*	**Subject line**: Upload Completed - Online Fruit Store
*	**E-mail Body**: All fruits are uploaded to our website successfully. A detailed list is attached to this email.
*	**Attachment**: Attach the path to the file processed.pdf

Now, check the webmail by visiting _[linux-instance-external-IP]/webmail_. Here, you'll need a login to **roundcube** using the username and password mentioned in the Connection Details Panel on the left hand side, followed by clicking **Login**.

Now you should be able to see your inbox, with one unread email. Open the mail by double clicking on it. There should be a report in PDF format attached to the mail. View the report by opening it.

### Health check
This is the last part of the lab, where you will have to write a Python script named **_health_check.py_** that will run in the background monitoring some of your system statistics: CPU usage, disk space, available memory and name resolution. Moreover, this Python script should send an email if there are problems, such as:
*	Report an error if CPU usage is over 80%
*	Report an error if available disk space is lower than 20%
*	Report an error if available memory is less than 500MB
*	Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1"

Complete the script to check the system statistics every 60 seconds, and in event of any issues detected among the ones mentioned above, an email should be sent.
To test out your script, you can install the _stress_ tool.

Use crontab to launch it every minute in background.
