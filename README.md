# MyBlog

#### Video Demo:  https://www.youtube.com/watch?v=r8cbJpA9-bQ&ab_channel=OmarHamid

# ***Description:***
This project is a blog application where user can read posts and create their own.Also users can attach an image to their post.
# ***Functionality:***

### **_MyBlog_**
On the main page there are posts in order from new to old.Each post has a **Title**, **Body**, **Date** and **Author**.**Images** are optional.Image's size is depending on its dimensions in order to make post better looking.  
If user is logged in - they can delete their post by clicking on a **Delete** button which is located at the bottom of a post.  
At the top of the page there is a navbar with a blog's logo, which redirects to "MyBlog" page and two other links.  

If user is not logged in they see:
> **Register** and **Log In**.

If user is logged in they see:
> **Create Post** and **Log Out**

### **_Create Post_**
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
<br/><br/>
# ***Future development***

### **_Password requirements_**
Now password can contain any number and types of characters, which is bad for security because passwords may be very weak.  
In future It will be necessary to require from the user more complicated password.

### **_Multiple files_**
Now users are allowed to attach only one file to theirs posts. However users would like to use more than one file in their posts.
This feature will improve user experience

### **_More file types_**
It would be a good feature if users can upload not only images but different file types as well, such as video files or code
<br/><br/>

# **_Struggles/Issues_**

### **_Image storage_**
For this project I was storing posts' images in **static folder** in order to retrieve them easily in templates. The path to each image was stored in my database. However I think this method is unnecessary complicated. Real web applications use different methods to store the images, but since this is my firs project and I am not familiar with those services yet I decided to store images in my **static folder**


### **_Image formatting_**
Some images with uncommon dimensions may cause unpretty view of a post. So i decided to implement some restrictions to uploaded images.  
Also images with different dimensions are rendered differently in the post, however this algorithm is very simple and should be improved in order to allow users upload files with any dimensions and render each one uniquely, depended in their dimensions