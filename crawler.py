
import traceback, datetime, re
import requests
from bs4 import BeautifulSoup

class Article():
    ''' Article Model '''
    FIELDS = dict(
        datetime=datetime.datetime,
        author=str,
        title=str,
        content=str,
        board=str
    )

    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
            # todo: check datatype
    
    def serialize(self):
        tmp = dict()
        for key in kwargs: tmp[key] = getattr(self, key)
        return tmp

class BBSSimpleCrawler():
    SITE = 'https://www.ptt.cc'
    INDEX = f'{SITE}/bbs/index.html'

    def __init__(self, board=None):
        self.__selected_board = board.lower()
        self.__board_url = None

    def enter_adult_board(self):
        ''' Code here to help to get into adult board'''
        pass

    def run(self):
        data = requests.get(self.INDEX)
        soup = BeautifulSoup(data.text.lower(), 'html.parser')
        board_list = soup.find('div', class_='b-list-container')
        
        # set board url
        board_name_div = board_list.find('div', string=self.__selected_board)
        board_link = (board_name_div.find_parents("a")).pop()
        self.__board_url = board_link.attrs['href']

        # find articles and save
        # only get the first page
        board_page = requests.post(f'{self.SITE}{self.__board_url}', dict(yes='yes'))
        board_page_soup = BeautifulSoup(board_page.text, 'html.parser')
        if board_page_soup is None: 
            board_page_soup = self.enter_adult_board()

        article_list = board_page_soup.find('div', class_='r-list-container')
        article_links = article_list.find_all('a')
        self.article_links = [a.attrs['href'] for a in article_links]
        self.article_links = [
            # this code still fail to parse url which exclude search
            url for url in filter(lambda url: False if re.match('search', url.replace('/', '')) else True, self.article_links)
        ]
        print(self.article_links)

if __name__ == '__main__':
    BOARD_TO_SEARCH = 'NBA'

    try:
        crawler = BBSSimpleCrawler(board=BOARD_TO_SEARCH)
        crawler.run()
    except Exception as e:
        traceback.print_exc()

    