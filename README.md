# Bank-note-Authentication-end-to-end-implementation-with-docker

#### Bank Note Authentication end to end implementation with Docker | Building UI with Flasgger | Deployed with Streamlit | Flask

![money img](https://user-images.githubusercontent.com/80705710/113998505-c2669e00-9876-11eb-82a2-8cc1d3642c96.jpg)

[Dataset available on kaggle from this link.](https://www.kaggle.com/ritesaluja/bank-note-authentication-uci-data)

### About the data
Data were extracted from images that were taken from genuine and forged banknote-like specimens. For digitization, an industrial camera usually used for print inspection was used. The final images have 400x 400 pixels. Due to the object lens and distance to the investigated object gray-scale pictures with a resolution of about 660 dpi were gained. Wavelet Transform tool were used to extract features from images.
The problem statement is quiet simple:
#### Problem statement

as it is described in about the data section, There is a gray scale pictures of notes with a resolution of about 660 dpi.
Wavelet Transform tool were used to extract features from images.we have four features`['Variance', 'skewness', 'curtosis', 'entropy']` and we have to predict wheather Bank Note is authentic or not.

I Have used RandomForestClassifier to predict wheather the note is authetic or not as problem is not that complex,fitted the data and predict with 99% accuracy
and created pickle file to save the model .

The pickle module implements a fundamental, but powerful algorithm for serializing and de-serializing a Python object structure.and additonally pickle is a binary file format

I have used flask to create a Web API

##### Let's dockerize our machine learning Model as REST API using Flask :
1. Create Dockerfile 
    ```
    FROM continuumio/anaconda3:4.4.0     # Creating base image which is created by docker hub
    COPY . /usr/app                      # Cpoying the working directory in root user directory
    EXPOSE 5000                          # Exposing the PORT number
    WORKDIR usr/app                      # Telling the container where is the working directory
    RUN pip install -r requirements.txt  # installing required packages to run 
    CMD python app.py                    # Command to run our app
    ```
    Creat your requirements.txt file by following command
    ```
    pip freeze > requirements.txt
    ```
2. Build docker image
    ```
    docker build -t "<app_name>" . 
    --------------------------------
    Eg: docker build -t money_api .
    ```
3. Run the Docker container after build
    ```
    docker run -p 5000:5000 "<app_name>"    # -p : to make the port available for the browser externally
    ```
4. Check your all running container
    ```
    docker ps   # You can check you container id , status and name et
    ```
    
    If you want to access the ip address for a specific running container
    ```
    docker inspect "<Container_id>"
    ```

    Kill and remove container
    ```
    docker rm "<container_id>" -f
    ```
- OUTPUT of this perticular project Running on Docker container 

    -I have used flasgger for the UI `pip install flasgger`

    ![Flasgger bank note authentication](https://user-images.githubusercontent.com/80705710/114000250-7288d680-9878-11eb-93dd-202c3c3339ea.png)

    
    
### Deploying using Streamlit 

first of all You have to install streamlit in you environment using below command
```
pip install streamlit`
```
then run the flasgger_app.py 
```
streamlit run flasgger_app.py
```
OUTPUT :
![Streamlit Bank note authentication](https://user-images.githubusercontent.com/80705710/114000625-cb586f00-9878-11eb-9c80-268a682fafa2.png)

