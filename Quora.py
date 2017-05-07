import requests
from bs4 import BeautifulSoup


class ScrapeQuora:
    def __init__(self, username):
        self.username = username
        self.feed_count = self.count(username)
        self.links = self.links(username)

    @staticmethod
    def links(username):
        """
        Uses the feed div to find links to :
        1. Answers
        2. Questions
        3. Activity
        4. Posts
        5. Followers
        6. Following
        7. Edits

        (div soup) -> dict(links)
        """

        url = "https://www.quora.com/profile/{}".format(username)
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find('div', {'class': 'EditableList NavList ProfileNavList'})

        url_list = []

        for url in div.find_all('a'):
            url_list.append("https://www.quora.com{}".format(url.get('href')))

        links = {
            'answers': url_list[0],
            'questions': url_list[1],
            'activity': url_list[2],
            'posts': url_list[3],
            # 'blogs': url_list[4],
            'followers': url_list[5],
            'following': url_list[6],
            # 'topics': url_list[7],
            'edits': url_list[8]
        }

        return links

    @staticmethod
    def count(username):
        """
        Returns count of :
        answers, questions, posts, followers,etc

        (div soup) -> dict(user data)
        """

        url = "https://www.quora.com/profile/{}".format(username)
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find('div', {'class': 'EditableList NavList ProfileNavList'})

        count_list = []

        for link in div.find_all('a'):
            count = link.find('span', {'class': 'list_count'})

            if count is not None:
                count_list.append(count.get_text())

        counts = {
            'answers': count_list[0],
            'questions': count_list[1],
            'posts': count_list[2],
            # 'blogs': count_list[3],
            'followers': count_list[4],
            'following': count_list[5],
            # 'topics': count_list[6],
            'edits': count_list[7]
        }

        return counts

    def questions(self):
        """
        Returns the recent questions asked by a user and their links.

        (div soup) -> list(questions), list(questions_links)
        """

        url = self.links['questions']

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        div_questions = soup.find_all('span', {'class': 'question_text'})
        div_links = soup.find_all('a', {'class': 'question_link'})

        recent_questions = []
        questions_links = []

        for question in div_questions:
            recent_questions.append(question.get_text())

        for link in div_links:
            questions_links.append("https://www.quora.com{}".format(link.get('href')))

        questions = {
            'page': url,
            'count': self.feed_count['questions'],
            'recent': recent_questions,
            'url': questions_links,
        }

        return questions

    def posts(self):
        """
        Returns the recent questions answered by as user and their links.

        (div soup) -> list(questions), list(questions_links)
        """

        url = self.links['posts']

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        div_posts = soup.find_all('span', {'class': 'rendered_qtext'})
        a_links = soup.find_all('a', {'class': 'BoardItemTitle'})
        span_upvotes = soup.find_all('div', {'class': 'ActionBar Post'})
        # TODO: Find a way to get upvotes


        recent_posts = []
        posts_links = []
        post_upvotes = []
        # TODO: Find a way to get upvotes

        for link in a_links:
            posts_links.append(link.get('href'))
            p_text = link.find('p', {'class': 'qtext_para'})
            recent_posts.append(p_text.get_text())

        posts = {
            'page': url,
            'count': self.feed_count['posts'],
            'recent': recent_posts,
            'url': posts_links,
            'upvotes': post_upvotes,
            # TODO: Find a way to get upvotes
        }

        return posts

    def answers(self):
        """
        Returns the recent questions answered by as user and their links.

        (div soup) -> list(questions), list(questions_links)
        """

        url = self.links['answers']

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        div_questions = soup.find_all('span', {'class': 'question_text'})
        a_links = soup.find_all('a', {'class': 'question_link'})
        span_upvotes = soup.find_all('div', {'class': 'Answer ActionBar'})
        # TODO: Find a way to get upvotes

        recent_answers = []
        answers_links = []
        answer_upvotes = []

        for question in div_questions:
            recent_answers.append(question.get_text())

        for link in a_links:
            answers_links.append("https://www.quora.com{}/answer/{}" .format(link.get('href'), self.username))

        answers = {
            'page': url,
            'count': self.feed_count['answers'],
            'recent': recent_answers,
            'url': answers_links,
            'upvotes': answer_upvotes,
            # TODO: Find a way to get upvotes
        }

        return answers

    def followers(self):

        # TODO: Find a way to get recent followers
        followers = {
            'url': self.links['followers'],
            'count': self.feed_count['followers']
        }

        return followers

    def following(self):

        # TODO: Find a way to get recent users followed
        following = {
            'url': self.links['following'],
            'count': self.feed_count['following']
        }

        return following
