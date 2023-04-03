# insfetch
A simple and lightweight Instagram post fetcher written in pure Python

TODO:
	- Organize files in python modules;
	- Break down "timeline media" and "related profiles" on profile handler;
	- Separate data for `post_handler` using classes;
	- Separate data for `profile_handler` using classes;
	- Refactor both post and profile handlers to get data using `__getattr__` (functions will be gone and a properties dictionary will be created)
	- Write argument parser;
	- Write README
		- Explain how profile fetch works (unnoficial api, etc);
		- Explain how post fetch works (html parsing, etc);
		- Explain why this script can be unreliable and stop working at any given moment;
		- Write warning about IP ban on profile fetch;
		- Write about how to use the app
