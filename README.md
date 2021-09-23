acid-crawl
==========

An acid test suite for web archives.

The idea would be to run a workflow along these lines:

* Spin up a Python server with test files and behaviour.
    * Big files, little files, embeds, [javascript tests][4], dodgy server behaviour, etc. etc.
* Spin up a [warcprox][3] proxy to record what happens.
* Unpack and configure Heritrix3 with a sample job configuration that tests all modules of interest.
* Start up Heritrix (via it's API) and get it crawling the test site.
* Perform various standard operations, like pausing and checkpointing, resuming from a checkpoint etc.
* At the end, check the logs are sane, check the output has what is expected in it.
* Use the warcprox recordings to cross-check the WARC contents from Heritrix3.

This repo is intended to provide docker images containing servers that 
deliver the test resources, and the expected results. The testing processes 
will be elsewhere (for now at least).


Cases
-----

* Normal GETs, 200s, redirects, etc.
* Byte-range requests:
    * Presumably we should grab the whole thing in this case?
    * See [this related OpenWayback issue](https://github.com/iipc/openwayback/pull/263)
* 206 Partial Content
    * See [this example](https://github.com/ikreymer/pywb/issues/144)


Components
----------

### acid-simple-resources

This is a simple Java web application that serves simple static resources of various kinds.


### acid-crawl-selftest

This is a simple test system that shows how to file up the test server and request resources.




Simulating Bad Servers
----------------------

Some work done on the idea of simulating a very badly behaved server.

Original idea was to proxy some requests to [cynic][1] in order to test crawler behaviour under bad server behaviour.
Unfortunately, cynic depends on select.poll() functionality that does not work under OS X. Cynic uses watched files 
to implement the server sockets, spawning child processes per request, and so it is difficult to disentangle things.

    pip install bottle cynic wsgiproxy

Alternatively, the [hamms][2] package offers similar functionality and may be simpler to use.

[1]: https://github.com/rspivak/cynic
[2]: https://github.com/kevinburke/hamms
[3]: https://github.com/internetarchive/warcprox
[4]: http://acid.matkelly.com/

