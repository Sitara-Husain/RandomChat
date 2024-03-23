# RandomChat

### Prerequisite:

    * Python 3.12
    * Postgress 15.2
    

### System Setup:

1. Environment setup:

    * Install pip and virtualenv:
        - sudo apt-get install python3-pip
        - pip install --upgrade pip
        - sudo pip3 install virtualenv or sudo pip install virtualenv

   * Create virtual environment:
       - virtualenv venv
         OPTIONAL:- In case finding difficulty in creating virtual environment by
                     above command , you can use the following commands too.
    
               *   Create virtualenv using Python3:-
                       - virtualenv -p python3.12 venv
       - Activate environment:
           - source venv/bin/activate
      
   * Clone project:

             ```
               https://github.com/Sitara-Husain/RandomChat.git
             ```

       - Checkout to branch
     
           ```
             git checkout dev_db
           ```
    
   * Install the requirements(according to server) by using command:
       - cd RandomChat/

       ```
         pip3 install -r requirements.txt
       ```
        
2. Database Setup:

        ```
         DATABASES = {
          'default': {
              'ENGINE': '*******',
              'NAME': '*********',
              'USER': '*********',
              'PASSWORD': '*****',
              'HOST': '*********',
              'PORT': '*********',
          }
         }
        ```

3. Run migrations:

    ```
     $ python manage.py migrate
    ```

4. Run servers:

    ```
     $ python manage.py runserver
    ```
   
5. Load fixtures:
    
    ```
     $ python manage.py loaddata fixtures/sentence_corpus.json
    ```
