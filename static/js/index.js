document.addEventListener('DOMContentLoaded', function () {

  // Drag-to-compare sliders
  document.querySelectorAll('.compare-range').forEach(function (range) {
    range.addEventListener('input', function (e) {
      var val = e.target.value;
      var container = e.target.closest('.compare');
      if (!container) return;
      var img = container.querySelector('.compare-overlay');
      var handle = container.querySelector('.compare-handle');
      if (img) img.style.clipPath = 'inset(0 0 0 ' + val + '%)';
      if (handle) handle.style.left = val + '%';
    });
  });

  // BibTeX copy-to-clipboard
  var copyBtn = document.querySelector('.bibtex-copy');
  var bibtexPre = document.querySelector('.bibtex-wrap pre');
  if (copyBtn && bibtexPre) {
    var copyTimeout;
    copyBtn.addEventListener('click', function () {
      var text = bibtexPre.textContent;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).catch(function () {});
      }
      copyBtn.classList.add('is-copied');
      copyBtn.setAttribute('aria-label', 'Copied');
      clearTimeout(copyTimeout);
      copyTimeout = setTimeout(function () {
        copyBtn.classList.remove('is-copied');
        copyBtn.setAttribute('aria-label', 'Copy BibTeX');
      }, 1600);
    });
  }

});
