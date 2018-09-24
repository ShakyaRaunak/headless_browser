## Headless Chrome and Python
**The Dark Ages**

Prior to the release of Headless Chrome, any time that you did any automated driving of 
Chrome that potentially involved several windows or tabs, you had to worry about the CPU 
and/or memory usage. Both are associated with having to display the browser with the 
rendered graphics from the URL that was requested.
When using a headless browser, we don’t have to worry about that. As a result, we can 
expect lower memory overhead and faster execution for the scripts that we write.

Headless browsers are web browsers without a graphical user interface (GUI) and 
are usually controlled programmatically or via a command-line interface. One of 
the many use cases for headless browsers is automating usability testing or testing 
browser interactions. If you’re trying to check how a page may render in a different 
browser or confirm that page elements are present after a user initiates a certain 
workflow, using a headless browser can provide a lot of assistance.
In addition to this, traditional web-oriented tasks like web scraping can be difficult 
to do if the content is rendered dynamically (say, via Javascript). Using a headless 
browser allows easy access to this content because the content is rendered exactly as 
it would be in a full browser.


    $ chrome --headless --disable-gpu --remote-debugging-port=9222 https://www.chromestatus.com


Navigate to [http://localhost:9222/](http://localhost:9222/)


Install the below package.

    $ pip install Scrapy
    
    $ npm i --save puppeteer

    $ pip install selenium
