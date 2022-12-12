# MyBlog

#### Video Demo:  https://www.youtube.com/watch?v=r8cbJpA9-bQ&ab_channel=OmarHamid

## _Description_:
This project is a blog application where user can read posts and create their own.Also users can attach an image to their post.

## _MyBlog_
On the main page there are posts in order from new to old.Each post has a **Title**, **Body**, **Date** and **Author**.**Images** are optional.Image's size is depending on its dimensions in order to make post better looking.  
If user is logged in - they can delete their post by clicking on a **Delete** button which is located at the bottom of a post.  
At the top of the page there is a navbar with a blog's logo, which redirects to "MyBlog" page and two other links.  

If user is not logged in they see:
> **Register** and **Log In**.

If user is logged in they see:
> **Create Post** and **Log Out**

## _Create Post_
On this page logged in users can create their own post. They they have to provide a **Title** and **Text** for a post. Also the is an option to provide an **Image**. However not all of the image extensions are allowed. Supported extensions are:
- 'pdf'
- 'png'
- 'jpg'
- 'jpeg'
- 'gif'  

Attached file's width should not be less the half the height 
```
(width / height) > 0.5
```

And file's heigh should not be three times less than the height
```
(width / height) < 3
```
