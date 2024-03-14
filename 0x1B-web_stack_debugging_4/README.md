0x1B-web_stack_debugging_4

This repository tackles a web stack debugging scenario where a server running Nginx is experiencing a high volume of failed requests.

The Problem
We identified performance issues with our Nginx server setup using ApacheBench for benchmarking. The initial test resulted in:

2000 requests simulated
100 concurrent requests at a time
943 failed requests (almost half!)
Fixing the Web Stack
The provided Puppet script (0-the_sky_is_the_limit_not.pp) addresses the bottlenecks and improves server performance.
