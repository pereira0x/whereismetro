![made-with-python](https://img.shields.io/badge/Made%20with-Python3-brightgreen)

<!-- LOGO -->
<br />
<h1>
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Metropolitano_Lisboa_logo.svg/1200px-Metropolitano_Lisboa_logo.svg.png" alt="Logo" width="140" height="110">
  <br>whereismetro
</h1>
  <p align="center">
    Tracking the arrival times of the Lisbon Metro at each station.
    <br />
    </p>
</p>
<p align="center">
  <a href="#about-the-project">About The Project</a> •
  <a href="#usage">How To Use</a> •
  <a href="#examples">Examples</a> •
  <a href="#to-do">To Do</a> •
</p>  

<p align="center">
  
![screenshot](img/clip.gif)
</p>                                                                                                                             
                                                                                                                                                      
## About The Project
Whereismetro is a Django App for tracking real time arrivals of the Lisbon Metro. Currently has it's basic functionality, allowing the user to check all the stations of each line. Next steps on my plans are making the website look good and responsive, make sure it is accessible to all.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/pearsettings44/whereismetro
   ```
2. Install requirements
   ```sh
   pip install -r requirements.txt
   ```
3. Get yourself an API Key from https://api.metrolisboa.pt/store and store it in the .env file
   ```sh
   on your .env file:
   API_KEY='paste here your key'
   ```
4. Deploy the app (default will be on http://127.0.0.1:8000/)
   ```sh
   python manage.py runserver
   ```

## Usage
```sh
http://127.0.0.1:8000/verde/    ----> Green line

http://127.0.0.1:8000/azul/     ----> Blue line

http://127.0.0.1:8000/vermelha/ ----> Red line

http://127.0.0.1:8000/amarela/  ----> Yellow line
```


## Examples
![alt text](https://github.com/pearsettings44/whereismetro/blob/main/amarela.png?raw=true)
<p align="center">Yellow line page.</p>

![alt text](https://github.com/pearsettings44/whereismetro/blob/main/verde.png?raw=true)
<p align="center">Green line page.</p>


## To Do
List of things that are still to be developed:
- Make the arrivals time update every X seconds instead of needing to reload the page.
- Make the website look more modern, pretty, responsive and accessible.
- Expand it to also cover some info about CP trains.