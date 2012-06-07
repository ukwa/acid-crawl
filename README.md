acid-crawl
==========

An acid test suite for crawlers.


pip install bottle cynic wsgiproxy

Original idea was to proxy some requests to [cynic][1] in order to test crawler behaviour under bad server behaviour.
Unfortunately, cynic depends on select.poll() functionality that does not work under OS X. Cynic usese watched files 
to implement the server sockets, spawning child processes per request, and so it is difficult to disentangle things.

  [1]: https://github.com/rspivak/cynic

