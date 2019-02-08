
import sys
import os
from twitter_analysis import *


user = sys.argv[1]
words = sys.argv[2]

location = str(searchUserTweets(user,words)['location'])

followers_count = str(searchUserTweets(user,words)['followers_count'])

friends_count = str(searchUserTweets(user,words)['friends_count'])

created_at = str(searchUserTweets(user,words)['created_at'])

link = str(searchUserTweets(user,words)['link'])

full_tweets = str(searchUserTweets(user,words)['full_tweets'])


print"""
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" type="text/css" href="css/header.css"></head>

<body>
  <div class="topnav">
    <a href="index.html">Home</a>
    <a href="contact.html">Contact me</a>
    <a href="/twitter"> Twitter analysis</a>
    <a class="active" href="about.html">Project-Description</a>
  </div>
</div>
<div style="padding-left:20px">

</div>
</body>

</head>

    </body>
</html>
"""

print """
<table class="TwitterRes">
<thead>
<tr>
<center>
<th><h1>Cyberbullying Detection</h1> </th>
</center>
</tr>
</thead>

"""

print("<tr><td><p>location: " +location + " </p></td></tr>")
print("<tr><td><p>followers_count: " +followers_count + " </p></td></tr>")
print("<tr><td><p>tweets_at: " +created_at + "</p> </td></tr>")
print("<tr><td><p>full_tweets: " +full_tweets + "</p> </td></tr>")
print("<tr><td><p>linke: " +link + "</p> </td></tr>")

print"""

</tbody>
</tr>
</table>
"""























