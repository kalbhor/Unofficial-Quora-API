import requests
import pprint
from bs4 import BeautifulSoup

class ScrapeQuora:

    def __init__(self, username):
        self.username = username

    def feed_soup(self):
        """
        (username) -> <div> User Feed </div>
        Provides the division with the user info

        Returns a beautifulsoup object
        """

        url = "https://www.quora.com/profile/%s" % (self.username)

        response = requests.get(url)
        
        soup = BeautifulSoup(response.text,'html.parser')
        div = soup.find('div',{'class':'EditableList NavList ProfileNavList'})

        return div
    
    def links(self):
        """
        Uses the feed div to find links to :
        1. Answers
        2. Questions
        3. Activity
        4. Followers
        5. Following
        6. Edits

        (div soup) -> dict(links)
        """

        div = self.feed_soup()
        url_list = []

        for url in div.find_all('a'):
            url_list.append("https://www.quora.com" + url.get('href'))

        links = {
         'answers' : url_list[0],
         'questions' : url_list[1],
         'posts' : url_list[2],
         'activity': url_list[3],
         'followers': url_list[4],
         'following': url_list[5],
         'edits': url_list[6]
         }

        return links

    def count(self):
        """
        Returns user data.

        (div soup) -> dict(user data)
        """

        div = self.feed_soup()
        count_list = []

        for link in div.find_all('a'):
            count = link.find('span', {'class': 'list_count'})

            if count != None:
                count_list.append(count.get_text())

        counts = {
         'answers' : count_list[0],
         'questions' : count_list[1],
         'posts' : count_list[2],
         'followers': count_list[3],
         'following': count_list[4],
         'edits': count_list[5]
         }

        return counts

    def questions(self):
        """
        Returns the recent questions asked by a user and their links.

        (div soup) -> list(questions), list(questions_links) 
        """

        links = self.links()
        url = links['questions']

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        div_questions = soup.find_all('span',{'class' : 'question_text'})
        div_links = soup.find_all('a', {'class' : 'question_link'})

        questions = []
        questions_links = []

        for question in div_questions:
            questions.append(question.get_text())

        for link in div_links:
            questions_links.append("https://www.quora.com" + link.get('href'))

        return questions, questions_links


    def posts(self):
        """
        Returns the recent questions answered by as user and their links.

        (div soup) -> list(questions), list(questions_links)
        """
        links = self.links()
        url = links['answers']

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        div_posts = soup.find_all('span',{'class' : 'rendered_qtext'})
        a_links = soup.find_all('a', {'class' : 'BoardItemTitle'})
        span_upvotes = soup.find_all('div', {'class' : 'Answer ActionBar'}) ####

        posts = []
        posts_links = []
        post_upvotes = []

        for i in range(1,len(div_posts)):
            posts.append(div_posts[i].get_text())

        for link in a_links:
            posts_links.append("https://www.quora.com" + link.get('href'))

        return posts, posts_links, post_upvotes



    def answers(self):
        """
        Returns the recent questions answered by as user and their links.

        (div soup) -> list(questions), list(questions_links)
        """
        links = self.links()
        url = links['answers']

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        div_questions = soup.find_all('span',{'class' : 'question_text'})
        a_links = soup.find_all('a', {'class' : 'question_link'})
        span_upvotes = soup.find_all('div', {'class' : 'Answer ActionBar'}) ####

        answers = []
        answers_links = []
        answer_upvotes = []

        for question in div_questions:
            answers.append(question.get_text())

        for link in a_links:
            answers_links.append("https://www.quora.com" + link.get('href'))

        return answers, answers_links, answer_upvotes


if __name__ == '__main__':

    user = ScrapeQuora('User')
    links = user.links()
    recent_questions, questions_links = user.questions()
    recent_answers, answers_links, answer_upvotes = user.answers()
    recent_posts, posts_links, post_upvotes = user.posts()
    feed_count = user.count()


    questions = {
    'link' : links['questions'],
    'count' : feed_count['questions'],
    'recent' : recent_questions,
    'recentlinks' : questions_links,
    }

    answers = {
    'link' : links['answers'],
    'count' : feed_count['answers'],
    'recent' : recent_answers,
    'recentlinks' : answers_links,
    'upvotes': answers_upvotes, ## Find a way to get upvotes
    }

    followers = {
    'link' : links['followers'],
    'count' : feed_count['followers']
    }

    following = {
    'link' : links['following'],
    'count' : feed_count['following']
    }

    posts = {
    'link' : links['posts'],
    'count' : feed_count['posts'],
    'recent' : recent_posts, ## Needs to be looked upon
    'recentlinks' : posts_links, ## Direct consequence of recent_posts
    'upvotes' : posts_upvotes, ## Find a way to get upvotes 
    }

    pprint.pprint(posts)
