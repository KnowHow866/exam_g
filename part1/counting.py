
class Util():
    @staticmethod
    def extract_filename(url=''):
        filename = (url.split('/')).pop()
        return filename.lower()

if __name__ == '__main__':
    urls = [
        "http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "https://facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png",
    ]

    record = dict()
    for _, url in enumerate(urls):
        filename = Util.extract_filename(url=url)
        if record.get(filename, None) == None: 
            record[filename] = 1
        else: record[filename] += 1

    arr = [filename for filename in record]
    arr.sort(key=lambda i: record[i], reverse=True)
    arr = arr[:3]

    for filename in arr:
        print(f'{filename}: \t{record[filename]}')
