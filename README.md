Google Image Crawler
==============

Installation
-------------
Required package
```
$ pip install -r requirements.txt
```
> tqdm is package for progress bar

<br>
Required web-driver

* [How to check your Chrome version](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=ko)

* [Install chromedriver](https://sites.google.com/a/chromium.org/chromedriver/home)

Google Image Search requires the chromedriver that corresponds to the version of Chrome you are using. <br>
After installing chromedriver, place it in the same directory as crawler.py.

_Dev environment - Chrome : 80.0.3987_

Usage
------
Execute program

```
$ python crawler.py
keyword... : <keyword for image>
```

Enter the desired keyword in the terminal. <br>
Then, the retrieved image is then saved as a file
