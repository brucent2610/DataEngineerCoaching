#Normal Run Script
- Run 2 kind of command lines
- More than 1 hours to run and collect missing data

#Normal Run Script (Parallel)
- Run 1 command lines finish all crawl data
- Separate smaller to run
- About 20 mins to finish

#Plan to improve more
- To prevent for rate limitation in server, can use change proxies or implement VM to using different IP to connect the website
- Using VM in Cloud: Build a VM by command line, add startup script to install and run command line, finish will remove the VM
- Building docker images, using Container Docker to run, finish stop the container
- Using Kubernetes in Cloud: run docker images in Cronjob Services, stop services when run finish

#Note:
- [Scrapy Proxies – Rotating IP addresses](https://coderslegacy.com/python/scrapy-rotating-proxies/)
- [Concurrent Requests](https://coderslegacy.com/python/concurrent-requests-in-scrapy/)