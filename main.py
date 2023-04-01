import sys

from post_parser import PostParser
from post import Post

if __name__ == '__main__':
    post_id = sys.argv[1]

    post_parser = PostParser()
    post = Post(post_id=post_id, post_parser=post_parser)

    print(post.fetch_post())
