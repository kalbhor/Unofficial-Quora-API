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
        0. Profile
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
         'profile' : url_list[0],
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
         'profile' : count_list[0],
         'questions' : count_list[1],
         'posts' : count_list[2],
         'followers': count_list[3],
         'following': count_list[4],
         'edits': count_list[5]
         }

        return counts

    def questions(self):
        """
        Returns the recent questions asked by a user.

        (div soup) -> list(questions) 
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
	

if __name__ == '__main__':

    user = ScrapeQuora('')
    links = user.links()
    recent_questions, questions_links = user.questions()
    feed_count = user.count()


    questions = {
    'link' : links['questions'],
    'count' : feed_count['questions'],
    'recent' : recent_questions,
    'recentlinks' : questions_links,
    }

    pprint.pprint(questions)
