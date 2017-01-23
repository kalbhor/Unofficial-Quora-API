# Unofficial Quora API

[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)](LICENSE)

> An Unofficial REST API for [Quora](https://quora.com) 

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Endpoints](#endpoints)
  - [/{user}](#user)
  - [/{user}/questions](#userquestions)
  - [/{user}/answers](#useranswers)
  - [/{user}/posts](#userposts)
  - [/{user}/followers](#userfollowers)
  - [/{user}/following](#userfollowing)
- [Contribute](#contribute)
- [License](#license)


## Installation

### Source
```sh
$ git clone https://github.com/lakshaykalbhor/Unofficial-Quora-API
$ cd Unofficial-Quora-API
$ pip install -r requirements.txt 
```

## Usage

```sh
$ python server.py 
```

## Endpoints

### /{user}

> Gets user information and urls related to user.

#### GET /Lakshay-Kalbhor 

```
{
  "count": {
    "answers": "13", 
    "edits": "224", 
    "followers": "70", 
    "following": "112", 
    "posts": "0", 
    "questions": "17"
  }, 
  "url": {
    "activity": "https://www.quora.com/profile/Lakshay-Kalbhor/activity", 
    "answers": "https://www.quora.com/profile/Lakshay-Kalbhor", 
    "edits": "https://www.quora.com/profile/Lakshay-Kalbhor/log", 
    "followers": "https://www.quora.com/profile/Lakshay-Kalbhor/followers", 
    "following": "https://www.quora.com/profile/Lakshay-Kalbhor/following", 
    "posts": "https://www.quora.com/profile/Lakshay-Kalbhor/all_posts", 
    "questions": "https://www.quora.com/profile/Lakshay-Kalbhor/questions"
  }
}
```

### /{user}/questions

> Gets recent questions asked by user and their urls.

#### GET /Lakshay-Kalbhor/questions 

```
{
  "count": "17", 
  "page": "https://www.quora.com/profile/Lakshay-Kalbhor/questions", 
  "recent": [
    "How do North Koreans participate in online coding competitions?", 
    "How do I use CLRS to practice problems on SPOJ/Codeforces?", 
    "How should I learn to play the ukulele if I'm left handed?"
  ], 
  "url": [
    "https://www.quora.com/unanswered/How-do-North-Koreans-participate-in-online-coding-competitions", 
    "https://www.quora.com/How-do-I-use-CLRS-to-practice-problems-on-SPOJ-Codeforces", 
    "https://www.quora.com/How-should-I-learn-to-play-the-ukulele-if-Im-left-handed"
  ]
}
```

### /{user}/answers

> Gets recent answers by user and their urls.

#### GET /Lakshay-Kalbhor/answers 

```
{
  "count": "13", 
  "page": "https://www.quora.com/profile/Lakshay-Kalbhor", 
  "recent": [
    "What are the pros and cons of living in your city?", 
    "How should I begin learning Python?", 
    "Can I run selenium in background?", 
    "What are the best Python scripts you've ever written?", 
    "How do I scrape Flipkart or Amazon product reviews using code/API?"
  ], 
  "upvotes": [], 
  "url": [
    "https://www.quora.com/What-are-the-pros-and-cons-of-living-in-your-city",  
    "https://www.quora.com/How-should-I-begin-learning-Python?no_redirect=1", 
    "https://www.quora.com/Can-I-run-selenium-in-background", 
    "https://www.quora.com/What-are-the-best-Python-scripts-youve-ever-written", 
    "https://www.quora.com/How-do-I-scrape-Flipkart-or-Amazon-product-reviews-using-code-API"
  ]
}
```

### /{user}/posts

> Gets recent blog posts by users and their urls.

#### GET /Lakshay-Kalbhor/posts 

```
{
  "count": "0", 
  "page": "https://www.quora.com/profile/Lakshay-Kalbhor/all_posts", 
  "recent": [], 
  "upvotes": [], 
  "url": []
}
```

### /{user}/followers

> Gets information on the user's followers.

#### GET /Lakshay-Kalbhor/followers 

```
{
  "count": "70", 
  "url": "https://www.quora.com/profile/Lakshay-Kalbhor/followers"
}
```

### /{user}/following

> Gets information on the user's followed by the user.

#### GET /Lakshay-Kalbhor/follwing 

```
{
  "count": "112", 
  "url": "https://www.quora.com/profile/Lakshay-Kalbhor/following"
}
```

## Contribute

Found an issue? Post it in the [issue tracker](https://github.com/lakshaykalbhor/Unofficial-Quora-API/issues). <br> 
Want to add another awesome feature? [Fork](https://github.com/lakshaykalbhor/Unofficial-Quora-API/fork) this repository and add your feature, then send a pull request.

## License
The MIT License (MIT)
Copyright (c) 2017 Lakshay Kalbhor

