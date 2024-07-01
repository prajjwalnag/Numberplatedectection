# Number Plate Detection 
## Background
As a biker navigating the chaotic streets of India, I’ve faced countless challenges that often left me feeling frustrated and vulnerable. There were days when reckless drivers would zoom past me, ignoring traffic signals and putting everyone at risk. I remember a particularly harrowing incident where a car ran a red light, barely missing me by inches. The fear and helplessness I felt in that moment made me acutely aware of the dire need for better traffic management and safety measures in our country.
![Indian Biker Navigating Chaotic Streets](images/A_cartoonish_scene_depicting_an_Indian_biker_navig.jpg)

These personal experiences have shown me how crucial it is to have an efficient system for detecting number plates. Here’s why:

**Traffic Violations**:  Efficient number plate detection helps identify and penalize vehicles involved in speeding, signal jumping, and other traffic violations, ensuring that offenders are held accountable and deterring future violations.

**Congestion Management**: By tracking vehicle movements, authorities can better manage traffic flow and reduce congestion in busy areas, making daily commutes smoother and less stressful for everyone.

**Stolen Vehicle Recovery:** Quick detection and identification of stolen vehicles become possible, aiding law enforcement in recovering them swiftly and reducing the financial and emotional burden on victims.
Parking Enforcement: Illegal parking can be curbed, freeing up space and maintaining order on crowded streets, which is especially important in densely populated areas.

**Accident Investigation**: In case of accidents, number plate detection provides crucial information for investigations, helping determine fault and speeding up legal processes, offering justice and closure to those affected.

**Enhanced Security**: Monitoring suspicious vehicles and tracking their movements can help prevent and respond to potential security threats, contributing to a safer community.

These daily encounters with the chaos and dangers of Indian traffic have motivated me to work on a project focused on efficient number plate detection. I am determined to contribute to a safer and more orderly traffic system, hoping to make a real difference in the lives of fellow commuters and ensure that the roads we travel are secure and well-regulated.

## System Design 
![Indian Biker Navigating Chaotic Streets](images/Flowchart.png)

### Image Collection 
We collected all images from google images , we only wanted images of cars in Indian roads. To scrap the data we used 
simple image downloaded which is python package to download images, using google images search. We tested with alot of different keywords to find the extact type of images that we wanted for the project. Once we have the list of the keyword that suits our need we us the "downloadimages.py" script to download all the images. 

### Preprocessing
 Not all the images will be good for train and fight have duplicated data along the way, whcih needs to be removed before traing the data. 

### Labeling images 
 The important step in objec t recognition is to label the Area of Interesting using a Labeling tool. When we started the project we used Labelstudio for labeling the images , so that we can train the Yolo V7 model on the labeled images. 

 The idea was later discarded and roboflow platform was used as its API allow direct intregration in Jupyter Notebook to train YOLO V8 model. 

 ![Roboflow Dataset](images/Dataset.pnmg.PNG)
  The Dataset was created with 86 Images which was 
 ![Roboflow Dataset](images/testtrain.PNG)

 ### Training the model 
 The dataset was imported in a google collab and trained in Yolo V8 model using a GPU.
 *Tip* Free GPU can get exhuasted so train and save the model and then use CPU to do the infernces locally.

 ### Running the model locally 
 Once the model is trained and working, the model is saved and used locally to compute the inferences. The model could easily detect the number plate with an accuracy of 98.8% . 
 ![NumberPlate](images/8.JPG)
  
### Croping the Area of Interest 
Once the number plate is detected, the numberplate is then croped and saved in cropped image directory.

![CroppedImage](images/numberplate.png)
 
### Preprocessing for OCR 
We will be using the open source tool tesseract, to extract charecters from the number plate. Teseract works like a chartm with some preprcrocessing so we will incoprate a small preprocessing pipeline. 

![Processed Image](images/processed.PNG)

### Extract information using Tesseract 
Once the images are processed we can use it with tesseract to display the number plate information.

![OCR Results](images/OCR%20result.PNG)

