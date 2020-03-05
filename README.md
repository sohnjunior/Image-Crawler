Google Image Crawler
==============

Installation
-------------
Required package
```
$ pip install selenium
```
> selenium은 webdriver 구동에 필요한 패키지입니다.

<br>
구글 이미지 검색을 위해서 chromedriver가 필요합니다. <br>
이를 위해서 먼저 본인이 사용하고 있는 크롬 버전을 확인해야 합니다. <br> <br>

[크롬 버전 확인하는 방법](https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DDesktop&hl=ko)

[chromedriver 설치](https://sites.google.com/a/chromium.org/chromedriver/home)

이후 설치된 chromedriver를 main.py와 crawler.py와 같은 디렉토리에 위치시킵니다.

Usage
------
Execute program

```
$ python main.py
keyword... : <keyword for image>
```

실행시키면 터미널에 원하는 키워드를 입력합니다.
이후 chromedriver를 통해 이미지를 검색한 후 파일 형태로 저장합니다.