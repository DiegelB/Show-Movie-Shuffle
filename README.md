# Show-Movie-Shuffle
This program allows you to shuffle either your tv shows or movies. 
You are also able to pick how many times you would like it to loop. 

REQUIREMENTS:
- VLC
- File naming convention for movies: /home/'user'/Ent/Movies

- File naming convention for TV shows: /home/'user'/Ent/TvShows/Season#

  *** IN YOUR TvShows FOLDER MAKE SURE YOU HAVE A FOLDER CALLED "Singles" 
  *** THAT IS FOR SINGLE SHOWS WITHOUT SEASONS.
  
THE PROGRAMS:
- W2W.py:
  - This is the program that will ask you if you want a random movie or tv show
     once the option is chosen it will ask if you want to watch the chosen show/movie.
  - Once you hit 'y' for yes, the chosen show/movie will start running through VLC and 
     go into full screen.
  - When the show or movie is finished VLC closed and the program ends.
  
- loopShow.py
  - This program asks you how many times to loop tv shows.
  - Once the number (x) is chosen, it will play (x) amount of Tv-shows back to back
     this is played in VLC and opens full screen.
  - Once the first show finished, VLC exits and then reopens playing the next item.
  
I recommend adding these programs to your /bin folder to run anytime! 

First enter: chmod +x W2W.py
Then: cp W2W.py /bin

After that you can type 'W2W.py" from any directory and it will play your shows/movies!
enjoy!
