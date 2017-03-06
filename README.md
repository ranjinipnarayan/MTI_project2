# Twitter Projector

We built at projector that is dependent on a twitter stream. We tracked certain key words ('trump immigration, trump women, trump security') and depending on the result, we projected a different slide on to a white screen. We staggered the speed of movement by using some sentiment analysis -- only if the tweet was negative enough did we move the servo with the slides on it. 

**Building the projector** 
1. Create an app on Twitter and generate the necessary access tokens and keys
2. Clone the Arduino repository 
3. Run the following commands
  ~~~~
  sudo apt-get install python-pip 
  sudo pip install twython 
  sudo pip install twython --updgrade 
  ~~~~
4. Download the servo+twitter.py file and put in your access tokens 
5. Attach the servo hat to your raspberry pi and plug the servo in to the first pins 
6. Run the code using 
  ~~~~
  sudo python servo+twitter.py 
  ~~~~
7. Download the DXF file, laser cut it out of wood and assemble it. 
8. Put the system together and run it. 

**Troubleshooting** 
If you are getting at Error 401 when trying to stream twitter, run the following command: 
sudo ntpd -q
