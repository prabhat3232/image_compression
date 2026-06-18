function initCompressWidget(formId) {
  const form = document.getElementById(formId);
  if (!form) return;

  form.addEventListener('submit', async function (e) {
    e.preventDefault();
    const btn = form.querySelector('button[type="submit"]');
    const status = form.querySelector('.compress-status');
    const original = btn.innerHTML;
    btn.disabled = true;
    btn.innerHTML = 'Compressing...';
    if (status) status.textContent = '';

    try {
      const res = await fetch('/compress', { method: 'POST', body: new FormData(form) });
      const data = await res.json();
      if (!res.ok || data.status !== 'success') throw new Error(data.error || 'Compression failed');

      const a = document.createElement('a');
      a.href = data.download_url;
      a.download = data.filename;
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);

      if (data.original_size && data.compressed_size) {
        const saved = ((1 - data.compressed_size / data.original_size) * 100).toFixed(1);
        if (status) status.textContent = `Saved ${saved}% (${formatBytes(data.original_size)} → ${formatBytes(data.compressed_size)})`;
      } else if (status) {
        status.textContent = 'Download started.';
      }
    } catch (err) {
      if (status) status.textContent = 'Error: ' + err.message;
      else alert('Error: ' + err.message);
    } finally {
      btn.disabled = false;
      btn.innerHTML = original;
    }
  });
}

function formatBytes(n) {
  if (n < 1024) return n + ' B';
  if (n < 1048576) return (n / 1024).toFixed(1) + ' KB';
  return (n / 1048576).toFixed(2) + ' MB';
}

document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('[data-compress-widget]').forEach(function (el) {
    initCompressWidget(el.id);
  });
});
