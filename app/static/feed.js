// Sample data (you can replace it with your actual data)
const blogs = [
    { title: "Blog 1", link: "https://example.com/blog1" },
    { title: "Blog 2", link: "https://example.com/blog2" },
    { title: "Blog 3", link: "https://example.com/blog3" },
    // Add more blogs as needed
];

// Function to render blogs
function renderBlogs() {
    const blogsContainer = document.getElementById('blogs-container');
    blogsContainer.innerHTML = '';
    blogs.forEach(blog => {
        const blogElement = document.createElement('div');
        blogElement.classList.add('blog');
        blogElement.textContent = blog.title;
        blogElement.addEventListener('click', () => {
            window.location.href = blog.link;
        });
        blogsContainer.appendChild(blogElement);
    });
}

// Initial render
renderBlogs();
