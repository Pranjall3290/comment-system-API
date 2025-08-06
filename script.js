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
