import sys

from post_page_parser import PostPageParser
from post_handler import PostHandler

if __name__ == '__main__':
    post_id = sys.argv[1]

    post_page_parser = PostPageParser()
    post_handler = PostHandler(post_id=post_id,
                               post_page_parser=post_page_parser)

    print(post_handler.fetch_post())
