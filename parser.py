from html.parser import HTMLParser
from collections import namedtuple


Tag = namedtuple('Tag', 'data tag')


class POSParser(HTMLParser):
    """
    Parser to parse the pos file got from nltk.
    Data is linearised.
    """

    def __init__(self):
        super().__init__()
        self._reset_ds()

    def _reset_ds(self):
        self.data = []
        self.level = 0
        self.tag_history = []
    
    def handle_starttag(self, tag, attrs):
        self.tag_history.append(tag)
        self.level += 1

    def handle_endtag(self, tag):
        self.level -= 1
        if self.level < 0:
            raise ValueError("Error parsing file. Malformed tags.")
        self.tag_history.pop()

    def handle_data(self, data):
        hist = self.tag_history
        if hist and 'sentence' in hist[-1].lower():
            data = data.strip('\n')
            if not data:
                return
            parts = data.split()
            tags = []
            for ele in parts:
                try:
                    word, tag = ele.split('_')
                    tags.append(Tag(word, tag))
                except Exception as e:
                    # invalid sentence / untagged word found
                    raise ValueError("Malformed tags in the given File")
            self.data.append(tags)


    def parse_file(self, file_path):
        # parsing data in the file.
        self._reset_ds()
        with open(file_path) as fh:
            self.feed(fh.read())
        return self.data

