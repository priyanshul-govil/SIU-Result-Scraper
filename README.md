# SIU Result Scraper
Scrape [SIU result page](https://www.examination.siu.edu.in/examination/result.html) for results of your entire batch. All you need is the list of **PRNs** for which you want to find the result, and a range of possible **Seat Numbers**. The script will then do its magic, and store all results in a directory `./result` in the form of `PNG` images. However, the script isn't pure magic, so wait for SIU to release the result before you start cursing the develepor.


## DISCLAIMER
This project was made for educational purposes only.

Scraping the web might be considered illegal in some cases. All I ask is that you use this script responsibly, ethically, and at your own risk!

If you're from the SIU Administration and feel that this script violates any institutional policy, please contact me and I'll be happy to remove it.


## DEPENDENCIES

```
$ pip install Selenium
```

```
$ pip install Pillow
```


## USAGE

Clone this repository to your local machine. Navigate to the root directory.

Inside `script.py`, there are two places at the start of the file marked `# MAKE CHANGES HERE`. Go ahead and make the following changes:
    
1. Change values of `start_prn` and `end_prn`. The script will work to capture results of this range of PRNs.
    
2. Change values of `start_seat_num` and `end_seat_num` such that the range `[start_seat_num, end_seat_num]` contains the seat numbers for each required PRN. Take a good logical guess and choose a wide range of seat numbers. It won't matter as long as its reasonable (or if you've got a supercomputer!).

That's it. Run it now! What are you even waiting for?



## SCOPE

Further improvements in mind are storing results in form of a `CSV` for further analysis, and creating a front-end for mass usability. Contact me if you want to contribute.
