(function(){
  const jquery_version = '3.4.1';
  const site_url = 'https://127.0.01:8000';
  const static_url = site_url + 'static/'
  const min_width = 100;
  const min_height = 100;

  function bookmarklet(msg){

  }

  if(typeof window.jquery !== 'undefined'){
    bookmarklet();
  }else{
    const conflict = typeof window.$ != 'undefined';
    const script = document.createElement('script');
    script.src = `//ajax.googleapis.com/ajax/libs/jquery/${jquery_version}/jquery.min.js`
    document.head.appendChild(script);
    const attempts = 15;
    (function(){
      if(typeof window.jquery == 'undefined'){
        if(--attempts > 0) {
          window.setTimeout(arguments.callee, 250)
          }else{
        alert('An error occured while loading jQuery');
        }
     }else{
      bookmarklet();
     }
   })();
  }
})();