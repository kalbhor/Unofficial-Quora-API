import requests
import pprint
from bs4 import BeautifulSoup

class User:
    def __init__(self, username):
        self.username = username
    
    def user_links(self):
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
            url_list.append("https://quora.com" + url.get('href'))

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

    def user_questions(self):
        """
        
        """

        links = self.user_links()
        url = links['questions']

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find_all('span',{'class' : 'question_text'})

        questions = []

        for question in div:
            questions.append(question.get_text())

        return questions

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





	

if __name__ == '__main__':
    quora = User('')
    quora.user_questions()
