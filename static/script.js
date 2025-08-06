const API = '/comments';

async function loadComments() {
  const res = await fetch(API);
  const comments = await res.json();
  const list = document.getElementById('comment-list');
  list.innerHTML = '';

  comments.forEach((c) => {
    const li = document.createElement('li');
    li.innerHTML = `${c.author}: ${c.text} 
    <button onclick="deleteComment(${c.id})">🗑</button>`;
    list.appendChild(li);
  });
}

async function addComment() {
  const author = document.getElementById('author').value;
  const text = document.getElementById('text').value;
  if (!author || !text) return alert('Both fields required!');

  await fetch(API, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ author, text }),
  });

  document.getElementById('author').value = '';
  document.getElementById('text').value = '';
  loadComments();
}

async function deleteComment(id) {
  await fetch(`${API}/${id}`, { method: 'DELETE' });
  loadComments();
}

window.onload = loadComments;
const API_BASE = '';

// Load comments when page loads
document.addEventListener('DOMContentLoaded', loadComments);

async function loadComments() {
    try {
        const response = await fetch(`${API_BASE}/comments`);
        const comments = await response.json();
        
        const commentList = document.getElementById('comment-list');
        commentList.innerHTML = '';
        
        comments.forEach(comment => {
            const li = document.createElement('li');
            li.innerHTML = `
                <strong>${comment.author}</strong>: ${comment.text}
                <small style="color: #666; display: block; margin-top: 5px;">
                    ${new Date(comment.timestamp).toLocaleString()}
                </small>
                <button onclick="deleteComment(${comment.id})">Delete</button>
            `;
            commentList.appendChild(li);
        });
    } catch (error) {
        console.error('Error loading comments:', error);
    }
}

async function addComment() {
    const author = document.getElementById('author').value;
    const text = document.getElementById('text').value;
    
    if (!author || !text) {
        alert('Please fill in both fields');
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE}/comments`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ author, text })
        });
        
        if (response.ok) {
            document.getElementById('author').value = '';
            document.getElementById('text').value = '';
            loadComments(); // Reload comments
        } else {
            alert('Error adding comment');
        }
    } catch (error) {
        console.error('Error adding comment:', error);
        alert('Error adding comment');
    }
}

async function deleteComment(commentId) {
    try {
        const response = await fetch(`${API_BASE}/comments/${commentId}`, {
            method: 'DELETE'
        });
        
        if (response.ok) {
            loadComments(); // Reload comments
        } else {
            alert('Error deleting comment');
        }
    } catch (error) {
        console.error('Error deleting comment:', error);
        alert('Error deleting comment');
    }
}
