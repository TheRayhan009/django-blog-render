# Django Blog & Image Gallery

This project is a Django-based web application that includes a blog platform and an image gallery. It allows users to sign up, log in, post blogs, upload images, and interact with content by liking, disliking, and commenting.

## Features

- **User Authentication**: Users can sign up, log in, and manage their profiles.
- **Blog Posting**: Authenticated users can create, edit, and delete blog posts.
- **Image Gallery**: Users can upload images to a public gallery where others can like, dislike, and comment.
- **Search Functionality**: Users can search for blog posts based on titles.
- **Likes & Dislikes**: Users can like or dislike images in the gallery.
- **Comments**: Users can comment on blog posts.

## Project Structure

- **home**: The homepage that displays recent blog posts.
- **signin**: Handles user sign-up.
- **login**: Handles user login and session management.
- **Dblog**: Displays a detailed view of a single blog post along with comments.
- **search**: Allows users to search for blog posts by title.
- **blog**: Displays all blog posts with pagination.
- **myprofile**: User profile page that shows the user's blogs, images, likes, and dislikes.
- **postblog**: Allows users to create new blog posts.
- **image**: Displays the image gallery.
- **postimage**: Allows users to upload new images.
- **edit**: Allows users to edit their blog posts.
- **delete**: Handles blog post deletion with confirmation.
- **like**: Handles liking of images.
- **dislike**: Handles disliking of images.
- **logout**: Handles user logout and session termination.

## Models

- **Users**: Stores user information including username, password, email, and profile image.
- **UBlog**: Stores blog post details including title, content, image, category, and post date.
- **Comment**: Stores comments made by users on blog posts.
- **UPImage**: Stores images uploaded by users, along with their likes and dislikes count.
- **Likes**: Tracks which users have liked specific images.
- **DisLikes**: Tracks which users have disliked specific images.

## How to Run the Project

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
    ```

## Access the Application

Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Templates

- **`home.html`**: Displays the homepage with a list of recent blogs.
- **`signin.html`**: Sign-up page for new users.
- **`login.html`**: Login page for existing users.
- **`Dblog.html`**: Detailed blog post page with comments.
- **`search.html`**: Search results page.
- **`allblogs.html`**: Page to display all blogs with pagination.
- **`Uprofile.html`**: User profile page.
- **`postBlog.html`**: Page to create a new blog post.
- **`image.html`**: Image gallery page.
- **`postImage.html`**: Page to upload new images.
- **`Bedit.html`**: Page to edit existing blog posts.
- **`delete.html`**: Confirmation page for deleting blog posts.

## Static Files

Static files (CSS, JavaScript, images) are stored in the `static` directory and are served during development.

## Media Files

User-uploaded files such as images are stored in the `media` directory. Make sure to configure your Django settings to handle media files correctly.

## Additional Notes

- Ensure that you have properly set up the database configurations in `settings.py`.
- Use the Django admin interface to manage users, blogs, comments, images, likes, and dislikes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.


